import { createServerDjangoClient } from "~/composables/django_client"
import type { Playlist } from "~/types"

export default defineEventHandler(async (event) => {
    try {
        const access = getCookie(event, 'access')
        const refresh = getCookie(event, 'refresh')
        const client = createServerDjangoClient('/api/v1/', access, refresh, (token) => {
            setCookie(event, 'access', token)
        })
        const response = await client.get<Playlist[]>('playlists')
        return response.data
    } catch (e) {
        console.error(e)
        return {}
    }
})
