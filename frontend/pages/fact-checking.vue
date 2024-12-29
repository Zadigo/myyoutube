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
          <source-block v-for="(block, i) in blocks" :key="i" :block="block" :index="i" @update:blocks="handleSave" />

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

<script lang="ts">
import { SourceDetails } from '@/types/fact_checker';
import { defineComponent, ref } from 'vue';

import SourceBlock from '@/components/fact_checking/SourceBlock.vue';

export default defineComponent({
  name: 'FactCheckingPage',
  components: {
    SourceBlock
  },
  setup () {
    const blocks = ref<SourceDetails[]>([
      {
        id: 1,
        start_time: '',
        end_time: '',
        explanation: '',
        article_sources: []
      }
    ])
    return {
      blocks
    }
  },
  methods: {
    handleSave (block: SourceDetails) {
      const existingBlock = this.blocks.find(x => x.id === block.id)
      if (!existingBlock) {
        this.blocks.push(block)
      }
    },
    handleAddBlock () {
      this.blocks.push({
        id: this.blocks[this.blocks.length - 1].id,
        start_time: '',
        end_time: '',
        explanation: '',
        article_sources: []
      })
    }
  }
})
</script>
