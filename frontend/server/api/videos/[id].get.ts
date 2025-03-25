import { useAxiosClient } from "~/composables/django_client"
import type { VideosFeedResponseData } from "~/types"

export default defineEventHandler(async event => {
    const query = getQuery(event)

    const { client } = useAxiosClient()
    const response = await client.get<VideosFeedResponseData>('/videos', {
        params: {
            q: query.search
        }
    })

    return response.data
})
