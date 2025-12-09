const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end("🚀 Nouvelle version déployée automatiquement via CI/CD !\n");
});

server.listen(80, () => {
    console.log("Server running on port 80");
});
