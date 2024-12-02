<template>
    <div class="unclassified-face-list">
      <h2>未分類の顔</h2>
      <ul>
        <li v-for="face in unclassifiedFaces" :key="face.id">
          <img :src="face.imageUrl" alt="未分類の顔" />
          <button @click="classifyFace(face)">分類する</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'UnclassifiedFaceList',
    computed: {
      unclassifiedFaces() {
        return this.$store.getters.unclassifiedFaces
      }
    },
    methods: {
      classifyFace(face) {
        // 顔を分類するロジックをここに実装
      }
    }
  }
  </script>