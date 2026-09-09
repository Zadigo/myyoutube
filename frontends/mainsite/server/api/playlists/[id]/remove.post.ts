import { createErrorTemplate } from '#shared/errors'

export default defineEventHandler(async (_event) => {
  try {
    return 
    // const { id } = getQuery<{ id: string }>(event)
    // return await $fetch<Playlist>(`/v1/playlists/${id}`, {
    //   baseURL: useRuntimeConfig().public.djangoProdUrl,
    //   method: 'DELETE'
    // })
  } catch (error) {
    const template = createErrorTemplate(error)
    return createError(template)
  }
})
