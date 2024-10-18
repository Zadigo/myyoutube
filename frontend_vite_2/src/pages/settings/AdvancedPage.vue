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

<script lang="ts">
import { CustomUser } from '@/types/authentication';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'AdvancedPage',
  methods: {
    async handleAccountDetails () {
      try {
        const response = await this.$client.get<CustomUser>('/accounts/base')
        this.requestData = response.data
      } catch {
        // Handle error
      }
    }
  }
})
</script>
