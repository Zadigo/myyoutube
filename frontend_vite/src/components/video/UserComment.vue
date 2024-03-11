<template>
  <article class="card shadow-none">
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

          <p>
            I can’t stop smiling. I once “borrowed “ my brother’s shoes
            and accidentally ran into him and his friends. The whole time i
            was talking to them his eyes were laser focused on the shoes. I
            tried cutting the conversation short but at some point he leaned
            closer and went “ is that my shoes“. He roasted me but it was all
            lighthearted and fun. I can totally relate to the sisters
          </p>

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

          <v-btn rounded="xl" color="secondary" variant="text" class="mt-3" @click="showReplies = !showReplies">
            Voir 2 commentaires
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
import { ref } from 'vue';
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
  }
}
</script>
