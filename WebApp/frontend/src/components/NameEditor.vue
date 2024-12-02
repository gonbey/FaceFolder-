<template>
    <div class="name-editor">
      <h2>名称編集</h2>
      <input v-model="newName" @keyup.enter="updateName" />
      <button @click="updateName">更新</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NameEditor',
    data() {
      return {
        newName: ''
      }
    },
    methods: {
      updateName() {
        // 名前の更新ロジックをここに実装
      }
    }
  }
  </script>