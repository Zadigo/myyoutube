import type { Playlist } from '~/types'
import { selectRandomVideo, videoDetailsFixture } from './videos'

const randomVideo = selectRandomVideo()

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
                    id: randomVideo.id,
                    title: randomVideo.title,
                    description: randomVideo.description,
                    videoId: randomVideo.videoId,
                    userChannel: {
                      id: randomVideo.userChannel.id,
                      name: randomVideo.userChannel.name,
                      reference: randomVideo.userChannel.reference
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
