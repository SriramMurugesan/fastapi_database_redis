FROM node:20-alpine
WORKDIR /app
COPY package.json .
COPY mcp-server.js .
RUN npm install
EXPOSE 3000
CMD ["node", "mcp-server.js"]
