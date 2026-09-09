import { createErrorTemplate } from '#shared/errors'

export default defineEventHandler(async (_event) => {
  try {
    return []
    // return await $fetch<Playlist[]>('/v1/playlists', {
    //   baseURL: useRuntimeConfig().public.djangoProdUrl,
    //   method: 'GET'
    // })
  } catch (error) {
    const template = createErrorTemplate(error)
    return createError(template)
  }
})
