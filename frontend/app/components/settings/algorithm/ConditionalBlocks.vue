<template>
  <div class="conditional-blocks">
    <VoltAlert>
      You can set up conditional blocks to filter content based on specific criteria.
      For example, you can create a block that only shows videos related to a specific theme or
      keywords. This allows you to customize your viewing experience and focus on the content that matters most to you.

      {{ conditions }}

      <div class="mt-5">
        <VoltLink to="/">
          <Icon name="i-fa7-solid:arrow-right" />
          Advanced algorithm builder
        </VoltLink>
      </div>
    </VoltAlert>

    <div class="space-y-2">
      <SettingsAlgorithmConditionBlock v-for="(condition, idx) in conditions" :key="condition.id" :index="idx" @delete-block="handleDeleteBlock" />
    </div>

    <div class="flex justify-center mt-3">
      <VoltButton variant="tonal" @click="handleCreateBlock">
        <Icon name="i-fa7-solid:plus" class="me-2" />
        Create
      </VoltButton>
    </div>
  </div>
</template>

<script setup lang="ts">
const algorithmStore = useAlgorithmSettingsStore()
const { conditions } = storeToRefs(algorithmStore)

const { count: currentIndex, inc } = useCounter(0)

/**
 * Creates a new condition block and adds it to the list.
 */
async function handleCreateBlock() {
  inc()
  
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
 * Deletes a condition block from the list.
 */
async function handleDeleteBlock(index: number) {
  conditions.value.splice(index, 1)
}
</script>
