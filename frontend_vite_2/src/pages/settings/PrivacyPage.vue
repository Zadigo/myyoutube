<template>
  <section id="algorithm">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card shadow-sm">
          <div class="card-body">
            <h2>Privacy</h2>
          </div>
        </div>

        <settings-card class="shadow-sm" title="General" subtitle="Manage what you share on YouTube">
          <div class="list-group">
            <div class="list-group-item">
              <v-switch label="Keep all my saved playlists private" inset hide-details />
            </div>

            <div class="list-group-item">
              <v-switch label="Keep all my subscriptions private" inset hide-details />
            </div>
          </div>
        </settings-card>

        <settings-card class="shadow-sm" title="Ad personalization" subtitle="Manage what you share on YouTube">
          <p>Google makes your ads more useful on Google services (such as Search or YouTube), and on websites & apps that partner with Google to show ads</p>
          
          <div class="list-group">
            <div class="list-group-item">
              <v-switch label="Personalize ads" inset hide-details />
            </div>
          </div>

          <h4 class="mt-5">
            How your ads are personalized
          </h4>

          <p>
            Ads are based on personal info you've added to your 
            Google Account, data from advertisers that partner with Google, 
            and Google's estimation of your interests. Choose any factor to learn 
            more or update your preferences. Learn how to control the ads you see
          </p>

          <v-btn variant="text">
            Show categories
          </v-btn>
        </settings-card>

        <hr class="my-5">

        <h2>Sensitive ad categories on YouTube</h2>
        <p>Select the categories for which you want to see less of</p>

        <div class="list-group">
          <div v-for="sensitiveCategory in sensitiveCategories" :key="sensitiveCategory" class="list-group-item">
            <v-switch :label="sensitiveCategory" inset hide-details />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

import SettingsCard from '@/components/settings/SettingsCard.vue';
import { CustomUser } from '@/types/authentication';

const sensitiveCategories = [
  'Alcohol',
  'Dating',
  'Gambling',
  'Pregnancy and parenting',
  'Weight loss'
]

export default defineComponent({
  components: {
    SettingsCard
  },
  setup () {
    const requestData = ref<CustomUser | null>(null)
    return {
      requestData,
      sensitiveCategories
    }
  },
  methods: {
    async handleAccountDetails () {
      try {
        const response = await this.$client.get<CustomUser>('/accounts/base')
        this.requestData = response.data
      } catch {
        // Handle error
      }
    }
  }
})
</script>
