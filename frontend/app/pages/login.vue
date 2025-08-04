<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-md-5 col-sm-12 offset-md-4">
        <div class="card">
          <div class="card-body">
            <form @submit.prevent>
              <VoltInputText v-model="email" type="email" placeholder="Email" />
              <VoltInputText v-model="password" type="password" placeholder="Password" />
              <VoltButton variant="tonal" color="primary" @click="handleLogin">
                Login
              </VoltButton>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

definePageMeta({
  layout: 'site'
})

const authenticated = useState('authenticated')
const router = useRouter()
const authStore = useAuthentication()
const access = useCookie('access')
const refresh = useCookie('refresh')

const email = ref<string>('')
const password = ref<string>('')

async function handleLogin() {
  try {
    const response =  await login(email.value, password.value)

    access.value = response.access
    refresh.value = response.refresh
    
    authStore.accessToken = response.access
    authStore.refreshToken = response.refresh

    authenticated.value = true

    router.push('/')
  } catch {
    // Handle error
  }
}
</script>
