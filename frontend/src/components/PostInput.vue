<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  modelValue: String
})

const emit = defineEmits(['update:modelValue'])

const updateValue = (event: Event) => {
  emit('update:modelValue', (event.target as HTMLInputElement).value)
}
</script>

<template>
  <textarea :value="modelValue" @input="updateValue" placeholder="What's on your mind?"></textarea>
</template>

<style scoped>
textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  font-size: 16px;
}
</style>
