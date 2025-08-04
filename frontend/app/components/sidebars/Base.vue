<template>
  <div class="mx-3 mt-4 flex-col justify-between">
    <div id="links" class="space-y-5">
      <slot name="links" />
    </div>

    <slot />
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="scss" scoped>
$box_shadow: 0 2px 5px 0 rgb(0 0 0 / 16%), 0 2px 10px 0 rgb(0 0 0 / 12%);

a {
  &.active {
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
  
  &[class*="-exact-active"] {
    z-index: 2;
    color: var(--p-surface-0);
    background-color: var(--p-primary-500);
    border-color: var(--p-primary-500);
    border-radius: 5px;
    box-shadow: $box_shadow;
  }
}
</style>
