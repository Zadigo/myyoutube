<template>
  <section id="fact-checking" class="container mx-auto px-4">
    <VoltCard class="shadow-sm">
      <template #content>
        <h1 class="font-bold text-2xl mb-4">
          Fact checking center
        </h1>

        <p class="font-light">
          Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur deleniti at eius beatae tempora, 
          suscipit harum odit inventore cupiditate dolorum error itaque, aspernatur blanditiis voluptatum. 
          Debitis accusantium numquam nostrum iste?
        </p>

        <VoltButton variant="text">
          <Icon name="i-fa7-solid:arrow-up-right-from-square" class="me-2" />
          Learn more
        </VoltButton>
      </template>
    </VoltCard>

    <div class="grid grid-cols-12 gap-2 mt-10">
      <div class="col-span-6">
        <VoltCard class="shadow-sm">
          <template #content>
            <div class="space-y-3"> 
              <FactCheckingEditBlock v-for="(block, i) in blocks" :key="i" :block="block" :index="i" @update:blocks="handleSave" />
            </div>

            <VoltDivider class="my-5" />

            <div class="space-x-2">
              <VoltButton rounded @click="handleAddBlock">
                <Icon name="i-fa7-solid:plus" class="me-2" />
                Add block
              </VoltButton>
              
              <VoltButton rounded>
                <Icon name="i-fa7-solid:check" class="me-2" />
                Submit
              </VoltButton>
            </div>
          </template>
        </VoltCard>
      </div>

      <div class="col-span-6">
        <VoltCard class="shadow-sm">
          <template #content>
            <VideoPlayerBase video-source="/video_fixture_1.mp4" @update:metadata="handleMetadata" />
          </template>
        </VoltCard>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { SourceDetails, VideoTechnicalDetails } from '~/types'

const blocks = ref<SourceDetails[]>([
  {
    id: 1,
    start_time: '',
    end_time: '',
    explanation: '',
    article_sources: []
  }
])

const hasSources = computed(() => {
  return blocks.value.map(x => x.article_sources.length > 0).every(x => x === true)
})

/**
 * Handles the save action for a block
 * @param {SourceDetails} block - The block to save
 */
function handleSave (block: SourceDetails) {
  const existingBlock = blocks.value.find(x => x.id === block.id)
  if (!existingBlock) {
    blocks.value.push(block)
  }
}

/**
 * Handles the addition of a new block
 */
function handleAddBlock () {
  blocks.value.push({
    id: blocks.value[blocks.value.length - 1].id,
    start_time: '',
    end_time: '',
    explanation: '',
    article_sources: []
  })
}

// Metadata

const videoMetadata = ref<VideoTechnicalDetails | null>(null)

function handleMetadata(data: VideoTechnicalDetails) {
  videoMetadata.value = data
}

provide('videoMetadata', videoMetadata)
</script>
