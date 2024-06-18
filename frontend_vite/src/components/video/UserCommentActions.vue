<template>
  <div class="card shadow-none">
    <div class="card-body">
      <div class="d-flex justify-content-start align-items-start gap-4">
        <img src="/avatar3.png" width="60" height="60" class="img-fluid rounded-circle" alt="">
        <div class="actions" style="width: 100%;">
          <v-textarea v-model="requestData.content" label="" variant="outlined" clearable></v-textarea>
          
          <div class="d-flex gap-2">
            <v-btn color="secondary" size="small" rounded="xl" flat>
              Cancel
            </v-btn>

            <emoji-picker @emoji-click="hanlePickEmoji" />

            <v-btn color="secondary" size="small" rounded="xl" flat @click="requestCreateComment">
              <font-awesome-icon icon="fas fa-comment" class="me-2" />
              Comment
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

import EmojiPicker from '../../components/emojis/EmojiPicker.vue'

export default {
  name: 'UserCommentActions',
  components: {
    EmojiPicker
  },
  emits: {
    'new-comment' () {
      return true
    }
  },
  setup () {
    const requestData = ref({ content: '' })
    return { requestData }
  },
  methods: {
    async requestCreateComment () {
      // Creates a new comment for the video that
      // the user is currently viewing
      try {
        const videoID = this.$route.params.id
        const response = await this.$client.post(`/comments/${videoID}/create`, this.requestData)
        this.requestData.content = ''
        this.$emit('new-comment', response.data)
      } catch (e) {
        console.error(e)
      }
    },
    hanlePickEmoji (emoji) {
      // Adds an emoji selected by the user to the text of the
      // text area field
      this.requestData.comment = this.requestData.comment + emoji
    }
  }
}
</script>
