<template>
  <section id="billing">
    <SettingsHeader>
      Manage your YouTube billing settings
    </SettingsHeader>

    <!-- Membership -->
    <SettingsCard title="YouTube Membership" subtitle="Manage your YouTube membership settings" class="mt-1">
      <template #default>
        <div class="grid grid-cols-3 gap-2">
          <VoltCard v-for="subscriptionType in subscriptionTypes" :key="subscriptionType" :class="{ 'bg-primary-100': userSettings.subscription.name === subscriptionType }" class="border border-slate-50 bg-primary-50 cursor-pointer shadow-none" @click="() => { userSettings.subscription.name = subscriptionType }">
            <template #content>
              <div class="font-bold text-2 text-center">
                {{ subscriptionType }}

                <div class="text-3xl font-bold mt-3">
                  5.99€<span class="text-sm">/month</span>
                </div>
              </div>
            </template>
          </VoltCard>
        </div>

        {{ hasSubscription }}

        <div class="flex justify-end">
          <VoltButton :disabled="!hasSubscription" class="mt-3" @click="() => { showPayment=true }">
            Payment <Icon name="i-fa7-solid:arrow-right" />
          </VoltButton>
        </div>
      </template>
    </SettingsCard>

    <SettingsCard title="Bills" subtitle="YouTube bills and payment history" class="mt-1">
      <template #default>
        <div class="flex justify-end mb-5">
          <VoltButton class="hover:bg-primary-200">
            Cancel subscription <Icon name="i-fa7-solid:arrow-right" />
          </VoltButton>
        </div>
        
        <ul>
          <li v-for="i in 5" :key="i" class="mb-2">
            <VoltCard class="border border-slate-50 bg-primary-50 cursor-pointer shadow-none">
              <template #content>
                <div class="text-2">
                  2/01/2023 - YouTube Premium - 5.99€/month
                </div>
              </template>
            </VoltCard>
          </li>
        </ul>
      </template>
    </SettingsCard>

    <!-- Modals -->
    <ModalsSettingsPayment v-model="showPayment" />
  </section>
</template>

<script setup lang="ts">
import { subscriptionTypes } from '~/data'

definePageMeta({
  layout: 'settings'
})

const showPayment = ref<boolean>(false)

const settingsStore = useSettingsStore()
const { userSettings, hasSubscription } = storeToRefs(settingsStore)
</script>
