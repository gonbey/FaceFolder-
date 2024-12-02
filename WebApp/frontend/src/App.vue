<template>
  <div id="app">
    <PersonList />
    <FaceImageDisplay />
    <NameEditor />
    <MergeSplitOperations />
    <UnclassifiedFaceList />
  </div>
</template>

<script>
import PersonList from './components/PersonList.vue'
import FaceImageDisplay from './components/FaceImageDisplay.vue'
import NameEditor from './components/NameEditor.vue'
import MergeSplitOperations from './components/MergeSplitOperations.vue'
import UnclassifiedFaceList from './components/UnclassifiedFaceList.vue'

export default {
  name: 'App',
  components: {
    PersonList,
    FaceImageDisplay,
    NameEditor,
    MergeSplitOperations,
    UnclassifiedFaceList,
  }
}
</script>