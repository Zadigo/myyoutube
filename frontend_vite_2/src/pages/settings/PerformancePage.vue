<template>
  <section id="algorithm">
    Performance
  </section>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PerformancePage',
  methods: {
    async handleAccountDetails () {
      try {
        const response = await this.$client.get<AxiosResponseData>('/accounts/base')
        this.requestData = response.data
      } catch {
        // Handle error
      }
    }
  }
})
</script>
