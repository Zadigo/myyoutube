<template>
  <v-dialog id="report-video" v-model="show" width="400">
    <v-card>
      <v-card-text>
        <v-expansion-panels>
          <v-expansion-panel v-for="reportType in reportTypes" :key="reportType.title" :title="reportType.title" text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima" />
        </v-expansion-panels>

        <p class="fw-bold mt-5">
          Flag the section you believe to be problematic
        </p>

        <div class="d-flex justify-content-between gap-2">
          <v-text-field type="time" variant="outlined" />
          <v-text-field type="time" variant="outlined" />
        </div>

        <div class="alert alert-info">
          Flagged videos and users are reviewed by YouTube staff 24 hours a day,
          7 days a week to determine whether they violate Community Guidelines.
          Accounts are penalized for Community Guidelines violations, and
          serious or repeated violations can lead to account termination.
          Report channel
        </div>
      </v-card-text>

      <v-card-actions>
        <v-btn @click="show=false">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { reportTypes } from '~/data'

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
