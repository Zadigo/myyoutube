<template>
  <section id="community-note">
    <div v-if="communityNote" class="grid grid-cols-2 gap-2">
      <div class="col-span-2 mb-5">
        <nuxt-card>
          <template #content>
            <u-button to="/community-notes">
              <icon name="i-lucide-arrow-left" />
              Back
            </u-button>
          </template>
        </nuxt-card>
      </div>

      <!-- User Information -->
      <aside>
        <u-card>
          <h1 class="text-2xl font-bold mb-3">{{ communityNote.node.author.username }}</h1>
          <img src="/avatars/avatar1.png" :alt="communityNote.node.author.username" class="rounded-lg">
        </u-card>
      </aside>

      <!-- Note Details -->
      <div class="space-y-2">
        <u-card>
          <div class="flex items-center justify-start gap-2">
            <h2 class="font-bold text-xl">{{ communityNote.node.title }}</h2>
            <u-badge :label="communityNote.node.status" size="xl" variant="subtle" />
          </div>

          <p class="text-sm text-gray-600">{{ communityNote.node.description }}</p>

          <div class="mt-4 space-x-2">
            <u-button @click="() => { createVote('upvote') }">
              <icon name="lucide:thumbs-up" />
            </u-button>

            <u-button @click="() => { toggleShouldDemandReason() }">
              <icon name="lucide:thumbs-down" />
            </u-button>

            <div v-if="shouldDemandReason" id="readon">
              <u-textarea v-model="reason" class="mt-2" :style="{ resize: 'none' }" />

              <u-button class="mt-2" @click="() => { createVote('downvote') }">
                Submit Reason
              </u-button>
            </div>
          </div>
        </u-card>

        <!-- Other Notes -->
        <u-card>
          <h2 class="font-bold text-xl mb-4">
            Other Notes on {{ communityNote.node.subjectCreatorId }} (36)
          </h2>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <community-card v-if="communityNote" :note="communityNote" />
            <div v-else>Community note not found.</div>
          </div>
        </u-card>

        <!-- Note Sources -->
        <u-card>
          <h2 class="font-bold text-xl mb-4">Sources</h2>
          <ul>
            <li v-for="(source, index) in communityNote.node.noteSources" :key="index" class="rounded-lg bg-primary-50 p-5 flex items-center gap-2">
              <icon name="lucide:link" />
              <nuxt-link :to="source.url" class="text-primary-500 dark:text-primary-400 hover:underline" target="_blank">
                {{ source.url }}
              </nuxt-link>
            </li>
          </ul>
        </u-card>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const { communityNotes } = await useCommunityNotesComposable()

const { id } = useRoute().params
const getCommunityNote = reactify(() => isDefined(communityNotes) ?  communityNotes.value.find(note => note.node.reference === id) : undefined)
const communityNote = getCommunityNote()

/**
 * Voting
 */

const { createVote, shouldDemandReason, toggleShouldDemandReason, reason } = useCommunityNoteById(communityNote)
</script>
