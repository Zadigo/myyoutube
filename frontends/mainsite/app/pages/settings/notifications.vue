<template>
  <section id="notifications">
    <SettingsHeader>
      Choose when and how to be notified
    </SettingsHeader>

    <SettingsCard title="General" subtitle="Manage your mobile and desktop notifications">
      <VoltList :items="notificationOptions">
        <template #item="{ item, theme }">
          <div :class="theme">
            <VoltLabel>
              <template #input>
                <VoltToggleSwitch v-model="item.action" />
              </template>
              <template #label>
                {{ item.label }}
              </template>
            </VoltLabel>
          </div>
        </template>
      </VoltList>
    </SettingsCard>
  </section>
</template>

<script setup lang="ts">
import type { NotificationProfile } from '~/types'

useHead({
  title: 'Notifications'
})

definePageMeta({
  layout: 'settings'
})

const store = useViewerProfile()
const { notificationData } = storeToRefs(store)

const notificationOptions: Record<string, string>[] = [
  {
    "action": "subscribed_channel_activity",
    "label": "Notify me about activity from the channels I'm subscribed to"
  },
  {
    "action": "video_recommendation",
    "label": "Notify me of videos I might like based on what I watch"
  },
  {
    "action": "channel_activity",
    "label": "Notify me about comments and other activity on my channel or videos"
  },
  {
    "action": "replies_activity",
    "label": "Notify me about replies to my comments"
  },
  {
    "action": "mentions",
    "label": "Notify me when others mention my channel"
  },
  {
    "action": "repost",
    "label": "Notify me when others share my content on their channels"
  }
]

const { data } = useFetch('/api/notifications/profile', {
  lazy: true,
  server: false,
  watch: [notificationData],
  default() {
    return {
      subscribed_channel_activity: true,
      video_recommendation: true,
      channel_activity: true,
      replies_activity: true,
      mentions: true,
      repost: true
      }
  },
  transform(data: NotificationProfile) {
    return data
  }
})

if (data.value) {
  notificationData.value = data.value
}
</script>
