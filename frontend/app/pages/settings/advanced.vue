<template>
  <section id="algorithm">
    <div class="card">
      <div class="card-body">
        <VoltInputOtp :length="4" />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
// import type { CustomUser } from '@/types';

definePageMeta({
  layout: 'settings'
})

// const { client } = useAxiosClient()

// const requestData = ref()

// async function handleAccountDetails () {
//   try {
//     const response = await client.get<CustomUser>('/accounts/base')
//     requestData.value = response.data
//   } catch {
//     // Handle error
//   }
// }
</script>
