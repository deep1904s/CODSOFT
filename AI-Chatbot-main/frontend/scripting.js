// script.js

function sendMessage() {
    // Get user input
    var userInput = document.getElementById("user-input").value;
    
    // Clear input field
    document.getElementById("user-input").value = "";
    
    // Display user message
    var chatMessages = document.getElementById("chat-messages");
    var userMessage = "<div class='chat-message user-message'>User: " + userInput + "</div>";
    chatMessages.innerHTML += userMessage;
    chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
    
    // Send user message to backend server
    fetch("/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userInput,
            user_id: "123" // Dummy user ID (replace with actual user identification)
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot response
        var chatbotMessage = "<div class='chat-message chatbot-message'>Chatbot: " + data.response + "</div>";
        chatMessages.innerHTML += chatbotMessage;
        chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
    });
}

// Add event listener for send button click
document.getElementById("send-button").addEventListener("click", sendMessage);

// Add event listener for Enter key press in input field
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
