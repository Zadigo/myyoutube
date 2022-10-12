<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <div class="card mb-2">
            <div class="card-body">
              <h2>{{ $t('Choose when and how to be notified') }}</h2>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <h3>{{ $t('General') }}</h3>
              <p class="m-0 text-muted">
                {{ $t('Manage your mobile and desktop notifications') }}
              </p>
            </div>

            <div class="card-body">
              <settings-block-vue :items="general"></settings-block-vue>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import SettingsBlockVue from '@/components/account/SettingsBlock.vue'

export default {
  name: 'NotificationsView',
  components: {
    SettingsBlockVue
  },
  data () {
    return {
      general: [
        {
          name: 'Subscriptions',
          text: "Notify me about activity from the channels I'm subscribed to",
          selected: false
        },
        {
          name: 'Recommended-videos',
          text: "Notify me of videos I might like based on what I watch",
          selected: false
        },
        {
          name: 'Activity-on-my-channel',
          text: "Notify me about comments and other activity on my channel or videos",
          selected: false
        },
        {
          name: 'Replies-to-my-comments',
          text: "Notify me about replies to my comments",
          selected: false
        },
        {
          name: 'Mentions',
          text: "Notify me when others mention my channel",
          selected: false
        },
        {
          name: 'Shared-content',
          text: "Notify me when others share my content on their channels",
          selected: false
        }
      ]
    }
  }
}
</script>
