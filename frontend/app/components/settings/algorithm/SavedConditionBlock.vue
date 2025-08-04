<template>
  <div v-if="condition">
    <p>Show me videos when...</p>
    <span class="badge badge-success">{{ condition.theme }}</span>
    <span>Matches these keywords...</span>
    <span v-for="keyword in condition.keywords" :key="keyword" class="badge badge-warning">{{ keyword }}</span>
    <span>Which appear in these sections of the video...</span>
    <span v-for="section in condition.video_sections" :key="section" class="badge badge-warning">{{ section }}</span>
  </div>
</template>

<script setup lang="ts">
import type { AlgorithmConditionBlock } from '~/data'

defineProps<{ condition: AlgorithmConditionBlock | undefined }>()
</script>
