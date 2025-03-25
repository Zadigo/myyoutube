import { useAxiosClient } from "~/composables/django_client"
import type { Playlist } from "~/types"

export default defineEventHandler(async (event) => {
    try {
        // const client = createDjangoClient('/api/v1/')
        const { client } = useAxiosClient()
        const response = await client.get<Playlist[]>('playlists')
        return response.data
    } catch {
        return {}
    }
})
