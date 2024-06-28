
function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    
    document.getElementById("user-input").value = "";
    
    var chatMessages = document.getElementById("chat-messages");
    var userMessage = "<div class='chat-message user-message'>User: " + userInput + "</div>";
    chatMessages.innerHTML += userMessage;
    chatMessages.scrollTop = chatMessages.scrollHeight; 
    
    fetch("/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userInput,
            user_id: "123" 
        })
    })
    .then(response => response.json())
    .then(data => {
        var chatbotMessage = "<div class='chat-message chatbot-message'>Chatbot: " + data.response + "</div>";
        chatMessages.innerHTML += chatbotMessage;
        chatMessages.scrollTop = chatMessages.scrollHeight; 
    });
}

document.getElementById("send-button").addEventListener("click", sendMessage);

document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
