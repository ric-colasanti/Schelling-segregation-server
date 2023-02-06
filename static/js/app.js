
var socket = io.connect();
socket.emit('message', "test");

//receive details from server
socket.on("data", function (data) {
  console.log(data);

  
});
