<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<script lang="ts" setup>
const authStore = useAuthentication()
const { accessToken, refreshToken } = storeToRefs(authStore)

const access = useCookie('access')
const refresh = useCookie('refresh')

authStore.$subscribe(({ storeId }) => {
  if (storeId === 'authentication') {
    accessToken.value = access.value
    refreshToken.value = refresh.value
  }
})

onBeforeMount(() => {
  accessToken.value = access.value
  refreshToken.value = refresh.value
})
</script>
