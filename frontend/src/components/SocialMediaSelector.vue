<script setup lang="ts">
import { defineEmits } from 'vue'

const emit = defineEmits(['selectPlatform'])

const platforms = ['facebook', 'X', 'instagram']

const selectPlatform = (platform: string) => {
  emit('selectPlatform', platform)
}
</script>

<template>
  <div class="social-media-selector">
    <button v-for="platform in platforms" :key="platform" @click="selectPlatform(platform)">
      <img :src="`./src/assets/icons/${platform}.png`" :alt="platform" />
    </button>
  </div>
  <hr>
</template>

<style scoped>

.social-media-selector {
  display: flex;
  gap: 10px;
  justify-content: left;
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
</style>
