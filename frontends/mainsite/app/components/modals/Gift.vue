<template>
  <u-modal id="gifts" v-model:open="showGiftsModal" :dismissable-mask="false" modal>
    <template #body>
      <volt-panel class="mb-4">
        You have purchased no gifts yet. You can buy gifts here before pursuing.
      </volt-panel>
  
      <u-button class="my-2">
        Purchase
      </u-button>
  
      <div class="grid grid-cols-3 gap-2">
        <article v-for="i in 10" id="donation" :key="i" class="font-light">
          <u-card class="shadow-none border border-slate-50 text-center">
            Gift 1
          </u-card>
        </article>
      </div>
    </template>
  </u-modal>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showGiftsModal } = tryUseVideoDetailModalsStore()
</script>
