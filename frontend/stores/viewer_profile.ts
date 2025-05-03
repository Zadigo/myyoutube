import type { NotificationProfile, ViewingProfile } from "~/types"

export const useViewerProfile = defineStore('viewer_profile', () => {
    const profileData = ref<ViewingProfile>()
    const notificationData = ref<NotificationProfile>()
    return {
        profileData,
        notificationData
    }
})
