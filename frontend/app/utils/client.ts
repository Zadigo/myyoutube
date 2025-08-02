import type { CustomLoginApiResponse, LoginApiResponse, RefreshApiResponse } from "~/apps/types"

/**
 * Helper function used to ask for a new access
 * token for the user
 * 
 * @param refresh The refresh token
 */
export async function refreshAccessToken(refresh: string | undefined) {
  if (!refresh) {
    return {
      access: null
    }
  }

  const response = await $fetch<RefreshApiResponse>('/auth/v1/refresh/token/', {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    method: 'POST',
    body: {
      refresh
    }
  })

  return {
    access: response.access
  }
}

/**
 * Function used to login the user in the frontend 
 * 
 * @param email The email address
 * @param password The password to use
 */
export async function login(email: string, password: string): Promise<CustomLoginApiResponse>  {
  if (import.meta.server) {
    return {
      failureCount: 0,
      access: '',
      refresh: ''
    }
  }

  const failureCount = ref(0)

  const response = await $fetch<LoginApiResponse>('/auth/v1/token/', {
    baseURL: useRuntimeConfig().public.djangoProdUrl,
    method: 'POST',
    body: {
      username: email,
      password
    },
    onRequestError() {
      failureCount.value += 1
    }
  })

  return {
    failureCount: failureCount.value,
    access: response.access,
    refresh: response.refresh
  }
}

/**
 * 
 */
export async function logout() {
  if (import.meta.server) {
    return
  }

  const accessToken = useCookie('access')
  const refreshToken = useCookie('refresh')

  accessToken.value = null
  refreshToken.value = null

  // router.push('/')
}
