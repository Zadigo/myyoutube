export * from './moderation'
export * from './algorithm'

export const useSettingsComposable = createGlobalState(() => {
  const userSettings = reactive<UserSettings>({
    account_type: [],
    is_professional: false,
    subscription: {
      name: 'Free'
    }
  })

  const isBusiness = computed(() => {
    return userSettings.account_type.includes('Business') || userSettings.account_type.includes('News publisher or broadcaster')
  })

  const isArtist = computed(() => {
    return userSettings.account_type.includes('Artist')
  })

  const hasSubscription = computed(() => userSettings.subscription.name !== 'Free')

  return {
    userSettings,
    /**
     * Check if the user has a business account
     */
    isBusiness,
    /**
     * Check if the user is an artist
     */
    isArtist,
    /**
     * Check if the user has a subscription
     */
    hasSubscription
  }
})
