export type VideoMenuAction = 'Gift'
  | 'Store'
  | 'Download'
  | 'Save'
  | 'Gift'
  | 'Donate'
  | 'Share' 
  | 'Recommendations' 
  | 'Community note'
  | 'Fact check'
  | 'Report' 
  | 'Classify'

/**
 * Manages the state of various modals and drawers in the video detail view.
 * Provides reactive references to control the visibility of each modal/drawer.
 * Includes a function to open specific modals based on user actions.
 */
export function useVideoDetailModals() {
  const showClassificationDrawer = ref<boolean>(false)
  const showReportModal = ref<boolean>(false)
  const showGiftsModal = ref<boolean>(false)
  const showSaveModal = ref<boolean>(false)
  const showShareModal = ref<boolean>(false) 
  const showDonationModal = ref<boolean>(false)
  const showCommunityNotes = ref<boolean>(false)

  function openModal(action: VideoMenuAction) {
    if (action === 'Gift') {
      showGiftsModal.value = true
    }
  
    if (action === 'Save') {
      showSaveModal.value = true
    }
  
    if (action === 'Store') {
      // Pass
    }
  
    if (action === 'Recommendations') {
      showClassificationDrawer.value = true
    }
  
    if (action === 'Donate') {
      showDonationModal.value = true
    }
  
    if (action === 'Report') {
      showReportModal.value = true
    }
  
    if (action === 'Share') {
      showShareModal.value = true
    }
  
    if (action === 'Classify') {
      showClassificationDrawer.value = true
    }
  }

  return {
    /**
     * Opens the modal or drawer corresponding to the given action.
     * @param action The action that determines which modal/drawer to open.
     */
    openModal,
    showClassificationDrawer,
    showReportModal,
    showGiftsModal,
    showSaveModal,
    showShareModal,
    showDonationModal,
    showCommunityNotes
  }
}
