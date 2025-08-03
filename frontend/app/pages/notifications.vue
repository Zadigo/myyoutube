<template>
  <section id="notifications" class="w-4xl mx-auto">
    <div class="py-5 flex justify-end rounded-lg mb-10">
      <VoltSelectButton v-model="notificationType" :options="['All', 'Messages', 'Uploads']" />
    </div>

    <div class="space-y-2">
      <VoltCard v-for="notification in notifications" :key="notification" class="shadow-sm">
        <template #content>
          <article>
            {{ notification }}
          </article>
        </template>
      </VoltCard>

      <div ref="moreButtonEl" class="py-5">
        <VoltButton @click="() => {}">
          Load More
        </VoltButton>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const notificationType = ref<'All' | 'Messages' | 'Uploads'>('All')

const notifications = ref<string[]>([])

onMounted(() => {
  notifications.value = Array.from({ length: 100 }, (_, i) => `Notification ${i + 1}`)
  document.body.classList.add('bg-primary-600/30')
})

onUnmounted(() => {
  document.body.classList.remove('bg-primary-600/30')
})

const moreButtonEl = useTemplateRef<HTMLElement>('moreButtonEl')

useIntersectionObserver(moreButtonEl, (isIntersecting) => {
  if (isIntersecting) {
    notifications.value.push(...Array.from({ length: 20 }, (_, i) => `Notification ${i + 1}`))
  }
})
</script>
