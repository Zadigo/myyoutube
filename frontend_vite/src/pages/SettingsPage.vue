<template>
  <section id="settings">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card">
          <div class="card-body">
            <h1 class="h4">Choose how you appear and what you see on YouTube</h1>
          </div>
        </div>

        <!-- Account Type -->
        <settings-card title="Account type" subtitle="Manage what you share on YouTube">
          <template #default>
            <div class="alert alert-info">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas quo quibusdam nihil non placeat sed saepe aliquam dolore. Reiciendis soluta sed, voluptatem minima cumque alias obcaecati delectus recusandae similique pariatur.
            </div>

            <v-switch v-model="professionalAccount" label="My account is professional" inset></v-switch>

            <div v-if="professionalAccount" class="list-group list-group-radio d-grid gap-2 border-0 w-auto mt-4">
              <div class="position-relative">
                <input id="account-selection-0" name="account-selection" class="form-check-input position-absolute top-50 end-0 me-3 fs-5" type="radio" value="0">
                <label class="list-group-item py-3 pe-5" for="account-selection-0">
                  <strong class="fw-semibold">Artist</strong>
                </label>
              </div>
            </div>
          </template>
        </settings-card>

        <settings-card title="Membership" subtitle="Manage what you share on YouTube" class="card mt-1">
          <template #default>
            <h2>No subscriptions</h2>
            <v-btn class="mt-3" rounded="xl" size="x-large" color="warning" flat @click="showSubscriptions = true">
              Choose a subscription
            </v-btn>
          </template>
        </settings-card>

        <settings-card title="Vos chaînes YouTube" subtitle="Manage what you share on YouTube">
          <template #default>
            <div class="list-group my-2">
              <router-link :to="{ name: 'feed' }" class="list-group-item list-group-item-action">
                <div class="d-flex align-items-center gap-3">
                  <v-avatar image="/avatar1.png" size="30" alt=""></v-avatar>
                  <p class="m-0"> Channel name 1</p>
                </div>
              </router-link>
            </div>
          </template>
        </settings-card>
      </div>
    </div>

    <!-- Modals -->
    <v-dialog v-model="showSubscriptions" persistent>
      <v-card>
        <v-card-text>
          Something
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn @click="showSubscriptions = false">
            Disagree
          </v-btn>

          <v-btn @click="showSubscriptions = false">
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </section>
</template>

<script>
import { ref } from 'vue'
import SettingsCard from '../components/settings/SettingsCard.vue'

export default {
  components: {
    SettingsCard
  },
  setup () {
    const professionalAccount = ref(false)
    const showSubscriptions = ref(false)
    return {
      professionalAccount,
      showSubscriptions
    }
  }
}
</script>
