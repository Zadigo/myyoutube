export default defineNuxtRouteMiddleware(to => {
    const authenticated = useState('authenticated')

    if (to.path.includes('/settings')) {
        if (!authenticated.value) {
            return navigateTo('/login')
        }
    }

    return true
})
