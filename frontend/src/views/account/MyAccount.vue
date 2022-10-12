<template>
  <section id="account">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <base-template-card class="mb-2">
            <div class="card-body">
              <h2>{{ $t('manage_appearance', { platform: 'YouTube' }) }}</h2>
            </div>
          </base-template-card>

          <base-card :title="$t('Membership')" class="mb-2">
            <template #body>
              <h3 class="my-3">{{ $t('No subscriptions') }}</h3>
              <button type="button" class="btn btn-primary">
                {{ $t('Get subscription') }}
              </button>
            </template>
          </base-card>
          
          <base-template-card class="mb-2">
            <div class="card-body">
              <base-checkbox id="dark-mode" :label="$t('Use dark mode')" :is-switch="true" :update:initial="handleDarkmode" />
            </div>
          </base-template-card>

          <base-card :title="$t('Your YouTube channel', { platform: 'YouTube' })" class="mb-2">
            <template #body>
              <!-- <p class="text-muted">Your channels</p> -->
              <div class="list-group my-2">
                <router-link v-for="i in 3" :key="i" :to="{ name: 'channel_view' }" class="list-group-item list-group-item-action" href @click.prevent>
                  <div class="d-flex align-items-center">
                    <img :src="require('@/assets/avatar1.png')" class="img-thumbnail" height="50" width="50" alt="">
                    <p class="mx-3">
                      Channel name {{ i }}
                    </p>
                  </div>
                </router-link>
              </div>

              <button type="button" class="btn btn-primary">
                {{ $t('Create') }}
              </button>
            </template>
          </base-card>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseTemplateCard from '@/layouts/bootstrap/cards/BaseTemplateCard.vue'

export default {
  name: 'MyAccount',
  components: {
    BaseCard,
    BaseCheckbox,
    BaseTemplateCard,
  },
  methods: {
    handleDarkmode (value) {
      this.$localstorage.create('darkMode', value)
    }
  }
}
</script>
