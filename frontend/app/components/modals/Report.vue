<template>
  <volt-dialog id="report-video" v-model:visible="showReportModal" class="w-2xl" modal>
    <volt-accordion v-for="reportType in reportTypes" :key="reportType.title">
      <volt-accordion-panel :value="reportType.title">
        <volt-accordion-header>{{ reportType.title }}</volt-accordion-header>
        <volt-accordion-content>
          <p>
            {{ reportType.reports }}
          </p>
        </volt-accordion-content>
      </volt-accordion-panel>
    </volt-accordion>

    <p class="font-bold mt-5">
      Flag the section you believe to be problematic
    </p>

    <div class="flex justify-start gap-2">
      <volt-input-text type="time" />
      <volt-input-text type="time" />
    </div>

    <div class="p-5 bg-primary-100 rounded-lg mt-5">
      Flagged videos and users are reviewed by YouTube staff 24 hours a day,
      7 days a week to determine whether they violate Community Guidelines.
      Accounts are penalized for Community Guidelines violations, and
      serious or repeated violations can lead to account termination.
      Report channel
    </div>

    <template #footer>
      <volt-button @click="() => showReportModal = false">
        Close
      </volt-button>

      <volt-button>
        Save
      </volt-button>
    </template>
  </volt-dialog>
</template>

<script setup lang="ts">
import { reportTypes } from '~/data'

/**
 * Modal
 */

const { showReportModal } = tryUseVideoDetailModalsStore()
</script>
