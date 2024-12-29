<template>
  <aside class="mt-3">
    <NuxtLink :to="{ name: 'video_details', params: { id: 'vd_eneoifz' } }">
      <div v-for="i in 10" :key="i" class="card mt-1">
        <div class="card-body">
          Something
        </div>
      </div>
    </NuxtLink>
  </aside>
</template>

<script setup></script>
