<template>
  <section id="settings" class="relative">
    <header>
      <!-- Sidebar -->
      <SidebarsSettings />
    </header>

    <main>
      <div class="max-w-280 mx-auto ps-[calc(var(--sidebar-width)+1rem)] my-10">
        <slot />
      </div>
    </main>
  </section>
</template>

<script setup lang="ts">
onMounted(() => {
  document.body.classList.add('bg-primary-50/20')
})

onUnmounted(() => {
  document.body.classList.remove('bg-primary-50/20')
})
</script>
