import { createErrorTemplate } from '#shared/errors'

export default defineEventHandler(async (_event) => {
  const { singleItem } = useLoadFixtures()
  const video = singleItem()

  try {
    return {
      data: {
        allplaylists: {
          edges: [
            {
              node: {
                id: 'UGxheWxpc3Q6NA==',
                playlistId: '4',
                isIntelligent: false,
                name: 'Kendall Jenner',
                description: 'My kendall Jenner playlist',
                visibility: 'Public',
                createdOn: '2025-03-25T23:34:17.619177Z',
                videos: {
                  edges: [
                    {
                      node: {
                        id: video?.id,
                        title: video?.title,
                        description: video?.description,
                        videoId: video?.videoId,
                        userChannel: {
                          id: video?.userChannel.id,
                          name: video?.userChannel.name,
                          reference: video?.userChannel.reference
                        }
                      }
                    }
                  ]
                }
              }
            },
            {
              node: {
                id: 'UGxheWxpc3Q6NQ==',
                playlistId: '5',
                isIntelligent: false,
                name: 'Photoshop',
                description: 'My photoshop playlist',
                visibility: 'Public',
                createdOn: '2025-03-25T23:36:35.412430Z',
                videos: {
                  edges: []
                }
              }
            }
          ]
        }
      }
    } as Playlist
  } catch (error) {
    const template = createErrorTemplate(error)
    return createError(template)
  }
})
