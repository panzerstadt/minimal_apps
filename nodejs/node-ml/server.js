//https://medium.com/shovel-apps/simple-node-js-server-on-heroku-210ec24f485

var static = require("node-static");
var file = new static.Server();

require('http').createServer(function(request, response) {
    request.addListener('end', function() {
        console.log("serving", request);
        file.serve(request, response);
    }).resume();
}).listen(process.env.PORT || 3000);
console.log('have a look in port 3000!');