<template>
  <aside class="mt-3 bg-slate-100 rounded-lg h-[800px] overflow-y-scroll p-3">
    <NuxtLink :to="`/channels/ch_noienozinfoz`">
      <VoltCard v-for="i in 120" :key="i" class="mt-1">
        <template #content>
          Something
        </template>
      </VoltCard>
    </NuxtLink>
  </aside>
</template>

<script setup></script>
