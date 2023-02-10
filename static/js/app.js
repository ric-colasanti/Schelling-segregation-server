console.log("here");
var socket = io.connect();
socket.emit('message', JSON.stringify({size:20,density: 0.8}));

//receive details from server
socket.on("data", function (data) {
  console.log(data);

  
});
