import createClient from '~/composables/client'

export default defineNuxtPlugin(_nuxtApp => {
    const client = createClient('/api/v1/')
    
    return {
        provide: {
            client
        }
    }
})
