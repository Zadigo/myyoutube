<template>
  <volt-card class="shadow-none">
    <template #content>
      <div class="flex-col items-start gap-4">
        <div class=" flex items-center gap-2 mb-3">
          <nuxt-link :to="`/channels/${userChannel.reference}`" aria-label="">
            <volt-avatar image="/avatars/avatar2.png" :alt="userChannel.name" shape="circle" size="small" />
          </nuxt-link>
  
          <u-button :to="`/channels/${userChannel?.reference}`" size="small" variant="outlined">
            {{ userChannel.name }}
          </u-button>
  
          <u-button size="small" variant="outlined" disabled>
            3 weeks ago
          </u-button>
        </div>
  
        <p class="pt-2 pb-5">{{ videoComment.node.content }}</p>
  
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
          <u-button variant="outline" size="sm" rounded>
            <icon v-if="videoComment.node?.isLiked" name="i-fa7-solid:thumbs-up" />
            <icon v-else name="i-fa7-regular:thumbs-up" />
            12.3k
          </u-button>
          
          <u-button variant="outline" size="sm" rounded>
            <icon v-if="!videoComment?.node.isDisliked" name="i-fa7-solid:thumbs-down" />
            <icon v-else name="i-fa7-regular:thumbs-up" />
            24
          </u-button>
  
          <u-button variant="outline" size="sm" rounded>
            <icon name="i-lucide-message-circle-more" />
            Answer
          </u-button>
        </div>
  
        <u-button v-if="hasReplies" variant="ghost" class="mt-3" rounded @click="() => { toggleReplies() }">
          Voir {{ videoComment.node.numberOfReplies }} commentaires
        </u-button>
  
        <transition id="replies" tag="div" name="pop" mode="in-out">
          <div v-if="showReplies && isDefined(replies)" class="replies">
            <video-user-reply v-for="reply in replies.data.commentreplies.edges" :key="reply.node.id" :reply="reply" />
          </div>
        </transition>
      </div>
    </template>
  </volt-card>
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
