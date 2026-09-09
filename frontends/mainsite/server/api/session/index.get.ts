import { createErrorTemplate } from '#shared/errors'
import type { SessionData } from '#shared/types/session'

export default defineEventHandler(async (event) => {
  try {
    const { docRef } = await getOrCreateSession(event)
    const result = await docRef.get()
    return result.data() as SessionData
  } catch(error) {
    const template = createErrorTemplate(error)
    throw createError(template)
  }
})
