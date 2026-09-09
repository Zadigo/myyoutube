import { createErrorTemplate } from '~/utils/errors'

export default defineEventHandler(async (event) => {
  try {
    const query = getQuery<{ offset?: number }>(event)
    return await $fetch<NotificationApiResponse>('/', {
      method: 'GET',
      query: {
        offset: query?.offset
      }
    })
  } catch (error) {
    const template = createErrorTemplate(error)
    throw createError(template)
  }
})
