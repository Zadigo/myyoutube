import { defineStore } from 'pinia'

export const useAuthenticationStore = defineStore('authentication', () => {
  const accessToken = ref<string | null | undefined>()
  const refreshToken = ref<string | null | undefined>()

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
