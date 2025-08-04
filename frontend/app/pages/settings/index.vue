<template>
  <section id="settings">
    <SettingsHeader>
      Choose how you appear and what you see on YouTube
    </SettingsHeader>

    <!-- Account Type -->
    <SettingsCard title="Account type" subtitle="Manage what you share on YouTube">
      <VoltAlert>
        You can choose to rank you account as a professional account. This will allow you to access 
        more features and tools on YouTube, such as advanced analytics and monetization options.
      </VoltAlert>

      <VoltLabel class="mt-5">
        <template #input>
          <VoltToggleSwitch v-model="professionalAccount" />
        </template>

        <template #label>
          My account is professional or artistic
        </template>
      </VoltLabel>

      {{ userSettings }}

      <div v-if="professionalAccount" class="p-5 rounded-lg bg-slate-100 mt-10 ms-10">
        <VoltLabel v-for="item in rankAs" :key="item">
          <VoltCheckbox v-model="userSettings.account_type" :value="item" />
          <label class="py-3 pe-5 font-semibold">
            {{ item }}
          </label>
        </VoltLabel>
        
        <div v-if="settingsStore.isBusiness">
          <VoltInputText placeholder="Business ID" />
          <VoltInputText placeholder="Business VAT" />
        </div>
      </div>
    </SettingsCard>

    <!-- Membership -->
    <SettingsCard title="YouTube Membership" subtitle="Manage your YouTube membership settings" class="mt-1">
      <template #default>
        <div class="grid grid-cols-3 gap-2">
          <VoltCard v-for="subscriptionType in subscriptionTypes" :key="subscriptionType" class="shadow-sm cursor-pointer" @click="() => { userSettings.subscription_name = subscriptionType }">
            <template #content>
              {{ subscriptionType }}
            </template>
          </VoltCard>
        </div>

        {{ hasSubscription }}

        <div class="text-center">
          <VoltButton :disabled="!hasSubscription" class="mt-3" @click="() => { showPayment=true }">
            Payment <Icon name="i-fa7-solid:arrow-right" />
          </VoltButton>
        </div>
      </template>
    </SettingsCard>

    <SettingsCard title="Vos chaînes YouTube" subtitle="Manage what you share on YouTube">
      <div class="my-2">
        <NuxtLink to="/" class="bg-slate-50 p-5 rounded-lg flex items-center w-full">
          <VoltAvatar image="/avatars/avatar1.png" shape="circle" size="large" alt="" />

          <p class="m-0">
            Channel name 1
          </p>
        </NuxtLink>
      </div>
    </SettingsCard>

    <!-- Modals -->
    <VoltDialog v-model:visible="showPayment" modal>
      <VoltButton @click="showPayment = false">
        Disagree
      </VoltButton>

      <VoltButton @click="showPayment = false">
        Agree
      </VoltButton>
    </VoltDialog>
  </section>
</template>

<script setup lang="ts">
import { rankAs, subscriptionTypes } from '~/data'

definePageMeta({
  layout: 'settings'
})

const professionalAccount = ref(false)
const showPayment = ref<boolean>(false)

const { data } = useFetch('/api/account/viewer-profile', {
  baseURL: useRuntimeConfig().public.djangoProdUrl,
  method: 'GET'
})

const settingsStore = useSettingsStore()
const { userSettings, hasSubscription } = storeToRefs(settingsStore)

const store = useViewerProfile()
const { profileData } = storeToRefs(store)

if (data.value) {
  profileData.value = data.value
}
</script>
