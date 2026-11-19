// Minimal client for Unreal's MCP server (streamable HTTP), for when the agent's own MCP link is down.
// Usage: node mcp_call.mjs <script.py>            -> runs ProgrammaticToolset.execute_tool_script with the file's text
//        node mcp_call.mjs --tool <toolset> <tool> '<json args>'
// Prints the tool result text. Exit code 1 on an MCP error.
import { readFileSync } from "node:fs";

const URL_ = process.env.UE_MCP_URL || "http://127.0.0.1:8000/mcp";
let session = null;
let nextId = 1;

async function rpc(method, params, notify = false) {
  const body = { jsonrpc: "2.0", method, params };
  if (!notify) body.id = nextId++;
  const headers = { "Content-Type": "application/json", Accept: "application/json, text/event-stream" };
  if (session) headers["Mcp-Session-Id"] = session;
  const res = await fetch(URL_, { method: "POST", headers, body: JSON.stringify(body) });
  const sid = res.headers.get("mcp-session-id");
  if (sid) session = sid;
  if (notify) return null;
  const text = await res.text();
  // Either plain JSON or an SSE stream whose data lines carry JSON-RPC messages.
  const msgs = text.trim().startsWith("{")
    ? [JSON.parse(text)]
    : text.split("\n").filter((l) => l.startsWith("data:")).map((l) => JSON.parse(l.slice(5)));
  const reply = msgs.find((m) => m.id === body.id);
  if (!reply) throw new Error(`no reply to ${method}: ${text.slice(0, 300)}`);
  if (reply.error) throw new Error(JSON.stringify(reply.error));
  return reply.result;
}

const args = process.argv.slice(2);
let toolset, tool, toolArgs;
if (args[0] === "--tool") {
  [toolset, tool] = [args[1], args[2]];
  toolArgs = JSON.parse(args[3] || "{}");
} else {
  toolset = "editor_toolset.toolsets.programmatic.ProgrammaticToolset";
  tool = "execute_tool_script";
  toolArgs = { script: readFileSync(args[0], "utf8") };
}

await rpc("initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "mus-build", version: "1" } });
await rpc("notifications/initialized", {}, true);
const result = await rpc("tools/call", { name: "call_tool", arguments: { toolset_name: toolset, tool_name: tool, arguments: toolArgs } });
const out = (result.content || []).map((c) => c.text ?? "").join("\n");
console.log(out);
process.exit(result.isError ? 1 : 0);
