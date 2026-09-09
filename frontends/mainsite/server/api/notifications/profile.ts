export default defineCachedEventHandler(async (event) => {
  try {
    const refresh = getCookie(event, 'refresh')
    return await $fetch<NotificationProfile>('/api/v1/notifications/profile', {
      baseURL: useRuntimeConfig().public.djangoProdUrl,
      params: {},
      onRequestError({ response, error }) {
        if (response) {
          if (response.status === 401) {
            refreshAccessToken(refresh)
            console.log(error)
          }
        }
      }
    })
  } catch (error) {
    const template = createErrorTemplate(error)
    return createError(template)
  }
})
