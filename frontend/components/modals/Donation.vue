<template>
  <v-dialog v-model="show" width="500" @close="show=false">
    <v-card>
      <v-card-text>
        <v-form>
          <v-text-field type="number" :min="10" :max="500" :step="10" variant="outlined" />
        </v-form>
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
