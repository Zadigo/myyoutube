import { defineStore } from 'pinia'

const useStudio = defineStore('studio', {
  state: () => ({
    videosToUpload: null,
    previewUrl: null,
    options: {

    }
  })
})

export {
  useStudio
}
