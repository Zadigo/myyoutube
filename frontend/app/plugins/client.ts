// export default defineNuxtPlugin(async nuxtApp => {
//   const access = useCookie('access')
//   const refresh = useCookie('refresh')

//   console.log('access/refresh', access.value, refresh.value)

//   const client = $fetch.create({
//     baseURL: useRuntimeConfig().public.djangoProdUrl,
//     onRequest({ request, options, error }) {
//       console.log('Authorization', access ? `Token ${access.value}` : '')
//       options.headers.set('Content-Type', 'application/json')
//       if (access.value) {
//         options.headers.set('Authorization', `Token ${access.value}`)
//       }
//     },
//     async onResponseError({ response }) {
//       if (response.status === 401) {
//         access.value = null

//         if (refresh.value) {
//           const { access: newAccess } = await refreshAccessToken(refresh.value)
//           console.log('onResponseError', newAccess)
//           access.value = newAccess
//         } else {
//           refresh.value = null
//           await nuxtApp.runWithContext(() => navigateTo('/'))
//         }
//       }
//     }
//   })

//   return {
//     provide: {
//       client
//     }
//   }
// })

export default defineNuxtPlugin(async _nuxtApp => {
  const videoesClient = $fetch.create({
    baseURL: useRuntimeConfig().public.videosGraphqlUrl
  })

  const moderationClient = $fetch.create({
    baseURL: useRuntimeConfig().public.moderationGraphqlUrl
  })

  return {
    provide: {
      videosGraphqlClient: videoesClient,
      moderationGraphqlClient: moderationClient
    }
  }
})
