<template>
  <u-card class="shadow-none">
    <div class="flex-col items-start gap-4">
      <div class=" flex items-center gap-2 mb-3">
        <nuxt-link :to="`/channels/${userChannel.reference}`" aria-label="">
          <u-avatar src="/avatars/avatar2.png" :alt="userChannel.name" size="sm" />
        </nuxt-link>

        <u-button :to="`/channels/${userChannel?.reference}`" size="sm" variant="subtle">
          {{ userChannel.name }}
        </u-button>

        <u-button size="sm" variant="outline" disabled>
          3 weeks ago
        </u-button>
      </div>

      <p class="pt-2 pb-5">{{ videoComment.node.content }}</p>

      <div class="my-3 space-x-2 flex items-center">
        <u-badge label="@creator" />
        <u-badge label="Aimé par le createur" />
        <u-badge label="First comment" />
        <u-badge label="Donor" icon="i-lucide-dollar-sign" />
      </div>

      <div class="flex gap-2 mt-4">
        <u-button class="rounded-full" variant="outline" size="sm" :icon="videoComment.node?.isLiked ? 'i-fa7-solid:thumbs-up' : 'i-fa7-regular:thumbs-up'">
          12.3k
        </u-button>
        
        <u-button class="rounded-full" variant="outline" size="sm" :icon="videoComment.node?.isDisliked ? 'i-fa7-solid:thumbs-down' : 'i-fa7-regular:thumbs-down'">
          24
        </u-button>

        <u-button variant="outline" size="sm" class="rounded-full">
          <icon name="i-lucide-message-circle-more" />
          Answer
        </u-button>
      </div>

      <u-button v-if="hasReplies" variant="ghost" class="mt-3 rounded-full" @click="() => { toggleReplies() }">
        Voir {{ videoComment.node.numberOfReplies }} commentaires
      </u-button>

      <transition id="replies" tag="div" name="pop" mode="in-out">
        <div v-if="showReplies && isDefined(replies)" class="replies">
          <video-user-reply v-for="reply in replies.data.commentreplies.edges" :key="reply.node.id" :reply="reply" />
        </div>
      </transition>
    </div>
  </u-card>
</template>

<script lang="ts" setup>
const { videoComment } = defineProps<{ videoComment: VideoCommentNode }>()

/**
 * Show Replies
 */

const [showReplies, toggleReplies] = useToggle(false)

const replies = ref<VideoReplies>()

whenever(showReplies, async (newVal) => {
  if (newVal && !replies.value) {
    replies.value = await $fetch<VideoReplies>(`/api/comments/${videoComment.node.id}`)
  }
})

/**
 * Userchannel
 */

const userChannel = computed(() => videoComment.node.user.userChannelSet.at(0)) 

/**
 * State
 */

const hasReplies = computed(() => videoComment.node.numberOfReplies >= 1)
const isPinned = computed(() => videoComment.node.pinned)
</script>
