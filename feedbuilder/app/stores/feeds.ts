import { defineStore } from 'pinia'
import type { BlockNames } from '~/data'
import type { NewFeed } from '~/types'

export const useFeedsStore = defineStore('feeds', () => {
  const feeds = reactive<NewFeed[]>([
    {
      name: 'First Feed',
      blocks: [
        {
          position: 0,
          component: 'Source',
          data: {
            source: 'Entire network',
            duration: '12 hours'
          }
        }
      ]
    }
  ])
  const currentFeed = ref<NewFeed>()

  const currentFeedBlocks = computed(() => currentFeed.value?.blocks || [])

  function setCurrentFeed(feed: NewFeed) {
    currentFeed.value = feed
  }

  function deleteBlock(index: number) {
    if (currentFeed.value) {
      currentFeed.value.blocks.splice(index, 1)

      // Reorder blocks after deletion
      currentFeed.value.blocks.forEach((block, idx) => {  
        block.position = idx
      })
    }
  }

  function addBlock(blockName: BlockNames) {
    const newBlock = {
      position: currentFeedBlocks.value.length,
      component: blockName,
      data: null
    }

    if (blockName === 'Source') {
      newBlock.data = {
        source: 'Entire network',
        duration: '12 hours'
      }
    }

    if (currentFeed.value) {
      currentFeed.value.blocks.push(newBlock)
    }
  }

  return {
    feeds,
    currentFeed,
    currentFeedBlocks,
    setCurrentFeed,
    deleteBlock,
    addBlock
  }
})
