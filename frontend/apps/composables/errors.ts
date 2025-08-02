import { ref } from 'vue'

import { FetchError } from 'ofetch'

export interface ErrorContext {
    message: string
    code?: string
    type: 'warning' | 'error' | 'info'
}

export function useErrorHandler() {
    // Global error state (optional, can be used for error logging or global error display)
    const globalError = ref<ErrorContext | null>(null)
    const { $toast } = useNuxtApp()

    // Utility for logging errors to a service
    function logErrorToService(_error: FetchError) {
        // Implementation depends on your error logging service
        // Could be Sentry, LogRocket, custom backend endpoint, etc.
    }

    // Specific error type handlers
    function handleBadRequest(error: FetchError) {
        $toast.error('Bad Request', {
            description: error.message,
            position: 'top-center'
        })

        globalError.value = {
            message: error.message,
            type: 'warning'
        }
    }

    function handleUnauthorized(_error: FetchError) {
        // Potential redirect to login or token refresh
        $toast.error('Unauthorized', {
            description: 'Please log in again',
            position: 'top-center'
        })

        // Example of potential logout and redirect
        const authStore = useAuthentication()
        authStore.logout()
    }

    function handleForbidden(_error: FetchError) {
        $toast.error('Access Denied', {
            description: 'You do not have permission to perform this action',
            position: 'top-center'
        })
    }

    function handleNotFound(_error: FetchError) {
        $toast.error('Not Found', {
            description: 'The requested resource could not be found',
            position: 'top-center'
        })
    }

    function handleServerError(error: FetchError) {
        // Log to error tracking service
        logErrorToService(error)

        $toast.error('Server Error', {
            description: 'An unexpected error occurred. Our team has been notified.',
            position: 'top-center'
        })
    }

    function handleGenericError(error: Error) {
        $toast.error('Error', {
            description: error.message,
            position: 'top-center'
        })
    }

    function handleUnknownError(error: unknown) {
        $toast.error('Unexpected Error', {
            description: 'An unknown error occurred',
            position: 'top-center'
        })

        // Potentially log the entire error object for debugging
        console.error('Unhandled error:', error)
    }

    function customErrorHandler(error: unknown) {
        // Type guard to check if it's an Axios error
        if (error instanceof FetchError) {
            const axiosError = error as FetchError

            // Different handling based on error status
            switch (axiosError.response?.status) {
                case 400:
                    handleBadRequest(axiosError)
                    break
                case 401:
                    handleUnauthorized(axiosError)
                    break
                case 403:
                    handleForbidden(axiosError)
                    break
                case 404:
                    handleNotFound(axiosError)
                    break
                case 500:
                    handleServerError(axiosError)
                    break
                default:
                    handleGenericError(axiosError)
            }
        } else if (error instanceof Error) {
            // Handle standard JavaScript errors
            handleGenericError(error)
        } else {
            // Catch-all for unexpected error types
            handleUnknownError(error)
        }
    }

    return {
        customErrorHandler,
        globalError
    }
}
