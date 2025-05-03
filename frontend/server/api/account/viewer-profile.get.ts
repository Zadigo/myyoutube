import { createServerDjangoClient } from "~/composables/django_client"
import type { ViewingProfile } from "~/types"

export default defineCachedEventHandler(async event => {
    const access = getCookie(event, 'access')
    const refresh = getCookie(event, 'refresh')
    const client = createServerDjangoClient('/api/v1/accounts', access, refresh, (token) => {
        setCookie(event, 'access', token)
    })
    const response = await client.get<ViewingProfile>('viewing-profile')
    return response.data
}, {
    base: 'redis',
    maxAge: 1
})
