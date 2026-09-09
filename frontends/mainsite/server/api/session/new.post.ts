import { createErrorTemplate } from '#shared/errors'

type SessionResponse = {
  sessionId: string
}

export default defineEventHandler(async (event) => {
  try {
    const { docRef } = await getOrCreateSession(event)
    return { sessionId: docRef.id } as SessionResponse
  } catch (error) {
    console.error('Error creating session:', error)
    const template = createErrorTemplate(error)
    throw createError(template)
  }
})
