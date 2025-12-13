import { communityNotesFixture } from '~/data/fixtures/moderation'
import type { CommunityNoteNode, CommunityNotes, Undefineable } from '~/types'

export const useCommunityNotesComposable = createSharedComposable(async () => {
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
                author {
                  id
                  username
                }
                title
                description
                createdOn
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
})

export function useCommunityNoteById(note: MaybeRefOrGetter<Undefineable<CommunityNoteNode>>) {
  const _note = toValue(note)
  const { $moderationClient } = useNuxtApp()
  /**
   * Appobation
   */
  const approval = ref({
    isApproved: false,
    isDisapproved: false
  })

  const [shouldDemandReason, toggleShouldDemandReason] = useToggle(false)

  whenever(() => approval.value.isDisapproved, () => {
    toggleShouldDemandReason()
  })

  /**
   * New Vote
   */

  const reason = ref('')

  async function createVote(voteType: 'upvote' | 'downvote') {
    if (isDefined(_note)) {
      await $moderationClient('/v1/moderation/', {
        method: 'POST',
        body: {
          query: `
          mutation {
            createCommunityNoteVote(
              reference: "${_note.node.reference}",
              voteType: "${voteType}",
              reason: ${reason.value ? `"${reason.value}"` : null}
            ) {
              reference
            }
          }
        `
        }
      })
    }
  }

  return {
    approval,
    shouldDemandReason,
    reason,
    toggleShouldDemandReason,
    createVote
  }
}
