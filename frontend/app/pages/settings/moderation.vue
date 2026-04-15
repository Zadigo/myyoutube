<template>
  <section class="moderation">
    <settings-header>
      Moderate what you see on YouTube
    </settings-header>

    <!-- Blocked channels -->
    <settings-card title="Blocked channels" subtitle="Channels that you blocked and do not want to see">
      <volt-list v-if="hasChannels" :items="channels">
        <template #default="{ item }">
          <div class="flex justify-start items-center gap-3">
            <volt-avatar image="/avatars/avatar1.png" shape="circle" size="large" />
            <span>{{ item.channel.name }}</span>
          </div>

          <volt-button color="danger" variant="text">
            <icon name="lucide:arrow-left" />
          </volt-button>
        </template> 
      </volt-list>
    </settings-card>

    <!-- Blocked Keywords -->
    <settings-card title="Blocked keywords" subtitle="Block videos containing certain specific keywords (title, description)">
      <template #default>
        <div class="flex justify-start gap-2">
          <!-- <volt-input-text v-model="newKeyword.word" variant="outlined" placeholder="Enter a keyword to block" @keypress.enter="create" />
          <volt-select v-model="newKeyword.duration" :options="Array.from(blockingDurations)" /> -->
        </div>

        <volt-label class="my-5">
          <template #input>
            <volt-toggle-switch v-model="excludeFollowedAccounts" />
          </template>

          <template #label>
            Exclude accounts that you follow
          </template>
        </volt-label>

        <!-- <volt-list v-if="hasKeywords" :items="keywords" item-label="word">
          <template #default="{ item }">
            <div class="flex justify-between items-center gap-2">
              <div class="space-x-2">
                <p>
                  {{ item.word }}
                </p>

                <volt-badge>
                  {{ item.duration }}
                </volt-badge>
              </div>

              <volt-button @click="() => remove(i)">
                <icon name="i-fa7-solid:trash" />
              </volt-button>
            </div>
          </template>
        </volt-list> -->
      </template>
    </settings-card>

    <!-- Moderation Lists -->
    <settings-card title="Block lists" subtitle="Create shareable block lists">
      <template #default>
        <volt-alert>
          Blocklists are lists of accounts that other users have create of
          accounts that they have associated to be problematic
        </volt-alert>
        
        <div class="flex justify-center">
          <volt-button color="secondary" variant="tonal" rounded @click="() => { showBlockLists=true }">
            Use or create block lists
          </volt-button>
        </div>
      </template>
    </settings-card>

    <!-- Modals -->
    <lazy-modals-moderation-block-lists v-model="showBlockLists" hydrate-on-visible />
    <lazy-modals-moderation-create-list v-model="showCreateList" hydrate-on-visible />
  </section>
</template>

<script setup lang="ts">
import { blockingDurations } from '~/data'

definePageMeta({
  layout: 'settings'
})

const { keywords, hasKeywords, create, remove, newKeyword, excludeFollowedAccounts } = useBlockedKeywordsComposable()
const { channels, hasChannels, showCreateList, showBlockLists } = useBlockedChannels()
</script>
