<template>
  <article :aria-label="`Comment n°${comment.id}`" class="card shadow-none">
    <div class="card-body">
      <div class="d-flex align-items-start gap-4">
        <NuxtLink :to="{ name: 'channel_details', params: { id: comment.user_channel } }" aria-label="">
          <v-img src="/avatar2.png" width="80" height="80" class="img-fluid rounded-circle" alt="" />
        </NuxtLink>

        <div class="content">
          <div class="mb-3">
            <v-btn :to="{ name: 'channel_details', params: { id: comment.user_channel } }" color="secondary" variant="plain">
              {{ comment.user.get_full_name }}
            </v-btn>

            <v-btn class="mx-2" disabled>
              3 weeks
            </v-btn>

            <v-btn disabled>
              Something
            </v-btn>
          </div>

          <p>{{ comment.content }}</p>

          <div class="my-3">
            <div class="badge badge-danger me-1">
              @creator
            </div>

            <div class="badge badge-light">
              Aimé par le creator
            </div>
          </div>

          <div class="d-flex gap-2 mt-4">
            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome v-if="comment?.is_liked" icon="fas fa-thumbs-up" class="me-2" />
              <font-awesome v-else icon="far fa-thumbs-up" class="me-2" />
              12.3k
            </v-btn>
            
            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome v-if="!comment?.is_disliked" icon="fas fa-thumbs-down" class="me-2" />
              <font-awesome v-else icon="far fa-thumbs-up" class="me-2" />
              24
            </v-btn>

            <v-btn color="primary" size="small" rounded="xl" flat>
              <font-awesome icon="fas fa-comment" class="me-2" />
              Answer
            </v-btn>
          </div>

          <v-btn v-if="hasReplies" rounded="xl" color="secondary" variant="text" class="mt-3" @click="showReplies = !showReplies">
            Voir {{ comment.number_of_replies }} commentaires
          </v-btn>

          <!-- Replies -->
          <transition id="replies" tag="div" name="pop" mode="in-out">
            <div v-if="showReplies" class="replies">
              <user-reply v-for="i in 3" :key="i" :reply="{}" />
            </div>
          </transition>
        </div>
      </div>
    </div>
  </article>
</template>

<script setup>
import { ref } from 'vue';

import type { PropType } from 'vue';
import type { VideoComment } from '~/types';

defineProps({
  comment: {
    type: Object as PropType<VideoComment>,
    default: () => {},
    required: false
  }
})

const showReplies = ref(false)

const hasReplies = computed(() => {
  return this.comment.number_of_replies >= 1
})
</script>
