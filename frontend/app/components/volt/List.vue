<template>
  <div :class="theme.list">
    <slot :theme="theme.listItem" name="body">
      <template v-for="item in items" :key="item[itemLabel]">
        <slot :item="item" :theme="theme.listItem" name="item">
          <div :class="theme.listItem">
            <slot>
              {{ item[itemLabel] }}
            </slot>
          </div>
        </slot>
      </template>
    </slot>
  </div>
</template>

<script setup lang="ts" generic="T extends Record<string, unknown>">
const { items = [], itemLabel = 'id' } = defineProps<{ items?: T[], itemLabel?: string }>()

const theme = ref({
  list: [
    `rounded-lg border border-slate-100 
    dark:border-slate-700 bg-white dark:bg-slate-800 p-4 shadow-sm`,
  ],
  listItem: [
    `flex items-center px-2 py-5
    border-b border-slate-100 dark:border-slate-700`,
  ]
})
</script>
