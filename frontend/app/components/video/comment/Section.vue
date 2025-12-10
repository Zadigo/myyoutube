<template>
  <volt-card>
    <template #content>
      <div class="flex items-center justify-between">
        <h2 v-if="comments" class="h4 m-0">
          {{ comments.length }} comments
        </h2>

        <volt-dropdown id="comment-sorting" :items="sortActionsMenuItem">
          <template #default="{ attrs }">
            <volt-button @click="attrs.toggle">
              <icon name="i-lucide-sort-asc" />
            </volt-button>
          </template>
        </volt-dropdown>
      </div>

      <volt-divider class="my-3" />

      <!-- Actions -->
      <video-comment-section-actions @new-comment="handleNewComment" />

      <volt-divider class="my-5" />

      <!-- Comments -->
      <video-comment-card-item v-for="comment in pinnedComments" :key="comment.id" :comment="comment" />
      <video-comment-card-item v-for="comment in unpinnedComments" :key="comment.id" :comment="comment" />
    </template>
  </volt-card>
</template>

<script setup lang="ts">
import { useCommentsComposable } from '~/composables/use'
import { commentsFixture } from '~/data/fixtures'
import type { VideoComment } from '~/types'

const sortActions = [
  'Newest',
  'Oldest',
  'Most popular',
  'Least popular'
] as const

type SortActions = (typeof sortActions)[number]

type SortActionsMenuItem = {
  label: SortActions
}

/**
 * Comments
 */

const comments = ref<VideoComment[]>(commentsFixture)
const { comments: allComments, pinnedComments, unpinnedComments, sortCommentsBy } = await useCommentsComposable()

const sortActionsMenuItem: SortActionsMenuItem[] = sortActions.map(action => {
  return {
    label: action,
    command: sortCommentsBy
  }
})

/**
 * New comment
 */

/**
 * Append the newly created comment by implementing it
 * at the start of the current comment list
 * @todo - Send to backend
 */
async function handleNewComment (comment: VideoComment) {
  if (comments.value) {
    comments.value.unshift(comment)
  }
}
</script>
