<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-md-5 col-sm-12 offset-md-4">
        <div class="card">
          <div class="card-body">
            <v-form @submit.prevent>
              <v-text-field v-model="requestData.email" type="email" placeholder="Email" variant="solo-filled" flat />
              <v-text-field v-model="requestData.password" type="password" placeholder="Password" variant="solo-filled" flat />
              <v-btn variant="tonal" color="primary" @click="handleLogin">
                Login
              </v-btn>
            </v-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import createClient from '~/composables/client';
import type { LoginApiResponse } from '~/types/authentication';

definePageMeta({
  layout: 'site'
})

const client = createClient('/auth/v1/')

const router = useRouter()
const authStore = useAuthentication()
const accessToken = useCookie('access')
const refreshToken = useCookie('refresh')

const requestData = ref({
  email: null,
  password: null
})

async function handleLogin() {
  try {
    const response = await client.post<LoginApiResponse>('/token/', requestData.value)
    accessToken.value = response.data.access
    refreshToken.value = response.data.refresh
    authStore.accessToken = response.data.access
    authStore.refreshToken = response.data.refresh
    router.push('/')
  } catch {
    // Handle error
  }
}
</script>
