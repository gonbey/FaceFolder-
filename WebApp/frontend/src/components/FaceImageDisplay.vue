<template>
    <div class="face-image-display">
      <h2>顔画像表示</h2>
      <div v-for="face in detectedFaces" :key="face.id">
        <img :src="face.imageUrl" :alt="face.name || '未分類'" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FaceImageDisplay',
    computed: {
      detectedFaces() {
        return this.$store.state.detectedFaces
      }
    }
  }
  </script>