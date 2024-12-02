<template>
    <div class="merge-split-operations">
      <h2>マージ・分離操作</h2>
      <button @click="mergeFaces">似た顔をマージ</button>
      <button @click="splitFaces">異なる画像を分離</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MergeSplitOperations',
    methods: {
      mergeFaces() {
        // マージ操作のロジックをここに実装
      },
      splitFaces() {
        // 分離操作のロジックをここに実装
      }
    }
  }
  </script>