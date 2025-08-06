<template>
  <BlockBase @delete-block="feedsStore.deleteBlock(index)">
    <VoltInputText v-model="regexOptions.regex" class="w-full" placeholder="Regex: ^Taylor|Swift" />

    <div class="gap-2 my-2 flex flex-wrap">
      <VoltBadge v-for="targetOption in targetOptions" :key="targetOption">
        {{ targetOption }}
      </VoltBadge>
    </div>
    
    <div class="space-y-2">
      <VoltLabel>
        <VoltToggleSwitch v-model="regexOptions.invert" />
        <label>Invert the match</label>
      </VoltLabel>

      <VoltLabel>
        <VoltToggleSwitch v-model="regexOptions.case_sensitive" />
        <label>Case sensitive</label>
      </VoltLabel>
    </div>
  </BlockBase>
</template>

<script setup lang="ts">
interface RegexOptions {
  regex: string
  source: 'Video description' | 'Video transcript' | 'Video title'
  invert: boolean
  case_sensitive: boolean
}

const feedsStore = useFeedsStore()

const targetOptions = [
  'Video description',
  'Video transcript',
  'Video title'
]

defineProps<{ index: number }>()
const emit = defineEmits<{ 'define-options': [regexOptions: RegexOptions] }>()

const regexOptions = ref<RegexOptions>({
  regex: '',
  source: 'Video title',
  invert: false,
  case_sensitive: false
})
</script>
