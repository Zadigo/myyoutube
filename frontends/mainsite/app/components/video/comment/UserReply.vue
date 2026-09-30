<template>
  <article ref="replyCardEl" class="my-1 shadow-none bg-primary-50 rounded-lg max-w-5xl ms-auto">
    <u-card>
      <div class="flex justify-around">
        <div class="me-3">
          <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
            <u-avatar src="/avatars/avatar3.png" size="xl" alt="Image 3" />
          </nuxt-link>
        </div>

        <div class="ms-1">
          <div class="flex justify-start">
            <nuxt-link :to="`/channels/ch_noienozinfoz`" aria-label="">
              <span class="fw-bold me-2">Cee Dee</span>
              <span class="text-primary-400">3 weeks ago</span>
            </nuxt-link>
          </div>

          <p class="card-text">
            Gotta give Kendra points for not totally losing her professional
            "cool" when she realized she'd been called out on live TV.
          </p>

          <div class="my-3 flex gap-2">
            <lazy-video-comment-badges-from-creator hydrate-on-idle />
            <lazy-video-comment-badges-liked-by-creator hydrate-on-idle />
          </div>

          <div class="flex items-center gap-2">
            <u-button icon="i-lucide-thumbs-up" variant="subtle" size="sm">
              12.3k
            </u-button>
              
            <u-button icon="i-lucide-thumbs-down" variant="subtle" size="sm">
              26
            </u-button>
              
            <u-button icon="i-lucide-reply" variant="subtle" size="sm" @click="() => { toggleReplyTextarea() }">
              Repondre
            </u-button>
          </div>

          <!-- Reply textarea -->
          <div v-if="showReplyTextarea">
            <u-textarea :style="{ resize: 'none' }" class="w-full mt-5" placeholder="Write a reply..." />
          </div>
        </div>
      </div>
    </u-card>
  </article>
</template>

<script lang="ts" setup>
defineProps<{ reply: VideoReplyNode }>()

const [showReplyTextarea, toggleReplyTextarea] = useToggle()

/**
 * Click outside
 */

const replyCardEl = useTemplateRef('replyCardEl')
onClickOutside(replyCardEl, () => {
  toggleReplyTextarea(false)
})
</script>
