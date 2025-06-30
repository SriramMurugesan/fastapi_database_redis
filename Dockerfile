# Dockerfile for Node-based MCP server
FROM node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy rest of the app code
COPY . .

# Expose MCP server port
EXPOSE 3000

# Start the MCP server
CMD ["node", "mcp-server.js"]
