<template>
  <section id="settings">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card">
          <div class="card-body">
            <h1 class="h4">
              Choose how you appear and what you see on YouTube
            </h1>
          </div>
        </div>

        <!-- Account Type -->
        <SettingsCard title="Account type" subtitle="Manage what you share on YouTube">
          <template #default>
            <div class="alert alert-info">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas quo quibusdam nihil non placeat sed saepe aliquam dolore. Reiciendis soluta sed, voluptatem minima cumque alias obcaecati delectus recusandae similique pariatur.
            </div>

            <v-switch v-model="professionalAccount" label="My account is professional" inset />

            <div v-if="professionalAccount" class="list-group list-group-radio d-grid gap-2 border-0 w-auto mt-4">
              <div class="position-relative">
                <input id="account-selection-0" name="account-selection" class="form-check-input position-absolute top-50 end-0 me-3 fs-5" type="radio" value="0">
                <label class="list-group-item py-3 pe-5" for="account-selection-0">
                  <strong class="fw-semibold">Artist</strong>
                </label>
              </div>
            </div>
          </template>
        </SettingsCard>

        <SettingsCard title="Membership" subtitle="Manage what you share on YouTube" class="card mt-1">
          <template #default>
            <v-item-group v-model="currentSubscription" selected-class="bg-primary">
              <v-container>
                <v-row>
                  <v-col v-for="subscription in subscriptions" :key="subscription" cols="12" md="4">
                    <v-item v-slot="{ selectedClass, toggle }">
                      <v-card :class="[selectedClass]" class="d-flex align-center" height="200" dark @click="toggle">
                        <div class="text-h5 flex-grow-1 text-center">
                          {{ subscription }}
                        </div>
                      </v-card>
                    </v-item>
                  </v-col>
                </v-row>
              </v-container>
            </v-item-group>

            <div class="text-center">
              <v-btn :disabled="currentSubscription < 1" class="mt-3" rounded="xl" size="x-large" color="warning" flat @click="showSubscriptions = true">
                Payment <font-awesome :icon="[ 'fas', 'fa-arrow-right' ]" />
              </v-btn>
            </div>
          </template>
        </SettingsCard>

        <SettingsCard title="Vos chaînes YouTube" subtitle="Manage what you share on YouTube">
          <template #default>
            <div class="list-group my-2">
              <NuxtLink to="/" class="list-group-item list-group-item-action">
                <div class="d-flex align-items-center gap-3">
                  <v-avatar image="/avatar1.png" size="30" alt="" />
                  
                  <p class="m-0">
                    Channel name 1
                  </p>
                </div>
              </NuxtLink>
            </div>
          </template>
        </SettingsCard>
      </div>
    </div>

    <!-- Modals -->
    <v-dialog v-model="showSubscriptions" width="700px" persistent>
      <v-card>
        <v-card-text>
          <!-- <v-stepper v-model="currentPaymentStep" :items="['Address', 'Payment']" model-value="0">
            <template #item.1>
              <v-card title="Address" flat>
                <v-form id="address" @submit.prevent>
                  <input type="text" autocomplete="address-level1">
                  <v-text-field autocomplete="address-level1"></v-text-field>
                </v-form>
              </v-card>
            </template>

            <template #:item.2>
              <v-card title="Payment" flat>
                <v-form id="paymment" @submit.prevent>
                  <div id="payment">
                    <v-text-field placeholder="Card number" aria-placeholder="Card number" autocomplete="cc-number" variant="outlined"></v-text-field>

                    <div class="d-flex justify-content-between gap-2">
                      <v-text-field autocomplete="cc-exp-month" placeholder="Expiry month" variant="outlined"></v-text-field>
                      <v-text-field autocomplete="cc-exp-year" placeholder="Expiry year" variant="outlined"></v-text-field>
                      <v-text-field autocomplete="cc-csc" placeholder="CVV" variant="outlined"></v-text-field>
                    </div>
                  </div>
                </v-form>
              </v-card>
            </template>
          </v-stepper> -->
        </v-card-text>

        <v-card-actions>
          <v-spacer />

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

<script setup lang="ts">
import { ref } from 'vue'
import type { ViewingProfile } from '~/types'

definePageMeta({
  layout: 'settings'
})

const subscriptions = [
  'Free',
  'YouTube+',
  'YouTube++'
]

const professionalAccount = ref(false)
const showSubscriptions = ref(false)
const currentSubscription = ref<number>(0)

const { data } = useFetch('/api/account/viewer-profile', {
  transform(data: ViewingProfile) {
    return data
  }
})

const store = useViewerProfile()
const { profileData } = storeToRefs(store)

if (data.value) {
  profileData.value = data.value
}
</script>
