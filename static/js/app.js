document.addEventListener("DOMContentLoaded", () => {
  const sendButton = document.getElementById("sendButton");
  const userInput = document.getElementById("userInput");
  const chatContainer = document.getElementById('chatContainer');
  const chatHistory = document.getElementById("chatHistory");
  const wordLimit = 100;

  const resizeInputTextArea = () => {
    // Resize the text area based on its content
    userInput.style.height = "auto";
    userInput.style.height = Math.min(userInput.scrollHeight, 240) + "px"; // 240px max height
  };

  const scrollToBottom = () => {
    // Scroll to the bottom of the chat container
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  const addMessage = (text, isUser) => {
    const msg = document.createElement("div");
    // Adjust the message side based on whether it's from the user or the model
    msg.className = `p-3 rounded-xl max-w-[75%] ${
      isUser
        ? "self-end bg-blue-600 animate-fadeInRight"
        : "self-start bg-gray-700 animate-fadeInLeft"
    }`;
    msg.textContent = text;
    chatHistory.prepend(msg);
  };

  const sendText = async () => {
    const text = userInput.value.trim();
    if (!text) return;

    addMessage(text, true);
    userInput.value = "";
    userInput.style.height = "auto";

    wordLenght = text.split(/\s+/).length;
    if (wordLenght < wordLimit) {
      if (wordLenght === 1)
        addMessage(`Your essay contains only 1 word. Please enter at least ${wordLimit} words.`, false);
      else
        addMessage(`Your essay contains ${wordLenght} words. Please enter at least ${wordLimit} words.`, false);

      scrollToBottom();
      return;
    }

    const response = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    let confidence = parseFloat(data.confidence);
    let prediction = `Your essay is ${data.prediction} with ${(confidence * 100).toFixed(2)}% confidence.`;
    addMessage(prediction, false);
    scrollToBottom();
  };

  sendButton.addEventListener("click", sendText);
  userInput.addEventListener("input", resizeInputTextArea);
  // Send message on Enter key press but allow Shift+Enter for new lines
  userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendText();
    }
  });
});
