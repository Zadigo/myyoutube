<template>
  <VoltDialog id="report-video" v-model:visible="show" modal class="max-w-3xl">
    <VoltAccordion v-for="reportType in reportTypes" :key="reportType.title">
      <VoltAccordionPanel :value="reportType.title">
        <VoltAccordionHeader>{{ reportType.title }}</VoltAccordionHeader>
        <VoltAccordionContent>
          <p>
            {{ reportType.reports }}
          </p>
        </VoltAccordionContent>
      </VoltAccordionPanel>
    </VoltAccordion>

    <p class="font-bold mt-5">
      Flag the section you believe to be problematic
    </p>

    <div class="flex justify-between gap-2">
      <VoltInputText type="time" />
      <VoltInputText type="time" />
    </div>

    <div class="p-5 bg-primary-100 rounded-lg mt-5">
      Flagged videos and users are reviewed by YouTube staff 24 hours a day,
      7 days a week to determine whether they violate Community Guidelines.
      Accounts are penalized for Community Guidelines violations, and
      serious or repeated violations can lead to account termination.
      Report channel
    </div>

    <template #footer>
      <VoltButton @click="() => show=false">
        Close
      </VoltButton>

      <VoltButton @click="() => add(selectedPlaylistId, $route.params.id)">
        Save
      </VoltButton>
    </template>
  </VoltDialog>
</template>

<script setup lang="ts">
import { reportTypes } from '~/data'

const emit = defineEmits<{ 'update:modelValue': [value: boolean] }>()
const props = defineProps<{ modelValue: boolean }>()
const show = useVModel(props, 'modelValue', emit, { defaultValue: false })
</script>
