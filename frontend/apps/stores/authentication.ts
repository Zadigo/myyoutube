import { defineStore } from "pinia";

export const useAuthentication = defineStore('authentication', () => {
    const accessToken = ref<string>()
    const refreshToken = ref<string>()

    const isAuthenticated = computed(() => {
        return (
            accessToken.value !== '' || 
            accessToken.value !== null ||
            typeof accessToken.value !== 'undefined'
        )
    })

    function logout() {
        accessToken.value = ''
        refreshToken.value = ''
    }

    return {
        logout,
        isAuthenticated,
        accessToken,
        refreshToken
    }
})
