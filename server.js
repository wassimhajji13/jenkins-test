const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end("Hello Wassim! Your Docker image is working.\n");
});

server.listen(80, () => {
    console.log("Server running on port 80");
});
