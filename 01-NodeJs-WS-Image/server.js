var os = require('os');
var http = require('http');

var handleRequest = function(request, response) {
  response.writeHead(200);
  response.end("시험삼아 해보는 웹페이지. 호스트는?  " + os.hostname());
  
  console.log("[" + Date(Date.now()).toLocaleString() + "] " + os.hostname());
}

var www = http.createServer(handleRequest);

www.listen(8080);
