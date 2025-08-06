import type { AlgorithmConditionBlock } from '~/data'
import type { RankAs, SubscriptionType } from '~/data/constants'
import type { NotificationProfile, ViewingProfile } from '~/types'

export interface UserSettings {
  account_type: RankAs[]
  is_professional: boolean
  subscription_name: SubscriptionType
}

/**
 * Store for user settings and profile information.
 * This store manages the user's account type, professional status, and subscription details.
 */
export const useSettingsStore = defineStore('settings', () => {
  const userSettings = reactive<UserSettings>({
    account_type: [],
    is_professional: false,
    subscription_name: 'Free'
  })

  const isBusiness = computed(() => {
    return userSettings.account_type.includes('Business') || userSettings.account_type.includes('News publisher or broadcaster')
  })

  const isArtist = computed(() => {
    return userSettings.account_type.includes('Artist')
  })

  const hasSubscription = computed(() => userSettings.subscription_name !== 'Free')

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

/**
 *  Store for viewer profile and notification settings.
 * This store holds the profile data and notification preferences for the logged-in user.
 */
export const useViewerProfile = defineStore('viewer_profile', () => {
  const profileData = ref<ViewingProfile>()
  const notificationData = ref<NotificationProfile>()

  return {
    profileData,
    notificationData
  }
})

export const useAlgorithmSettingsStore = defineStore('algorithm_settings', () => {
  const conditions = ref<AlgorithmConditionBlock[]>([])

  watchArray(conditions, (newList, oldList) => {
    // Do something
    console.log(newList,  oldList)
  })

  const getCurrentBlock = reactify((index: number) => {
    return conditions.value[index]
  })

  return {
    conditions,
    getCurrentBlock
  }
})
