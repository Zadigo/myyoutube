<template>
  <section id="comments">
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
      </template>
    </volt-card>
    
    <!-- Comments -->
     <div class="my-10 space-y-2 max-w-6xl ms-auto">
       <video-comment-card-item v-for="comment in pinnedComments" :key="comment.node.id" :video-comment="comment" />
       <video-comment-card-item v-for="comment in unpinnedComments" :key="comment.node.id" :video-comment="comment" />
     </div>
  </section>
</template>

<script setup lang="ts">
import { useCommentsComposable } from '~/composables/use'
import type { VideoComments } from '~/types'

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

const { comments, pinnedComments, unpinnedComments, sortCommentsBy } = await useCommentsComposable()

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
async function handleNewComment (comment: VideoComments) {
  if (comments.value) {
    // comments.value.unshift(comment)
  }
}
</script>
