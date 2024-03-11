<template>
  <div class="card shadow-none">
    <div class="card-body">
      <div class="d-flex justify-content-start align-items-start gap-4">
        <img src="/avatar3.png" width="60" height="60" class="img-fluid rounded-circle" alt="">
        <div class="actions" style="width: 100%;">
          <v-textarea v-model="requestData.comment" label="" variant="outlined" clearable></v-textarea>

          <div class="d-flex gap-2">
            <v-btn color="secondary" size="small" rounded="xl" flat>
              Cancel
            </v-btn>

            <emoji-picker @emoji-click="hanlePickEmoji" />

            <v-btn color="secondary" size="small" rounded="xl" flat>
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
  components: {
    EmojiPicker
  },
  setup () {
    const requestData = ref({
      comment: ''
    })
    return {
      requestData
    }
  },
  methods: {
    hanlePickEmoji (emoji) {
      // Adds an emoji selected by the user to the text of the
      // text area field
      this.requestData.comment = this.requestData.comment + emoji
    }
  }
}
</script>
