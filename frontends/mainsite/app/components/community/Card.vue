<template>
  <u-card class="shadow-sm">
    <h3 class="font-semibold text-lg">{{ note.node.title }}</h3>
    <p class="text-sm text-gray-600">{{ note.node.description }}</p>

    <u-button :to="`/community-notes/${note.node.reference}`" size="sm" variant="solid" class="mt-2">
      View Note
    </u-button>
  </u-card>
</template>

<script setup lang="ts">
import type { CommunityNoteNode } from '#shared/types/moderation'

defineProps<{ note: CommunityNoteNode }>()
</script>
