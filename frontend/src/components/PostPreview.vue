<script setup lang="ts">
import { defineProps, computed } from 'vue'
import SocialMediaSelector from "@/components/SocialMediaSelector.vue";

const props = defineProps({
  content: String,
  media: Array,
  platform: String
})

const platformClass = computed(() => {
  return `post-preview-${props.platform}`
})
</script>

<template>
  <div class="post-preview-container">
    <social-media-selector />
    <div :class="['post-preview', platformClass]">
      <p>{{ content }}</p>
      <div v-if="media.length">
        <img v-for="file in media" :src="URL.createObjectURL(file)" :key="file.name" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-preview {
  color: black;
}

.post-preview-container {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.social-media-selector {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
}

button {
  background: none;
  border: none;
  cursor: pointer;
}

img {
  width: 30px;
  height: 30px;
}

.post-preview {
  margin-top: 20px;
}

.post-preview img {
  max-width: 100px;
  margin-right: 10px;
}

.post-preview-facebook {
  /* Facebook specific styles */
}

.post-preview-twitter {
  /* Twitter specific styles */
}

.post-preview-instagram {
  /* Instagram specific styles */
}
</style>
