// mcp-server.js
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/mcp', (req, res) => {
    console.log('[MCP RECEIVED]', req.body);
    // Example: Echo response
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
