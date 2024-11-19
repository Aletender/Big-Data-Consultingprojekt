<script setup lang="ts">
import { defineEmits } from 'vue'

const emit = defineEmits(['submit'])

const handleSubmit = () => {
  emit('submit')
}
</script>

<template>
  <div class="post-actions">
    <button @click="handleSubmit">Submit</button>
    <button>Cancel</button>
  </div>
</template>

<style scoped>
.post-actions {
  margin-top: 20px;
}

button {
  margin-right: 10px;
}
</style>
