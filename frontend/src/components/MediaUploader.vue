<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

const props = defineProps({
  modelValue: Array
})

const emit = defineEmits(['update:modelValue'])

const handleFileChange = (event: Event) => {
  const files = (event.target as HTMLInputElement).files
  if (files) {
    emit('update:modelValue', Array.from(files))
  }
}
</script>

<template>
  <input type="file" multiple @change="handleFileChange" />
</template>

<style scoped>
input[type="file"] {
  margin-top: 10px;
}
</style>
