interface Participant {
  fullname: string | null
  url: string | null
  handle: 'Facebook' | 'X' | 'Instagram' | 'YouTube'
}

export interface NewVideo {
  title: string
  description: string
  tags: string[]
  category: string | null
  subcategory: string | null
  channel_playlist: string | null,
  publication: {
    language: string | null,
    publication_time: string | null, // ISO 8601 format
    publication_date: string | null // ISO 8601 format
    recording_location: string | null
  },
  teaser: File | null,
  visibility: {
    public: boolean,
    subscribers_only: boolean,
    is_premiere: boolean,
    panelize: boolean,
    age_restricted: boolean
  },
  files: File[]
  has_paid_promotion: boolean
  participants: Participant[]
}

export const useStudioStore = defineStore('studio', () => {
  const newVideo = ref<NewVideo>({
    title: '',
    description: '',
    tags: [],
    category: null,
    subcategory: null,
    files: [],
    has_paid_promotion: false,
    // video: null,
    publication: {
      language: null,
      publication_time: null, // ISO 8601 format
      publication_date: null, // ISO 8601 format
      recording_location: null
    },
    channel_playlist: null,
    teaser: null,
    visibility: {
      public: true,
      subscribers_only: false,
      is_premiere: false,
      panelize: false,
      age_restricted: false
    },
    participants: []
  })

  const hasCategory = computed(() => {
    return newVideo.value.category !== null
  })

  function submit() {
    const form = new FormData()
    // TODO: Allow uploading of multiple videos
    form.append('video', newVideo.value.files[0])
    form.append('title', newVideo.value.title)
    form.append('description', newVideo.value.description || '')
    form.append('channel_playlist', newVideo.value.channel_playlist || '')
    form.append('recording_location', newVideo.value.recording_location || '')
    form.append('visibility', newVideo.value.visibility ? 'true' : 'false')

    if (newVideo.value.category) {
      form.append('category', newVideo.value.category)
    }

    if (newVideo.value.subcategory) {
      form.append('subcategory', newVideo.value.subcategory)
    }

    if (newVideo.value.visibility.age_restricted) {
      form.append('age_restricted', 'true')
    }

    if (newVideo.value.tags.length > 0) {
      form.append('tags', JSON.stringify(newVideo.value.tags))
    }

    useAsyncData('/videos/studio/upload', () => {
      return $fetch('/videos/studio/upload', {
          baseURL: useRuntimeConfig().public.djangoProdUrl,
          method: 'POST',
          body: form,
      })
    })
  }

  return {
    submit,
    hasCategory,
    newVideo
  }
})
