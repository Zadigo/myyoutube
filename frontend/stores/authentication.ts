import { defineStore } from "pinia";
import type { LoginApiResponse } from "~/types";

export const useAuthentication = defineStore('authentication', () => {
    const accessToken = ref<string | null | undefined>('')
    const refreshToken = ref<string | null | undefined>('')

    const isAuthenticated = computed(() => {
        return accessToken.value !== '' || accessToken.value !== null
    })

    return {
        isAuthenticated,
        accessToken,
        refreshToken
    }
})
