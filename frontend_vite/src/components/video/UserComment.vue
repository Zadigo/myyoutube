<template>
  <article class="card shadow-none" aria-label="">
    <div class="card-body">
      <div class="d-flex align-items-start gap-4">
        <router-link :to="{ name: 'channel_details', params: { id: 'ch_noienozinfoz' } }" aria-label="">
          <v-img src="/avatar2.png" width="80" height="80" class="img-fluid rounded-circle" alt=""></v-img>
        </router-link>

        <div class="content">
          <div class="mb-3">
            <v-btn :to="{ name: 'channel_details', params: { id: 'ch_noienozinfoz' } }" color="secondary" variant="plain">
              Lucie Paul
            </v-btn>
            <v-btn class="mx-2" disabled>3 weeks</v-btn>
            <v-btn disabled>Something</v-btn>
          </div>

          <p>{{ comment.content }}</p>

          <div class="my-3">
            <div class="badge badge-danger me-1">@creator</div>
            <div class="badge badge-light">Aimé par le creator</div>
          </div>

          <div class="d-flex gap-2 mt-4">
            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome-icon v-if="comment?.is_liked" icon="fas fa-thumbs-up" class="me-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-up" class="me-2" />
              12.3k
            </v-btn>
            
            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome-icon v-if="comment?.is_disliked" icon="fas fa-thumbs-down" class="me-2" />
              <font-awesome-icon v-else icon="far fa-thumbs-up" class="me-2" />
              24
            </v-btn>

            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome-icon icon="fas fa-comment" class="me-2" />
              Answer
            </v-btn>
          </div>

          <v-btn v-if="hasReplies" rounded="xl" color="secondary" variant="text" class="mt-3" @click="showReplies = !showReplies">
            Voir {{ comment.number_of_replies }} commentaires
          </v-btn>

          <!-- Replies -->
          <transition id="replies" tag="div" name="pop" mode="in-out">
            <div v-if="showReplies" class="replies">
              <user-reply v-for="i in 2" :key="i" :reply="{}" />
            </div>
          </transition>
        </div>
      </div>
    </div>
  </article>
</template>

<script>
import { ref } from 'vue'
import UserReply from './UserReply.vue'

export default {
  name: 'UserComment',
  components: {
    UserReply
  },
  props: {
    comment: {
      type: Object,
      default: () => {},
      required: false
    }
  },
  setup () {
    const showReplies = ref(false)

    return {
      showReplies
    }
  },
  computed: {
    hasReplies () {
      // Checks if the comment has replies
      return this.comment.number_of_replies >= 1
    }
  }
}
</script>
