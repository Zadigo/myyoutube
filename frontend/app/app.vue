<template>
  <NuxtLayout>
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { useCreateViewingProfile } from './composables/use/viewing_profile'

useCreateViewingProfile()

const authStore = useAuthenticationStore()
const { accessToken, refreshToken } = storeToRefs(authStore)

const access = useCookie('access')
const refresh = useCookie('refresh')

watch([access, refresh], ([access, refresh]) => {
  authStore.accessToken = access
  authStore.refreshToken = refresh
})

onBeforeMount(async () => {
  if (access.value && refresh.value) {
    accessToken.value = access.value
    refreshToken.value = refresh.value
  }
})
</script>
