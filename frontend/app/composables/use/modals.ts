export type VideoMenuAction = 'Gift'
  | 'Save' 
  | 'Store' 
  | 'Recommendations' 
  | 'Donate' 
  | 'Report' 
  | 'Share' 
  | 'Classify'


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
