<template>
  <section class="moderation">
    <settings-header>
      Moderate what you see on YouTube
    </settings-header>

    <!-- Blocked channels -->
    <settings-card title="Blocked channels" subtitle="Channels that you blocked and do not want to see">
      <base-list-group v-if="hasChannels" :items="channels">
        <template #default="{ item }">
          <div class="flex justify-start items-center gap-3">
            <u-avatar src="/avatars/avatar1.png" size="xl" />
            <span>{{ item.channel.name }}</span>
          </div>

          <u-button color="error" variant="subtle">
            <icon name="lucide:arrow-left" />
          </u-button>
        </template> 
      </base-list-group>
    </settings-card>

    <!-- Blocked Keywords -->
    <settings-card title="Blocked keywords" subtitle="Block videos containing certain specific keywords (title, description)">
      <template #default>
        <div class="flex justify-start gap-2">
          <u-input v-model="newKeyword.word" placeholder="Enter a keyword to block" @keypress.enter="create" />
          <u-select v-model="newKeyword.duration" :options="Array.from(BLOCKING_DURATIONS)" />
        </div>

        <u-switch v-model="excludeFollowedAccounts" label="Exclude accounts that you follow" />

        <!-- <volt-list v-if="hasKeywords" :items="keywords" item-label="word">
          <template #default="{ item }">
            <div class="flex justify-between items-center gap-2">
              <div class="space-x-2">
                <p>
                  {{ item.word }}
                </p>

                <u-badge>
                  {{ item.duration }}
                </u-badge>
              </div>

              <u-button @click="() => remove(i)">
                <icon name="i-fa7-solid:trash" />
              </u-button>
            </div>
          </template>
        </volt-list> -->
      </template>
    </settings-card>

    <!-- Moderation Lists -->
    <settings-card title="Block lists" subtitle="Create shareable block lists">
      <template #default>
        <base-alert>
          Blocklists are lists of accounts that other users have create of
          accounts that they have associated to be problematic
        </base-alert>
        
        <div class="flex justify-center">
          <u-button color="secondary" variant="subtle" rounded @click="() => { showBlockLists=true }">
            Use or create block lists
          </u-button>
        </div>
      </template>
    </settings-card>

    <!-- Modals -->
    <lazy-modals-moderation-block-lists v-model="showBlockLists" hydrate-on-visible />
    <lazy-modals-moderation-create-list v-model="showCreateList" hydrate-on-visible />
  </section>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'settings'
})

const { keywords, hasKeywords, create, remove, newKeyword, excludeFollowedAccounts } = useBlockedKeywordsComposable()
const { channels, hasChannels, showCreateList, showBlockLists } = useBlockedChannels()
</script>
