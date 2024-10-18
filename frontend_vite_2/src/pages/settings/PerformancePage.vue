<template>
  <section id="algorithm">
    Performance
  </section>
</template>

<script lang="ts">
import { CustomUser } from '@/types/authentication';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PerformancePage',
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
