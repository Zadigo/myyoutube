<template>
  <u-card>
    <div class="p-5 flex items-center justify-between">
      <div class="flex items-center">
        <u-avatar />
        <p :class="theme.title">Julie Pauline</p>
      </div>

      <div>
        <u-button variant="soft" icon="i-lucide-plus" />
        <u-button variant="soft" icon="i-lucide-plus" />
      </div>
    </div>

    <slot :class="theme.content" />

    <div :class="[theme.footer, 'flex items-center justify-between']">
      <div>
        <u-button variant="soft" icon="i-lucide-plus" />
        <u-button variant="soft" icon="i-lucide-plus" />
      </div>

      <p class="font-light">
        Updated 2 hours ago
      </p>
    </div>
  </u-card>
</template>

<script setup lang="ts">
const theme = {
  header: `flex justify-between items-center p-[1.125rem] p-toggleable:py-[0.375rem] p-toggleable:px-[1.125rem]`,
  title: `leading-none font-semibold`,
  headerActions: `flex items-center gap-1`,
  contentContainer: ``,
  content: `pt-0 pb-[1.125rem] px-[1.125rem]`,
  footer: `pt-0 pb-[1.125rem] px-[1.125rem]`,
  transition: {
    enterFromClass: 'max-h-0',
    enterActiveClass: 'overflow-hidden transition-[max-height] duration-1000 ease-[cubic-bezier(0.42,0,0.58,1)]',
    enterToClass: 'max-h-[1000px]',
    leaveFromClass: 'max-h-[1000px]',
    leaveActiveClass: 'overflow-hidden transition-[max-height] duration-[450ms] ease-[cubic-bezier(0,1,0,1)]',
    leaveToClass: 'max-h-0'
  }
}
</script>
