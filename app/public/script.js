// script.js

// Function to send a message to the backend API
function sendMessage() {
    const messageInput = document.getElementById('textInput');
    const message = messageInput.value;

    // Read the backend API URL from the global variable
    const apiUrl = window.apiUrl || 'https://default-backend-api-url.com';

    // Make a simple POST request using Fetch API
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        // Assuming your backend responds with the saved message details
        const { id, text } = data;

        // Display the sent message on the message board
        const messageList = document.getElementById('messageList');
        const listItem = document.createElement('li');
        listItem.textContent = text;
        messageList.appendChild(listItem);

        // Clear the input field
        messageInput.value = '';
    })
    .catch(error => console.error('Error:', error));
}
