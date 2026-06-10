import type { CommunityNoteNode, CommunityNotes, Undefineable } from '~/types'

/**
 * Community Notes Composable
 * This composable is responsible for fetching and managing the state of community notes.
 * It provides a search functionality to filter notes based on their title and description.
 */
export const useCommunityNotesComposable = createSharedComposable(async () => {
  const { $moderationClient } = useNuxtApp()

  const communityNotes = computedAsync(async () => {
    try {
      return communityNotesFixture.data.allnotes.edges
      // return await $moderationClient<CommunityNotes>('/v1/moderation/', {
      //   method: 'POST',
      //   body: {
      //     query: `
      //       query {
      //         allnotes {
      //           edges {
      //             node {
      //               id
      //               reference
      //               author {
      //                 id
      //                 username
      //               }
      //               title
      //               description
      //               createdOn
      //             }
      //           }
      //         }
      //       }
      //     `
      //   }
      // })
    } catch (error) {
      console.error('Error fetching community notes:', error)
    }
  })

  /**
   * Search
   */

  const search = ref<string>('')

  const searchedCommunityNotes = computed(() => {
    if (isDefined(communityNotes)) {
      return useArrayFilter<CommunityNoteNode>(communityNotes, (note) => {
        return note.node.title.toLowerCase().includes(search.value.toLowerCase()) || note.node.description.toLowerCase().includes(search.value.toLowerCase())
      }).value
    } else {
      return []
    }
  })

  return {
    communityNotes,
    search,
    searchedCommunityNotes
  }
})

/**
 * Community Note By Id Composable
 * This composable is responsible for managing the state of a single community note, including its approval status and the reason for disapproval if applicable. 
 * @param note - The community note for which to manage the state. It can be a ref, a getter, or a direct value.
 */
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
          mutation($reference: String!, $voteType: String!, $reason: String) {
            createCommunityNoteVote(
              reference: $reference,
              voteType: $voteType,
              reason: $reason
            ) {
              reference
            }
          }
        `,
          variables: {
            reference: _note.node.reference,
            voteType,
            reason: reason.value
          }
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
