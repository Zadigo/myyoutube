import type { Playlist } from '~/types'
import { videoDetailsFixture } from './videos'

export const playlistsFixture: Playlist = {
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
                    id: videoDetailsFixture.id,
                    title: videoDetailsFixture.title,
                    description: videoDetailsFixture.description,
                    videoId: videoDetailsFixture.videoId,
                    userChannel: {
                      id: videoDetailsFixture.userChannel.id,
                      name: videoDetailsFixture.userChannel.name,
                      reference: videoDetailsFixture.userChannel.reference
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
}
