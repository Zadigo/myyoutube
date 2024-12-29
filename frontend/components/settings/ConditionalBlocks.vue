<template>
  <div class="conditional-blocks">
    <p class="alert alert-info">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. 
      Numquam, aut culpa eos labore rerum praesentium voluptatibus nulla architecto 
      autem dignissimos nihil et reprehenderit laborum. Commodi accusantium fugiat qui ex sit.
      <a href="#" @click.prevent>Learn more</a>
    </p>

    <ConditionBlock v-for="(condition, i) in conditions" :key="condition.id" :condition="condition" :index="i" @delete-block="handleDeleteBlock" />

    <div class="d-flex justify-content-center mt-3">
      <v-btn variant="tonal" @click="handleCreateBlock">
        <font-awesome-icon icon="plus" class="me-2" />
        Create
      </v-btn>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { AlgorithmConditionBlock } from '@/types/user_settings'

import ConditionBlock from './ConditionBlock.vue';

export default defineComponent({
  name: 'ConditionalBlocks',
  components: {
    ConditionBlock
  },
  setup() {
    const conditions = ref<AlgorithmConditionBlock[]>([])
    return {
      conditions
    }
  },
  methods: {
    /**
     * 
     */
    async handleCreateBlock () {
      this.conditions.push({
        id: 1,
        theme: '',
        keyword_operator: 'Exact match',
        keywords: [],
        keywords_subconditions: [],
        video_sections: [],
        join_operator: 'And',
        negation: false
      })
    },
    /**
     * 
     */
    async handleDeleteBlock (index: number) {
      this.conditions.splice(index, 1)
    }
  }
})
</script>
