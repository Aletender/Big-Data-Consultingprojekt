<script setup lang="ts">
import PostInput from '../components/PostInput.vue'
import MediaUploader from '../components/MediaUploader.vue'
import PostPreview from '../components/PostPreview.vue'
import PostActions from '../components/PostActions.vue'
import SocialMediaSelector from '../components/SocialMediaSelector.vue'
import { ref } from 'vue'

const postContent = ref('')
const mediaFiles = ref([])
const selectedPlatform = ref('facebook')

const handlePostSubmit = () => {
  // Handle post submission logic
}

const handlePlatformSelect = (platform: string) => {
  selectedPlatform.value = platform
}
</script>

<template>
  <div class="post-editor">
    <PostInput v-model="postContent" />
    <!--<MediaUploader v-model="mediaFiles" /> -->
    <PostActions @submit="handlePostSubmit" />
  </div>

  <div class="post-preview">
    <PostPreview :content="postContent" :media="mediaFiles" :platform="selectedPlatform" />
  </div>
</template>

<style scoped>
.post-editor {
  width: 100%;
  padding: 25px;
}

.post-preview {
  padding: 25px;
  width: 100%;
}
</style>
