<template>
  <section id="notifications" class="mx-auto">
    <div class="py-5 flex justify-end rounded-lg mb-10">
      <volt-select-button v-model="notificationType" :options="['All', 'Messages', 'Uploads']" />
    </div>

    <div class="space-y-2">
      <u-card v-for="notification in notifications" :key="notification.id" class="shadow-sm">
        <article>
          {{ notification }}
        </article>
      </u-card>

      <div ref="moreButtonEl" class="py-5">
        <u-button @click="() => {}">
          Load More
        </u-button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const notificationType = ref<'All' | 'Messages' | 'Uploads'>('All')

const apiResponse = ref<NotificationApiResponse | null>(null)
const notifications = ref<Notification[]>([])

const { $notificationsClient } = useNuxtApp()

onMounted(async () => {
  const data = await $fetch<NotificationApiResponse>('/api/notifications/', {
    method: 'GET'
  })

  apiResponse.value = data
  notifications.value = data.results

  document.body.classList.add('bg-primary-600/30')
})

onUnmounted(() => {
  document.body.classList.remove('bg-primary-600/30')
})

/**
 * Infinite Scroll
 */

const moreButtonEl = useTemplateRef<HTMLElement>('moreButtonEl')

useIntersectionObserver(moreButtonEl, async (isIntersecting) => {
  if (isIntersecting) {
    // const data = await $notificationsClient<NotificationApiResponse>('/', {
    //   method: 'GET',
    //   query: {
    //     offset: apiResponse.value?.next
    //   }
    // })

    // apiResponse.value = data
    // notifications.value = data.results

    const data = await $fetch<NotificationApiResponse>('/api/notifications/', { method: 'GET' })
    apiResponse.value = data
    notifications.value = apiResponse.value?.results
  }
})
</script>
