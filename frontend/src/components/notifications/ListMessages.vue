<template>
  <div class="col-sm-12 col-md-8 offset-md-2">
    <comment-card-vue v-for="comment in comments" :key="comment.id" :comment="comment" class="mb-1" />
  </div>
</template>

<script>
import useTesting from '@/composables/testing'

import CommentCardVue from '../CommentCard.vue'

export default {
  name: 'ListMessages',
  components: {
    CommentCardVue
  },
  setup () {
    const { comments } = useTesting()
    return {
      comments
    }
  }
}
</script>
