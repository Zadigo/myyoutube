<template>
  <block-base title="Regex" @delete-block="feedsStore.deleteBlock(index)">
    <nuxt-input v-model="regexOptions.regex" class="w-full" placeholder="Regex: ^Taylor|Swift" />

    <div class="gap-2 my-2 flex flex-wrap">
      <nuxt-badge v-for="targetOption in targetOptions" :key="targetOption">
        {{ targetOption }}
      </nuxt-badge>
    </div>
    
    <div class="space-y-2">
      <nuxt-switch v-model="regexOptions.invert" label="Invert the match" />
      <nuxt-switch v-model="regexOptions.case_sensitive" label="Case sensitive" />
    </div>
  </block-base>
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
