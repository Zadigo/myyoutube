<template>
  <u-modal v-model:open="showDonationModal">
    <template #body>
      <base-panel class="bg-surface-100">
        Support the creator by donating an amount between $10 and $500
      </base-panel>
  
      <div class="my-5">
        <u-input type="number" :min="10" :max="500" :step="10" />
  
        <div class="bg-primary-50 rounded-lg p-5 flex-col place-items-center text-center space-y-5 mt-5">
          <p>Enter the confirmation code sent to your email</p>
          <volt-input-otp />
        </div>
      </div>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showDonationModal } = useVideoDetailModalsStore()
</script>
