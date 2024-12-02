<template>
    <div class="person-list">
      <h2>人物リスト</h2>
      <ul>
        <li v-for="person in personGroups" :key="person.id">
          {{ person.name }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PersonList',
    computed: {
      personGroups() {
        return this.$store?.state?.personGroups || []
      }
    }
  }
  </script>