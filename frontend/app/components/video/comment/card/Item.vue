<template>
  <VoltCard class="shadow-none">
    <template #content>
      <div class="flex-col items-start gap-4">
        <div class=" flex items-center gap-2 mb-3">
          <NuxtLink :to="`/channels/${comment.user_channel}`" aria-label="">
            <VoltAvatar image="/avatars/avatar2.png" shape="circle" size="small" alt="" />
          </NuxtLink>
         
          <VoltButton :to="`/channels/${comment.user_channel}`">
            {{ comment.user.get_full_name }}
          </VoltButton>

          <VoltButton class="mx-2" disabled>
            3 weeks ago
          </VoltButton>
        </div>

        <p class="pt-2 pb-5">{{ comment.content }}</p>

        <div class="my-3 space-x-2">
          <VoltBadge severity="contrast">
            @creator
          </VoltBadge>

          <VoltBadge severity="contrast">
            Aimé par le creator
          </VoltBadge>
        </div>

        <div class="flex gap-2 mt-4">
          <VoltButton variant="outlined" size="small" rounded>
            <Icon v-if="comment?.is_liked" name="i-fa7-solid:thumbs-up" />
            <Icon v-else name="i-fa7-regular:thumbs-up" />
            12.3k
          </VoltButton>
          
          <VoltButton variant="outlined" size="small" rounded>
            <Icon v-if="!comment?.is_disliked" name="i-fa7-solid:thumbs-down" />
            <Icon v-else name="i-fa7-regular:thumbs-up" />
            24
          </VoltButton>

          <VoltButton variant="outlined" size="small" rounded>
            <Icon name="i-fa7-solid:comment" />
            Answer
          </VoltButton>
        </div>

        <VoltButton v-if="hasReplies" variant="text" class="mt-3" rounded @click="showReplies = !showReplies">
          Voir {{ comment.number_of_replies }} commentaires
        </VoltButton>

        <!-- Replies -->
        <Transition id="replies" tag="div" name="pop" mode="in-out">
          <div v-if="showReplies" class="replies">
            <VideoUserReply v-for="i in 3" :key="i" :reply="{}" />
          </div>
        </Transition>
      </div>

      <VoltDivider class=" mt-2 mb-5" />
    </template>
  </VoltCard>
</template>

<script lang="ts" setup>
import type { VideoComment } from '~/types'

const props = defineProps<{ comment: VideoComment }>()

const showReplies = ref<boolean>(false)

const hasReplies = computed(() => props.comment.number_of_replies >= 1)
const isPinned = computed(() => props.comment.pinned)
</script>
