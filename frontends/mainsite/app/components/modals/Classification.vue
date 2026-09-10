<template>
  <u-slideover id="classification-modal" v-model:open="showClassificationDrawer" position="right">
    <template #header>
      <h2 class="font-bold text-2xl">
        Classification
      </h2>
    </template>

    <template #body>
      <volt-panel class="my-5">
        Use this tool to signal that this video was not properly
        categorized by the creator and therefore does not correspond to
        the result you were expecting
      </volt-panel>
  
      <div class="space-y-2">
        <u-switch label="Mark as wrong category" />
        <u-switch label="Block this channel" />
      </div>  
    </template>

    <template #footer>
      <div class="space-x-2">
        <u-button variant="outline">
          <Icon name="i-fa7-solid:check" />
          Save
        </u-button>
      </div>
    </template>
  </u-slideover>
</template>

<script setup lang="ts">
/**
 * Modal
 */

const { showClassificationDrawer } = tryUseVideoDetailModalsStore()
</script>
