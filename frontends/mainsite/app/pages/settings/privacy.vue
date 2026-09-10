<template>
  <section id="algorithm">
    <SettingsHeader>
      Privacy
    </SettingsHeader>

    <SettingsCard class="shadow-sm" title="General" subtitle="Manage what you share on YouTube">
      <base-list-group>
        <template #body="{ theme }">
          <div :class="theme">
            <u-switch label="Keep all my saved playlists private" />
          </div>

          <div :class="theme">
            <u-switch label="Keep all my subscriptions private" />
          </div>
        </template>
      </base-list-group>
    </SettingsCard>

    <SettingsCard class="shadow-sm" title="Ad personalization" subtitle="Manage what you share on YouTube">
      <p>Google makes your ads more useful on Google services (such as Search or YouTube), and on websites & apps that partner with Google to show ads</p>
      
      <base-list-group>
        <template #body="{ theme }">
          <div :class="theme">
            <u-switch label="Personalize ads" />
          </div>
        </template>
      </base-list-group>

      <h4 class="mt-5">
        How your ads are personalized
      </h4>

      <p>
        Ads are based on personal info you've added to your 
        Google Account, data from advertisers that partner with Google, 
        and Google's estimation of your interests. Choose any factor to learn 
        more or update your preferences. Learn how to control the ads you see
      </p>

      <u-button variant="ghost">
        Show categories
      </u-button>
    </SettingsCard>

    <u-separator class="my-5" />

    <div>
      <h2 class="text-3xl font-bold">Sensitive ad categories on YouTube</h2>
      <p class="text-sm mb-5">Select the categories for which you want to see less of</p>

      <base-list-group :items="Array.from(SENSITIVE_CATEGORIES)">
        <template #default="{ item }">
          <u-switch :label="item.label" />
        </template>
      </base-list-group>
    </div>
  </section>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'settings'
})
</script>
