import { communityNotesFixture } from '~/data/fixtures/moderation'
import type { CommunityNotes } from "~/types"

export async function useCommunityNotesComposable() {
  const { $moderationClient } = useNuxtApp()
  const communityNotes = ref<CommunityNotes>(communityNotesFixture)

  try {
    await $moderationClient<CommunityNotes>('/v1/moderation/', {
      method: 'POST',
      body: {
        query: `
        query {
          allnotes {
            edges {
              node {
                id
                reference
                creatorId
                createdOn
                votes
              }
            }
          }
        }
      `
      }
    })
  } catch (error) {
    console.error('Error fetching community notes:', error)
  }

  return {
    communityNotes
  }
}
