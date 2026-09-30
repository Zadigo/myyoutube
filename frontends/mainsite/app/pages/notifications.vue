<template>
  <section id="notifications" class="mx-auto">
    <div class="py-5 flex justify-end rounded-lg mb-10">
      <u-button v-for="item in Array.from(NOTIFICATION_TYPES)" :key="item">
        {{ item }}
      </u-button>
    </div>

    <div class="space-y-2">
      <u-card v-for="notification in notifications" :key="notification.id" class="shadow-sm">
        <article>
          {{ notification }}
        </article>
      </u-card>

      <div ref="moreButtonEl" class="py-5">
        <u-button @click="() => { void refresh() }">
          Load More
        </u-button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const notificationType = ref<NotificationType>('All')

const { data: notifications, refresh } = await useAsyncData<NotificationApiResponse>(
  `notifications-${notificationType.value}`, 
  async () => await $fetch('/api/notifications/', {
    method: 'GET',
    query: {
      type: notificationType.value
    }
  }), {
    watch: [notificationType],
    default: () => ({} as NotificationApiResponse)
  }
)

/**
 * Infinite Scroll
 */

const moreButtonEl = useTemplateRef<HTMLElement>('moreButtonEl')

useIntersectionObserver(moreButtonEl, async (isIntersecting) => {
  if (isIntersecting) {
    void refresh()
  }
})

/**
 * Background
 */

onMounted(async () => {
  document.body.classList.add('bg-primary-600/30')
})

onUnmounted(() => {
  document.body.classList.remove('bg-primary-600/30')
})
</script>
