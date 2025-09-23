<template>
  <volt-card class="shadow-none">
    <template #content>
      <div class="flex-col items-start gap-4">
        <div class=" flex items-center gap-2 mb-3">
          <nuxt-link :to="`/channels/${comment.user_channel}`" aria-label="">
            <volt-avatar image="/avatars/avatar2.png" :alt="comment.user_channel" shape="circle" size="small" />
          </nuxt-link>

          <volt-button :to="`/channels/${comment.user_channel}`" size="small" variant="outlined">
            {{ comment.user_channel }}
          </volt-button>

          <volt-button size="small" variant="outlined" disabled>
            3 weeks ago
          </volt-button>
        </div>

        <p class="pt-2 pb-5">{{ comment.content }}</p>

        <div class="my-3 space-x-2">
          <volt-badge severity="contrast">
            @creator
          </volt-badge>

          <volt-badge severity="info">
            Aimé par le createur
          </volt-badge>

          <volt-badge severity="contrast">
            First comment
          </volt-badge>

          <volt-badge severity="contrast">
            <icon name="i-lucide-dollar-sign" />
            Donor
          </volt-badge>
        </div>

        <div class="flex gap-2 mt-4">
          <volt-button variant="outlined" size="small" rounded>
            <icon v-if="comment?.is_liked" name="i-fa7-solid:thumbs-up" />
            <icon v-else name="i-fa7-regular:thumbs-up" />
            12.3k
          </volt-button>
          
          <volt-button variant="outlined" size="small" rounded>
            <icon v-if="!comment?.is_disliked" name="i-fa7-solid:thumbs-down" />
            <icon v-else name="i-fa7-regular:thumbs-up" />
            24
          </volt-button>

          <volt-button variant="outlined" size="small" rounded>
            <icon name="i-lucide-message-circle-more" />
            Answer
          </volt-button>
        </div>

        <volt-button v-if="hasReplies" variant="text" class="mt-3" rounded @click="() => { toggleReplies() }">
          Voir {{ comment.number_of_replies }} commentaires
        </volt-button>

        <!-- Replies -->
        <transition id="replies" tag="div" name="pop" mode="in-out">
          <div v-if="showReplies" class="replies">
            <video-user-reply v-for="i in 3" :key="i" :reply="{}" />
          </div>
        </transition>
      </div>

      <volt-divider class=" mt-2 mb-5" />
    </template>
  </volt-card>
</template>

<script lang="ts" setup>
import type { VideoComment } from '~/types'

const props = defineProps<{ comment: VideoComment }>()

const [showReplies, toggleReplies] = useToggle(false)

const hasReplies = computed(() => props.comment.number_of_replies >= 1)
const isPinned = computed(() => props.comment.pinned)
</script>
