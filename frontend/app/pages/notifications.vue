<template>
  <section id="notifications" class="mx-auto">
    <div class="py-5 flex justify-end rounded-lg mb-10">
      <VoltSelectButton v-model="notificationType" :options="['All', 'Messages', 'Uploads']" />
    </div>

    <div class="space-y-2">
      <VoltCard v-for="notification in notifications" :key="notification.id" class="shadow-sm">
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
import type { Notification, NotificationApiResponse } from '~/types'

const notificationType = ref<'All' | 'Messages' | 'Uploads'>('All')

const apiResponse = ref<NotificationApiResponse | null>(null)
const notifications = ref<Notification[]>([])

const { $notificationsClient } = useNuxtApp()

onMounted(async () => {
  const data = await $notificationsClient<NotificationApiResponse>('/', {
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
    const data = await $notificationsClient<NotificationApiResponse>('/', {
      method: 'GET',
      query: {
        offset: apiResponse.value?.next
      }
    })

    apiResponse.value = data
    notifications.value = data.results
  }
})
</script>
