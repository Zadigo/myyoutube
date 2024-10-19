<template>
  <div class="card-body">
    <h4>Age restriction</h4>
    <p class="text-muted">
      Choose when to publish and who can see your video
    </p>
    
    <v-switch label="Age restricted" inset />

    <h4>Visibility</h4>
    <p class="text-muted">
      Choose when to publish and who can see your video
    </p>

    <v-date-picker />
    
    <v-switch label="Public" inset />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'VideoVisiblityComponent'
})
</script>
