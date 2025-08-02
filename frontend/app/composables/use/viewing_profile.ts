import { doc, setDoc } from 'firebase/firestore'
import { useFirestore } from 'vuefire'

export interface ViewingProfileApiResponse {
  token: string
}

export function useViewingProfile() { 
  const viewingProfileId = useCookie('vp_id')

  return {
    viewingProfileId
  }
}

export function useCreateViewingProfile() {
  const { viewingProfileId } = useViewingProfile()

  const db = useFirestore()

  const { execute } = useAsyncData(async () => {
    // const response =  await $fetch<ViewingProfileApiResponse>('/api/v1/viewing/id', {
    //   method: 'POST',
    //   baseURL: useRuntimeConfig().public.djangoProdUrl,
    // })

    // const vpProfilesDoc = doc($fireStore, 'vp_profiles', viewingProfileId.value)
    // await setDoc(vpProfilesDoc, { id: null, email: null })

    // viewingProfileId.value = response.token

    // return response

    const docRef = doc(db, 'youtube', '11Ugo5hYONkww3FS877T')
    await setDoc(docRef, { vpprofile: '1234-youtube' })

    return '1234-youtube'
  }, {
    immediate: false
  })

  onMounted(async () => {
    if (!viewingProfileId.value) {
      await execute()
    }   
  })

  return {
    viewingProfileId
  }
}
