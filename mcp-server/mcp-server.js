// mcp-server.js
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/mcp', (req, res) => {
    console.log('[MCP RECEIVED]', req.body);

    res.json({
        context: req.body.context,
        response: {
            text: `You said: ${req.body.context.text}`,
        }
    });
});

app.listen(port, () => {
    console.log(`✅ MCP Server running at http://localhost:${port}/mcp`);
});
import { serve } from "@modelcontextprotocol/server-http";

serve({
  async onInput({ context }) {
    console.log("🟢 Received context:", context);
    return {
      response: { text: `Echo: ${context.text}` }
    };
  },
  port: 3000
});
