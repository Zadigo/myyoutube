<template>
  <section id="comments">
    <u-card>
      <div class="flex items-center justify-between">
        <h2 v-if="comments" class="h4 m-0">
          {{ comments.length }} comments
        </h2>

        <u-dropdown-menu id="comment-sorting" :items="sortActionsMenuItem">
          <u-button>
            <icon name="i-lucide-sort-asc" />
          </u-button>
        </u-dropdown-menu>
      </div>

      <u-separator class="my-3" />

      <!-- Actions -->
      <video-comment-section-actions @new-comment="(comment) => { void handleNewComment(comment) }" />
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

const currentVideo = inject<Ref<VideoDetails>>(CURRENT_VIDEO_SYMBOL)

/**
 * Comments
 */

const { comments, pinnedComments, unpinnedComments, sortCommentsBy } = await useCommentsComposable(currentVideo)

const sortActionsMenuItem: SortActionsMenuItem[] = sortActions.map(action => {
  return {
    label: action,
    onSelect: () => void sortCommentsBy(action)
  }
})

/**
 * New comment
 */

/**
 * Prepend the newly created comment to the pinned or unpinned comments list depending on its pinned status
 */
const handleNewComment = async (comment: VideoComments) => {
  if (comments.value) {
    // comments.value.unshift(comment)
  }
}
</script>
