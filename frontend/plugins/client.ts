import createClient from '~/composables/django_client'

export default defineNuxtPlugin(_nuxtApp => {
    const client = createClient('/api/v1/')
    
    return {
        provide: {
            client
        }
    }
})
