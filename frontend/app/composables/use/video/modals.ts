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
 * @deprecated
 */
export function _useVideoDetailModals() {
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

const [useVideoDetailModals, _useVideoDetailModalsStore] = createInjectionState(() => {
  const [showClassificationDrawer, toggleClassificationDrawer] = useToggle<boolean>(false)
  const [showReportModal, toggleShowReportModal] = useToggle<boolean>(false)
  const [showGiftsModal, toggleShowGiftsModal] = useToggle <boolean>(false)
  const [showSaveModal, toggleShowSaveModal] = useToggle<boolean>(false)
  const [showShareModal, toggleShowShareModal] = useToggle<boolean>(false)
  const [showDonationModal, toggleShowDonationModal] = useToggle<boolean>(false)
  const [showCommunityNotes, toggleShowCommunityNotes] = useToggle<boolean>(false)

  function openModal(action: VideoMenuAction) {
    console.log('Opening modal for action:', action)
    if (action === 'Gift') {
      toggleShowGiftsModal()
    }

    if (action === 'Save') {
      toggleShowSaveModal()
    }

    if (action === 'Store') {
      // Pass
    }

    if (action === 'Recommendations') {
      toggleClassificationDrawer()
    }

    if (action === 'Donate') {
      toggleShowDonationModal()
    }

    if (action === 'Report') {
      toggleShowReportModal()
    }

    if (action === 'Share') {
      showShareModal.value = true
    }

    if (action === 'Classify') {
      toggleClassificationDrawer()
    }
  }

  return {
    showClassificationDrawer,
    showReportModal,
    showGiftsModal,
    showSaveModal,
    showShareModal,
    showDonationModal,
    showCommunityNotes,
    openModal,
    toggleClassificationDrawer,
    toggleShowReportModal,
    toggleShowGiftsModal,
    toggleShowSaveModal,
    toggleShowShareModal,
    toggleShowDonationModal,
    toggleShowCommunityNotes
  }
})

export { useVideoDetailModals }

export function tryUseVideoDetailModalsStore() {
  const counterStore = _useVideoDetailModalsStore()
  if (counterStore == null) {
    throw new Error('Please call `useVideoDetailModals` on the appropriate parent component')
  } else {
    return counterStore
  }
}
