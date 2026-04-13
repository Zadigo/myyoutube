<template>
  <block-base title="Regex" @delete-block="feedsStore.deleteBlock(index)">
    <nuxt-input v-model="data.pattern" class="w-full" placeholder="Regex: ^Taylor|Swift" />

    <div class="gap-2 my-2 flex flex-wrap">
      <nuxt-button v-for="option in Array.from(targetOptions)" :key="option" :variant="data.source === option ? 'solid' : 'outline'" size="sm" @click="() => { data.source = option }">
        <icon name="lucide:text" />
        {{ option }}
      </nuxt-button>
    </div>
    
    <div class="space-y-2">
      <nuxt-switch v-model="data.invert" label="Invert the match" />
      <nuxt-switch v-model="data.case_sensitive" label="Case sensitive" />
    </div>
  </block-base>
</template>

<script setup lang="ts">
import type { RegexOptions } from '~/types'

const feedsStore = useFeedsStore()

const emit = defineEmits<{ 'update:modelValue': [value: RegexOptions] }>()
const props = defineProps<{ modelValue: RegexOptions, index: number }>()

const data = useVModel(props, 'modelValue', emit, {
  passive: true,
  eventName: 'update:modelValue'
})
</script>
