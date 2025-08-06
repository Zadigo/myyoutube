<template>
  <BlockBase @delete-block="handleDeleteBlock(index)">
    <div class="row">
      <div class="col-12">
        <v-text-field v-model="regexOptions.regex" variant="solo-filled" placeholder="Regex: ^Taylor|Swift" flat hide-details @keypress="emit('define-options', regexOptions)" />

        <v-chip-group v-model="regexOptions.source">
          <v-chip v-for="targetOption in targetOptions" :key="targetOption">
            {{ targetOption }}
          </v-chip>
        </v-chip-group>
      </div>

      <div class="col-12">
        <v-switch v-model="regexOptions.invert" label="Invert" inset />
        <v-switch v-model="regexOptions.case_sensitive" label="Case sensitive" inset />
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

const { handleDeleteBlock } = useBlocks()

const targetOptions = [
  'Video description',
  'Video transcript',
  'Video title'
]

defineProps({
  index: {
    type: Number,
    required: true
  }
})

const emit = defineEmits({
  'define-options' (_data: RegexOptions) {
    return true
  }
})

const regexOptions = ref<RegexOptions>({
  regex: '',
  source: 'Video title',
  invert: false,
  case_sensitive: false
})
</script>
