<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-md-5 col-sm-12 offset-md-4">
        <div class="card">
          <div class="card-body">
            <form @submit.prevent>
              <u-input-text v-model="usernameField" type="email" placeholder="Email" />
              <u-input-text v-model="password" type="password" placeholder="Password" />
              <u-button color="primary" @click="handleLogin">
                Login
              </u-button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'site'
})

const router = useRouter()
const { login, usernameField, password } = useLogin('email')

async function handleLogin() {
  await login(() => {
    router.push('/')
  })
}
</script>
