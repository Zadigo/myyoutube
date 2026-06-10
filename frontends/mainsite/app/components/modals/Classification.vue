<template>
  <volt-drawer id="classification-modal" v-model:visible="showClassificationDrawer" position="right">
    <template #header>
      <h2 class="font-bold text-2xl">
        Classification
      </h2>
    </template>

    <volt-panel class="my-5">
      Use this tool to signal that this video was not properly
      categorized by the creator and therefore does not correspond to
      the result you were expecting
    </volt-panel>

    <div class="space-y-2">
      <div>
        <volt-label label-for="wrong-category" label="Mark as wrong category">
          <volt-toggle-switch />
        </volt-label>
      </div>

      <div>
        <volt-label label-for="block-channel" label="Block this channel">
          <volt-toggle-switch />
        </volt-label>
      </div>
    </div>

    <volt-divider class="my-5" />

    <div class="space-x-2">
      <volt-button variant="primary">
        <Icon name="i-fa7-solid:check" />
        Save
      </volt-button>
    </div>
  </volt-drawer>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showClassificationDrawer } = tryUseVideoDetailModalsStore()
</script>
