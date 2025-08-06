<template>
  <section class="middle">
    <div class="">      
      <h1 class="font-bold text-2xl">
        Feed builder

        <VoltButton @click="open()">
          Connect
        </VoltButton>
      </h1>
      
      <div class="mt-5">
        <div v-if="currentFeed" class="flex gap-2">
          <VoltInputText v-model="currentFeed.name" placeholder="Feed name" class="flex-grow" />
          <VoltButton>Run</VoltButton>
        </div>

        <div class="flex flex-wrap gap-1 mt-5">
          {{ isDisabled }}
          <VoltButton v-for="block in blockNames" :key="block" :disabled="isDisabled" size="small" @click="feedsStore.addBlock(block)">
            <Icon name="i-fa7-solid:plus" />
            {{ block }}
          </VoltButton>
        </div>

        <div>
          <div v-for="(block, i) in currentFeedBlocks" :key="i" class="my-3">
            <component v-model="block.data" :is="componentMapping[block.component]" :index="i" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { blockNames, type BlockNames } from '~/data'
import type { MessageReceivedFeedVideos, MessageSetCurrentFeed, WebsocketMessage } from '~/types/websocket'

const ResolvedBlockSource = resolveComponent('BlockSource')
const ResolvedBlockLimit = resolveComponent('BlockLimit')
const ResolvedBlockRegex = resolveComponent('BlockRegex')
const ResolvedBlockSort = resolveComponent('BlockSort')

const videoStore = useVideoStore()
const { items } = storeToRefs(videoStore)

const feedsStore = useFeedsStore()
const { currentFeed, currentFeedBlocks, isDisabled } = storeToRefs(feedsStore)

const componentMapping: { [K in BlockNames]: ReturnType<typeof resolveComponent> } = {
  'Source': ResolvedBlockSource,
  'RegExp': ResolvedBlockRegex,
  'Sort': ResolvedBlockSort,
  'Limit': ResolvedBlockLimit,
  'Remove': '',
  'Replace': ''
}

const { send, decode } = useWebsocketMessages()

const { open, ws } = useWebSocket<WebsocketMessage>(`${useRuntimeConfig().public.prodDomain}/ws/feed-builder`, {
  immediate: false,
  onConnected(connection) {
    // TODO: Set current feed from the parent
    send<MessageSetCurrentFeed>({ action: 'set_current_feed', feed: currentFeed.value }, connection)
  },
  onError() {

  },
  onMessage(_, event) {
    const data = decode<MessageReceivedFeedVideos>(event.data as string)
    
    if (data.value.action === 'feed_videos') {
      items.value = data.value.videos
    }
  }
})

onMounted(async () => {
  open()
})

watchDebounced(currentFeed, (newFeed) => {
  send<MessageSetCurrentFeed>({ action: 'update_feed_videos', feed: newFeed }, ws.value)
}, {
  debounce: 3000,
  deep: true
})
</script>
