<script setup lang="ts">
import { ref } from 'vue'

const messages = ref([
  { text: 'Hello! How can I help you today?', sender: 'bot' }
])
const newMessage = ref('')

const sendMessage = () => {
  if (newMessage.value.trim() !== '') {
    messages.value.push({ text: newMessage.value, sender: 'user' })
    newMessage.value = ''
    // Simulate bot response
    setTimeout(() => {
      messages.value.push({ text: 'This is a simulated response.', sender: 'bot' })
    }, 1000)
  }
}
</script>

<template>
  <div class="chat-container">
    <header class="chat-header">
      <h1>ChatGPT</h1>
    </header>
    <div class="chat-messages">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.sender]">
        <p>{{ message.text }}</p>
      </div>
    </div>
    <div class="chat-input">
      <input v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type a message..." />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 800px;
  margin: 0 auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: white;
  color: black;
}

.chat-header {
  background-color: #f5f5f5;
  padding: 1rem;
  border-bottom: 1px solid #ddd;
  text-align: center;
  color: black;
}

.chat-messages {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
  background-color: white;
  color: black;
}

.message {
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  max-width: 70%;
  color: black;
}

.message.user {
  background-color: #e0f7fa;
  align-self: flex-end;
}

.message.bot {
  background-color: #f1f1f1;
  align-self: flex-start;
}

.chat-input {
  display: flex;
  padding: 1rem;
  border-top: 1px solid #ddd;
  background-color: white;
}

.chat-input input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 0.5rem;
  color: black;
  background-color: white;
}

.chat-input button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.chat-input button:hover {
  background-color: #0056b3;
}
</style>
