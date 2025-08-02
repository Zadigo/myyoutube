<template>
  <section id="algorithm">
    <div class="row">
      <div class="col-8 offset-md-2">
        <div class="card">
          <div class="card-body">
            <v-otp-input :length="4" />
          </div>
        </div>
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
