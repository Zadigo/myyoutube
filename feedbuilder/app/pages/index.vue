<template>
  <section class="middle">
    <div class="">      
      <h1 class="font-bold text-2xl">
        Feed builder
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

const ResolvedBlockSource = resolveComponent('BlockSource')
const ResolvedBlockLimit = resolveComponent('BlockLimit')
const ResolvedBlockRegex = resolveComponent('BlockRegex')
const ResolvedBlockSort = resolveComponent('BlockSort')

// const videoStore = useVideoStore()
// const {  } = storeToRefs(videoStore)

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
</script>
