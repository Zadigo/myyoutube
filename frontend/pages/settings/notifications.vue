<template>
  <section id="notifications">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card">
          <div class="card-body">
            <h2>Choose when and how to be notified</h2>
          </div>
        </div>

        <SettingsCard title="General" subtitle="Manage your mobile and desktop notifications">
          <template #default>
            <div v-if="notificationData" class="list-group">
              <div v-for="notificationOption in notificationOptions" :key="notificationOption.action" class="list-group-item">
                <v-switch v-model="notificationData[notificationOption.action]" :label="notificationOption.label" inset />
              </div>
            </div>
          </template>
        </SettingsCard>
      </div>
    </div>
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

// console.log('this is working', data.value)

if (data.value) {
  notificationData.value = data.value
}

// async function getData() {
//   const client = createDjangoClient('/api/v1/notifications')
//   const response = await client.get('/profile')
//   notificationData.value = response.data
// }

// getData()
</script>
