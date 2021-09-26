document.getElementById("send_btn").addEventListener("click", function(event) {
	event.preventDefault();
	// var message_element = document.getElementsByTagName("input")[0];

  var message_element = document.getElementById("text_input");
  var message = message_element.value;

  if (message.toString().length) {
		// var username = localStorage.getItem("username");
    var username = "Vincent"

		var data = {
			type: "message",
			username: username,
			message: message
		};

		// var time_now = this.getCurrentTime();
		// alert(time_now);

		MessageAdd(message);
		// websocket.send(JSON.stringify(data));
    // find ways to append message to json file
		message_element.value = "";
	}


}, false);


function MessageAdd(message) {
	var chat_messages = document.getElementById("chat");

	var today = new Date();
	var hours = today.getHours()
	var minutes = today.getMinutes()
	if (hours < 10){
		hours = "0" + hours
	}

	if (minutes < 10){
		minutes = "0" + minutes
	}

	var time = hours + ":" + minutes;

  var chat_bubble_html = '<li class="me"><div class="entete"><h3 style="padding-right:5px">' + time +', Today</h3><h2> Me</h2><span class="status blue"></span></div><div class="message">' + message + '</div></li>'


	chat_messages.insertAdjacentHTML("beforeend", chat_bubble_html);
	chat_messages.scrollTop = chat_messages.scrollHeight;
}

function congrats_msg(){
	alert("Congratulation! Successfully match");
}
