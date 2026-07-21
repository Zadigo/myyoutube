import type { Playlist } from '~/types'
import { generateErrorTemplate } from '~/utils'

export default defineEventHandler(async (event) => {
  try {
    const { id } = getQuery<{ id: string }>(event)
    return await $fetch<Playlist>(`/v1/playlists/${id}`, {
      baseURL: useRuntimeConfig().public.djangoProdUrl,
      method: 'GET'
    })
  } catch (error) {
    const template = generateErrorTemplate(error)
    return createError(template)
  }
})
