<template>
  <div class="container">
    <div class="row my-5">
      <div class="col-md-5 col-sm-12 offset-md-4">
        <div class="card">
          <div class="card-body">
            <v-form>
              <v-text-field v-model="requestData.email" type="email" variant="solo-filled" flat />
              <v-text-field v-model="requestData.password" type="password" variant="solo-filled" flat />
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

<script lang="ts">
import { useAuthentication } from '@/store/authentication';
import { storeToRefs } from 'pinia';
import { defineComponent, ref } from 'vue';
import { LoginResponse } from '@/types/authentication'

export default defineComponent({
  name: 'LoginPage',
  setup() {
    const store = useAuthentication()
    const { accessToken, refreshToken } = storeToRefs(store)
    const requestData = ref({
      email: null,
      password: null
    })
    return {
      accessToken,
      refreshToken,
      requestData
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await this.$authClient.post<LoginResponse>('/token/', this.requestData)
        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        this.$session.create('authentication', response.data)
        this.$router.push({ name: 'feed' })
      } catch {
        // Handle error
      }
    }
  }
})
</script>
