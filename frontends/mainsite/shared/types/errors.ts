import { FetchError } from 'ofetch'
import type { H3Error } from 'h3'

/**
 * Creates a standardized error template based on the provided error object.
 * This function is useful for generating consistent error responses in API handlers. 
 * @param error The error object to generate the template from.
 */
export function createErrorTemplate(error: Error | FetchError | unknown) {
  const template: Partial<H3Error<typeof error>> = {
    statusCode: 500,
    statusMessage: 'An unknown error occurred',
    data: undefined,
    cause: error,
    message: 'An unknown error occurred'
  }

  try {
    if (error instanceof Error) {
      template.data = JSON.parse(error.message)
    }
  } catch {
    // Ignore JSON parse errors
  }

  if (error instanceof FetchError) {
    template.statusCode = error.response?.status || 500
    template.statusMessage = error.response?._data?.detail || `${error}`
  }

  return template
}
