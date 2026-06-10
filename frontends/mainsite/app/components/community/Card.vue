<template>
  <volt-card class="shadow-sm">
    <template #content>
      <h3 class="font-semibold text-lg">{{ note.node.title }}</h3>
      <p class="text-sm text-gray-600">{{ note.node.description }}</p>

      <nuxt-link-locale :to="`/community-notes/${note.node.reference}`" size="small" variant="primary" class="mt-2">
        <volt-button>
          View Note
        </volt-button>
      </nuxt-link-locale>
    </template>
  </volt-card>
</template>

<script setup lang="ts">
import type { CommunityNoteNode } from '~/types'

defineProps<{ note: CommunityNoteNode }>()
</script>
