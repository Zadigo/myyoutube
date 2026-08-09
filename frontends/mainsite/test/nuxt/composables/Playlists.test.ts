import { describe, it, expect, beforeEach, vi, afterEach } from 'vitest'
import { useEditPlaylists, useCreatePlaylist, usePlaylistsComposable } from '../../../app/composables'

const mockFetch = vi.fn(async (url: string, options: { method: string; body?: unknown }) => {
  if (url.includes('/playlists/') && options.method === 'POST') return { success: true }

  throw new Error(`Unexpected fetch call: ${url} with method ${options.method}`)
})

vi.stubGlobal('$fetch', mockFetch)

describe.todo('useEditPlaylists', () => {
  beforeEach(() => {
    vi.stubEnv('server', 'false')
  })

  afterEach(() => {
    vi.unstubAllEnvs()
  })

  it('should return all default values', () => {
    const result = useEditPlaylists([])
    expect(result).toBeDefined()

    expect(result.add).toBeDefined()
    expect(result.remove).toBeDefined()

    expect(result.add).toBeInstanceOf(Function)
    expect(result.remove).toBeInstanceOf(Function)
  })

  it('should call $fetch when add is called', async () => {
    const result = useEditPlaylists([])
    await result.add('playlistId', 'videoId')

    expect(mockFetch).toHaveBeenCalledWith('/playlists/playlistId/add', expect.objectContaining({
      method: 'POST',
      body: { video_id: 'videoId' }
    }))
  })
})

describe.todo('useCreatePlaylist', () => {
  it ('should return all default values', () => {
    const result = useCreatePlaylist([])
    expect(result).toBeDefined()
  })
})

describe.todo('usePlaylistsComposable', () => {
  it('should return all default values', () => {
    const result = usePlaylistsComposable()
    expect(result).toBeDefined()
  })
})
