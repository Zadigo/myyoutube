<template>
  <section id="notifications">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card">
          <div class="card-body">
            <h2>Choose when and how to be notified</h2>
          </div>
        </div>

        <settings-card title="General" subtitle="Manage your mobile and desktop notifications">
          <template #default>
            <div class="list-group">
              <div v-for="notificationOption in notificationOptions" :key="notificationOption.action" class="list-group-item">
                <v-switch v-model="requestData[notificationOption.action]" :label="notificationOption.label" inset></v-switch>
              </div>
            </div>
          </template>
        </settings-card>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'
import SettingsCard from '../../components/settings/SettingsCard.vue'
import _ from 'lodash'

const notificationOptions = [
  {
    "action": "channel_activity",
    "label": "Notify me about activity from the channels I'm subscribed to"
  },
  {
    "action": "liked_videos",
    "label": "Notify me of videos I might like based on what I watch"
  },
  {
    "action": "comments_activity",
    "label": "Notify me about comments and other activity on my channel or videos"
  },
  {
    "action": "replies_activity",
    "label": "Notify me about replies to my comments"
  },
  {
    "action": "channel_mentions",
    "label": "Notify me when others mention my channel"
  },
  {
    "action": "share_content",
    "label": "Notify me when others share my content on their channels"
  }
]

export default {
  components: {
    SettingsCard
  },
  setup () {
    const requestData = ref({})
    _.forEach(notificationOptions, (option) => {
      requestData[option.action] = false
    })
    return {
      requestData,
      notificationOptions
    }
  }
}
</script>
