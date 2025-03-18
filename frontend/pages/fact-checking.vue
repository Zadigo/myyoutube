<template>
  <section class="fact-checking">
    <div class="row">
      <div class="col-md-12">
        <div class="card mb-2">
          <div class="card-body">
            <h1 class="h4">
              Fact checking center
            </h1>

            <p class="fw-light">
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Tenetur deleniti at eius beatae tempora, suscipit harum odit inventore cupiditate dolorum error itaque, aspernatur blanditiis voluptatum. Debitis accusantium numquam nostrum iste?
            </p>
          </div>
        </div>
      </div>
      
      <div class="col-md-6">
        <div class="card">
          <!-- <template v-if="hasSources">
            <FactCheckingSavedBlock v-for="block in blocks" :key="block.id" :block="block" />
          </template> -->
          <FactCheckingEditBlock v-for="(block, i) in blocks" :key="i" :block="block" :index="i" @update:blocks="handleSave" />

          <div class="card-body">
            <v-btn variant="tonal" color="secondary" rounded @click="handleAddBlock">
              <font-awesome icon="plus" class="me-2" />
              Add block
            </v-btn>
          </div>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            Video
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts" setup>
import type { SourceDetails } from '~/types';
import { ref } from 'vue';

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

function handleSave (block: SourceDetails) {
  const existingBlock = blocks.value.find(x => x.id === block.id)
  if (!existingBlock) {
    blocks.value.push(block)
  }
}

function handleAddBlock () {
  blocks.value.push({
    id: blocks.value[blocks.value.length - 1].id,
    start_time: '',
    end_time: '',
    explanation: '',
    article_sources: []
  })
}
</script>
