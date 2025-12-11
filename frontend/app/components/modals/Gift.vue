<template>
  <volt-dialog id="gifts" v-model:visible="showGiftsModal" :dismissable-mask="false" modal>
    <volt-alert class="mb-4" variant="warning">
      You have purchased no gifts yet. You can buy gifts here before pursuing.
    </volt-alert>

    <volt-button class="my-2">
      Purchase
    </volt-button>

    <div class="grid grid-cols-3 gap-2">
      <article v-for="i in 10" id="donation" :key="i" class="font-light">
        <volt-card class="shadow-none border border-slate-50 text-center">
          <template #content>
            Gift 1
          </template>
        </volt-card>
      </article>
    </div>
  </volt-dialog>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showGiftsModal } = tryUseVideoDetailModalsStore()
</script>
