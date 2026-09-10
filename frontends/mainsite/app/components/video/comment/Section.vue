<template>
  <section id="comments">
    <u-card>
      <div class="flex items-center justify-between">
        <h2 v-if="comments" class="h4 m-0">
          {{ comments.length }} comments
        </h2>

        <u-dropdown id="comment-sorting" :items="sortActionsMenuItem">
          <u-button>
            <icon name="i-lucide-sort-asc" />
          </u-button>
        </u-dropdown>
      </div>

      <u-separator class="my-3" />

      <!-- Actions -->
      <video-comment-section-actions @new-comment="handleNewComment" />
    </u-card>
    
    <!-- Comments -->
     <div class="my-10 space-y-2 max-w-6xl ms-auto">
       <video-comment-card-item v-for="comment in pinnedComments" :key="comment.node.id" :video-comment="comment" />
       <video-comment-card-item v-for="comment in unpinnedComments" :key="comment.node.id" :video-comment="comment" />
     </div>
  </section>
</template>

<script setup lang="ts">
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
