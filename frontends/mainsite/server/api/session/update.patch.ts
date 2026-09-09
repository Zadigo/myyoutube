import { createErrorTemplate } from '#shared/errors'

export default defineEventHandler(async (event) => {
  try {
    const { docRef } = await getOrCreateSession(event)
    await docRef.update({
      language: {
        choice: 'en',
        selected: true
      },
      updatedAt: new Date()
    })

    return {
      state: 'Session updated successfully',
    }
  } catch (error) {
    const template = createErrorTemplate(error)
    throw createError(template)
  }
})
