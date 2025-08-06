import { defineStore } from 'pinia'

import type { BlockNames } from '~/data'
import type { FeedBlocks, NewFeed } from '~/types'
import type { WebsocketMessage } from '~/types/websocket'

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

  const isDisabled = computed(() => typeof currentFeed.value === 'undefined')
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
    const newBlock: FeedBlocks = {
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
    if (blockName === 'Sort') {
      newBlock.data = {
        by: 'Creation date',
        direction: 'Ascending'
      }
    }

    if (blockName === 'Limit') {
      newBlock.data = {
        limit: 100 // Default limit
      }
    }

    if (currentFeed.value) {
      currentFeed.value.blocks.push(newBlock)
    }
  }

  // watch(currentFeed, (newFeed) => {
  //   if (newFeed) {
  //     // Ensure the current feed is always set to the first feed if no feed is selected
  //     if (!feeds.includes(newFeed)) {
  //       currentFeed.value = feeds[0]
  //     }
  //   }
  // })

  return {
    isDisabled,
    feeds,
    currentFeed,
    currentFeedBlocks,
    setCurrentFeed,
    deleteBlock,
    addBlock
  }
})
