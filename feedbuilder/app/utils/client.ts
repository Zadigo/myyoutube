import type { CustomLoginApiResponse, LoginApiResponse, RefreshApiResponse } from '~/types'

/**
 * Helper function used to ask for a new access
 * token for the user
 * 
 * @param refresh The refresh token
 */
export async function refreshAccessToken(refresh: string | null | undefined) {
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
 * Function used to refresh the access token
 * on the client side
 */
export async function refreshAccessTokenClient() {
  if (import.meta.server) {
    return {
      access: null
    }
  }

  const refreshToken = useCookie('refresh')
  const response = await refreshAccessToken(refreshToken.value)

  if (response.access) {
    useCookie('access').value = response.access
  }

  return response
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
 * Function used to logout the user
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

/**
 * Function used to encode and decode messages
 * for websocket communication
 */
export function useWebsocketMessages() {
  function send<M extends object>(message: M, ws?: WebSocket): string {
    const data = JSON.stringify(message)
    if (ws) {
      ws.send(data)
    }
    return data
  }

  function decode<T>(message: string): Ref<T> {
    return toRef(JSON.parse(message))
  }

  return {
    send,
    decode
  }
}
