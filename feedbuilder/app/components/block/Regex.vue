<template>
  <BlockBase @delete-block="feedsStore.deleteBlock(index)">
    <div class="row">
      <div class="col-12">
        <VoltInputText v-model="regexOptions.regex" variant="solo-filled" placeholder="Regex: ^Taylor|Swift" flat hide-details @keypress="emit('define-options', regexOptions)" />

        <VoltBadge v-for="targetOption in targetOptions" :key="targetOption">
          {{ targetOption }}
        </VoltBadge>
      </div>

      <div class="col-12">
        <VoltToggleSwitch v-model="regexOptions.invert" label="Invert" inset />
        <VoltToggleSwitch v-model="regexOptions.case_sensitive" label="Case sensitive" inset />
      </div>
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
