<template>
  <div class="grid grid-cols-3 place-items-start gap-2">
    <VoltSelect v-model="conditionBlockProxy.operator" :options="Array.from(keywordOperators)" class="w-full" />

    <div class="w-full">
      <VoltAutoComplete v-model="conditionBlockProxy.keywords" :items="['NBA', 'WNBA']" />
    </div>

    <VoltButton>
      <Icon name="i-fa7-solid:trash" />
    </VoltButton>
  </div>
</template>

<script setup lang="ts">
import type { AlgorithmKeywordSubcondition } from '~/data'
import { keywordOperators } from '~/data/constants'

const props = defineProps<{ subCondition: AlgorithmKeywordSubcondition }>()

const conditionBlockProxy = computed({
  get: () => props.subCondition,
  set: (newValue) => console.log(newValue)
})
</script>
