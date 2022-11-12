<template>
  <div :class="[shadow ? null : 'shadow-none']" class="card rounded-none">
    <div class="card-body">
      <div class="d-flex justify-content-around">
        <div class="me-3">
          <router-link :to="{ name: 'channel_view'}">
            <img :src="require('@/assets/avatar1.png')" class="img-fluid rounded-circle" alt="Image 1">
          </router-link>
        </div>

        <div clas="ms-1">
          <div class="d-flex justify-content-left align-items-center">
            <router-link :to="{ name: 'channel_view'}">
              <span class="fw-bold me-2">{{ comment.user.username }}</span>
            </router-link>
            <span class="text-muted">3 weeks ago</span>
            <font-awesome-icon v-if="comment.is_pinned" icon="fa-solid fa-thumbtack" class="text-warning mx-3" />
          </div>

          <p class="card-text">
            I can’t stop smiling. I once “borrowed “ my brother’s shoes and accidentally ran into him
            and his friends. The whole time i was talking to them his eyes were laser focused on the shoes. I tried
            cutting the conversation short but at some point he leaned closer and went “ is that my
            shoes“. He roasted me but it was all lighthearted and fun. I can totally relate to the
            sisters
          </p>

          <!-- NOTE: Make this a reusable component
          for all comment/reply cards -->
          <div class="my-3">
            <div class="badge badge-danger me-1">@creator</div>
            <div class="badge badge-light">{{ $t('Liked by x', { creator: 'creator' }) }}</div>
          </div>

          <div class="btn-group shadow-none btn-rounded">
            <button type="button" class="btn btn-primary btn-sm shadow-none" @click="likeComment">
              <font-awesome-icon icon="fa-solid fa-thumbs-up" class="me-2"></font-awesome-icon>
              12.3k
            </button>
            <button type="button" class="btn btn-primary btn-sm shadow-none" @click="likeComment">
              <font-awesome-icon icon="fa-solid fa-thumbs-down" class="me-2"></font-awesome-icon>
              24
            </button>
            <button type="button" class="btn btn-info btn-sm shadow-none" @click="showReplyInput = !showReplyInput">
              <font-awesome-icon icon="fa-solid fa-message" class="me-2"></font-awesome-icon>
              {{ $t('Reply') }}
            </button>
          </div>

          <input v-if="showReplyInput" :placeholder="`${$t('Reply to x', { user: comment.user.username })}`" type="text" class="form-control mt-2" @keypress.enter="createComment">

          <div class="mt-2">
            <button type="button" class="btn btn-light shadow-none btn-rounded" @click="showReplies = !showReplies">
              <span v-if="showReplies">{{ $t('Hide x replies', { count: comment.replies.length }) }}</span>
              <span v-else>{{ $t('View x replies', { count: comment.replies.length }) }}</span>
            </button>
          </div>

          <!-- Replies -->
          <transition name="pop">
            <div v-if="showReplies" class="replies">
              <reply-card-vue v-for="reply in comment.replies" :key="reply.id" :reply="reply" />
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useUtilities } from '@/composables/utils'

import ReplyCardVue from './ReplyCard.vue'

export default {
  name: 'CommentCard',
  components: {
    ReplyCardVue
  },
  props: {
    comment: {
      type: Object,
      required: true
    },
    shadow: {
      type: Boolean,
      default: true
    }
  },
  setup () {
    const { incrementLastId } = useUtilities()
    return {
      incrementLastId
    }
  },
  data: () => ({
    showReplyInput: false,
    showReplies: false
  }),
  methods: {
    async likeComment () {
      // pass
    },
    async createComment () {
      var id = this.incrementLastId(this.comments)
      this.comments.push({ id: id, replies: [] })
    },
    async createReply () {
      // pass
    }
  }
}
</script>


<style scoped>
.opacity-enter-active,
.opacity-leave-active {
  transition: all .3s ease;
}

.opacity-enter-from,
.opacity-leave-to {
  opacity: 0;
}

.opacity-leave-from,
.opacity-enter-to {
  opacity: 1;
}

.pop-enter-active,
.pop-leave-active {
  transition: all .3s ease;
}

.pop-enter-from,
.pop-leave-to {
  opacity: 0;
  transform: scale(.95, .95);
}

.pop-leave-from,
.pop-enter-to {
  opacity: 1;
  transform: scale(1, 1);
}
</style>
