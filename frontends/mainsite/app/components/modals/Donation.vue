<template>
  <volt-dialog v-model:visible="showDonationModal">
    <volt-panel class="bg-surface-100">
      Support the creator by donating an amount between $10 and $500
    </volt-panel>

    <div class="my-5">
      <volt-fluid>
        <volt-input-text type="number" :min="10" :max="500" :step="10" variant="outlined" />
      </volt-fluid>

      <div class="bg-primary-50 rounded-lg p-5 flex-col place-items-center text-center space-y-5 mt-5">
        <p>Enter the confirmation code sent to your email</p>
        <volt-input-otp />
      </div>
    </div>
  </volt-dialog>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showDonationModal } = tryUseVideoDetailModalsStore()
</script>
