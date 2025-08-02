<template>
  <v-dialog v-model="show" width="300" @close="show=false">
    <v-card>
      <v-card-text>
        Share
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
const emit = defineEmits({
  'update:modelValue' (_value: boolean) {
    return true
  }
})

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const show = computed({
  get: () => props.modelValue,
  set: (value) => {
    emit('update:modelValue', value)
  }
})
</script>
