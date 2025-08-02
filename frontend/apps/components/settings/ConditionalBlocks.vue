<template>
  <div class="conditional-blocks">
    <p class="alert alert-info">
      Lorem ipsum dolor sit amet consectetur adipisicing elit. 
      Numquam, aut culpa eos labore rerum praesentium voluptatibus nulla architecto 
      autem dignissimos nihil et reprehenderit laborum. Commodi accusantium fugiat qui ex sit.

      <NuxtLink to="/">Learn more</NuxtLink>
    </p>

    <SettingsConditionBlock v-for="(condition, i) in conditions" :key="condition.id" :condition="condition" :index="i" @delete-block="handleDeleteBlock" />

    <div class="d-flex justify-content-center mt-3">
      <v-btn variant="tonal" @click="handleCreateBlock">
        <font-awesome-icon icon="plus" class="me-2" />
        Create
      </v-btn>
    </div>
  </div>
</template>

<script setup lang="ts">
import { z } from 'zod'
import { watchArray } from '@vueuse/core'
import { joinOperators, keywordOperators } from '~/apps/data/constants/operators'

const AlgorithmConditionBlockSchema = z.object({
  id: z.number(),
  theme: z.string(),
  keyword_operator: z.enum(keywordOperators),
  keywords: z.string().array(),
  keywords_subconditions: z.string().array(),
  video_sections: z.string().array(),
  join_operator: z.enum(joinOperators),
  negation: z.boolean().default(false)
})

type AlgorithmConditionBlock = z.infer<typeof AlgorithmConditionBlockSchema>

const currentIndex = ref<number>(1)
const conditions = ref<AlgorithmConditionBlock[]>([])

watchArray(conditions, (newList, oldList) => {
  // Do something
  console.log(newList,  oldList)
})

/**
 * Create a new condition block for
 * filtering the algorithm
 */
async function handleCreateBlock() {
  currentIndex.value += 1
  conditions.value.push({
    id: currentIndex.value,
    theme: '',
    keyword_operator: 'Exact match',
    keywords: [],
    keywords_subconditions: [],
    video_sections: [],
    join_operator: 'And',
    negation: false
  })
}

/**
 * 
 */
async function handleDeleteBlock(index: number) {
  conditions.value.splice(index, 1)
  currentIndex.value -= 1
}
</script>
