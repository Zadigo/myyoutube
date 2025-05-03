<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { doc, setDoc } from 'firebase/firestore'

interface ViewingProfileApiResponse {
  token: string
}

const { $fireStore } = useNuxtApp()
const authStore = useAuthentication()
const { accessToken, refreshToken } = storeToRefs(authStore)

const viewingProfileId = useCookie('vp_id')
const access = useCookie('access')
const refresh = useCookie('refresh')

watch([access, refresh], ([access, refresh]) => {
  authStore.accessToken = access
  authStore.refreshToken = refresh
})

const { execute } = useAsyncData(async () => {
  const response =  await $fetch<ViewingProfileApiResponse>('/api/v1/viewing/id', {
    method: 'GET',
    baseURL: useRuntimeConfig().public.djangoProdUrl,
  })

  const vpProfilesDoc = doc($fireStore, 'vp_profiles', viewingProfileId.value)

  setDoc(vpProfilesDoc, { id: null, email: null })
  viewingProfileId.value = response.token

  return response
}, {
  immediate: false
})

onBeforeMount(async () => {
  if (access.value && refresh.value) {
    accessToken.value = access.value
    refreshToken.value = refresh.value
  }

  if (!viewingProfileId.value) {
    await execute()
  }
})
</script>
