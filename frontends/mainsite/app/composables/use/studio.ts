export const useNewVideoComposable = createSharedComposable(() => {
  const newVideo = ref<NewVideoRequestData>({
    title: '',
    description: '',
    tags: [],
    category: null,
    subcategory: null,
    files: [],
    has_paid_promotion: false,
    // video: null,
    publication: {
      language: '',
      publication_time: '', // ISO 8601 format
      publication_date: '', // ISO 8601 format
      recording_location: ''
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
    monetization: {
      ads: false,
      gifts: false
    },
    participants: []
  })

  function submit() {
    const form = new FormData()
    const file = newVideo.value.files[0]
    form.append('video', file, file?.name || '')
    form.append('title', newVideo.value.title)
    form.append('description', newVideo.value.description || '')
    form.append('channel_playlist', newVideo.value.channel_playlist || '')
    form.append('publication_time', newVideo.value.publication.publication_time || '')
    form.append('publication_date', newVideo.value.publication.publication_date || '')
    form.append('recording_location', newVideo.value.publication.recording_location || '')
    form.append('visibility', JSON.stringify(newVideo.value.visibility))
    form.append('has_paid_promotion', newVideo.value.has_paid_promotion ? 'true' : 'false')
    form.append('monetization', JSON.stringify(newVideo.value.monetization))
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

    return $fetch('/api/studio/upload', {
        baseURL: useRuntimeConfig().public.djangoProdUrl,
        method: 'POST',
        body: form
    })
  }

  function addParticipant() {
    newVideo.value.participants.push({
      fullname: '',
      url: '',
      handle: 'Instagram'
    })
  }

  function removeParticipant(index: number) {
    newVideo.value.participants.splice(index, 1)
  }

  return {
    newVideo,
    submit,
    addParticipant,
    removeParticipant
  }
})
