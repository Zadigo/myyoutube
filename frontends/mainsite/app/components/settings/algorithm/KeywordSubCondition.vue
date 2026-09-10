<template>
  <div class="grid grid-cols-3 place-items-start gap-2">
    <u-select v-model="conditionBlockProxy.operator" :options="Array.from(KEYWORD_OPERATORS)" class="w-full" />

    <div class="w-full">
      <u-input-menu v-model="conditionBlockProxy.keywords" :items="['NBA', 'WNBA']" multiselect />
    </div>

    <u-button>
      <Icon name="i-fa7-solid:trash" />
    </u-button>
  </div>
</template>

<script setup lang="ts">
import type { AlgorithmKeywordSubcondition } from '~/data'
import { KEYWORD_OPERATORS } from '~/constants/operators'

const props = defineProps<{ subCondition: AlgorithmKeywordSubcondition }>()

const conditionBlockProxy = computed({
  get: () => props.subCondition,
  set: (newValue) => console.log(newValue)
})
</script>
