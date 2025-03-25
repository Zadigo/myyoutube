<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { doc, getFirestore, setDoc } from 'firebase/firestore'
// import { getAnalytics } from "firebase/analytics";

interface ViewingProfileApiResponse {
  token: string
}

// const { $app } = useNuxtApp()
const authStore = useAuthentication()
const { accessToken, refreshToken } = storeToRefs(authStore)

const db = getFirestore()
// const analytics = getAnalytics($app)

const viewingProfileId = useCookie('vp_id')
const access = useCookie('access')
const refresh = useCookie('refresh')

authStore.$subscribe((_, state) => {
  // accessToken.value = access.value
  // refreshToken.value = refresh.value
  access.value = state.accessToken
  refresh.value = state.refreshToken
})

async function requestViewingProfileId() {
  const client = createAxiosSimpleClient('/api/v1/viewing/')

  if (!viewingProfileId.value) {
    const response = await client.post<ViewingProfileApiResponse>('/id')
    viewingProfileId.value = response.data.token

    const vpProfilesDoc = doc(db, 'vp_profiles', viewingProfileId.value)
    setDoc(vpProfilesDoc, { id: null, email: null })
  }
}

onBeforeMount(async () => {
  if (access.value && refresh.value) {
    accessToken.value = access.value
    refreshToken.value = refresh.value
  }

  await requestViewingProfileId()
})
</script>
