<template>
  <section id="account">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8 offset-md-2">
          <base-template-card>
            <div class="card-body">
              <h2>{{ $t('manage_appearance', { platform: 'YouTube' }) }}</h2>
            </div>
          </base-template-card>

          <base-card class="my-2">
            <template #header>
              <h3>{{ $t('Account type') }}</h3>
              <p class="m-0 text-muted">{{ $t('Manage what you share on X', { platform: 'YouTube'}) }}</p>
            </template>

            <template #body>
              <p class="alert alert-info">Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem, nam. Quibusdam numquam doloremque temporibus molestiae saepe id quae, incidunt excepturi beatae, blanditiis optio repudiandae debitis exercitationem, impedit earum ipsa veritatis?</p>
              <base-checkbox id="account-type" is-switch label="My account is professional" />
  
              <base-list-group-item-radio id="account-selection" :items="[{ name: 'Artist'}, {name: 'Association'}, {name: 'Corporate'}]" class="mt-4" />
            </template>
          </base-card>

          <!-- Membership -->
          <base-card class="mb-2">
            <template #header>
              <h3>{{ $t('Membership') }}</h3>
              <p class="m-0 text-muted">{{ $t('Manage what you share on X', { platform: 'YouTube'}) }}</p>
            </template>

            <template #body>
              <h3 class="my-3">{{ $t('No subscriptions') }}</h3>
              <button type="button" class="btn btn-primary">
                {{ $t('Get subscription') }}
              </button>
            </template>
          </base-card>
          
          <!-- Dark mode -->
          <base-template-card class="my-2">
            <div class="card-body">
              <base-checkbox id="dark-mode" :label="$t('Use dark mode')" :is-switch="true" :update:initial="handleDarkmode" />
            </div>
          </base-template-card>

          <!-- Channels -->
          <base-card>
            <template #header>
              <h3 class="my-3">{{ $t('Your YouTube channel', { platform: 'YouTube' }) }}</h3>
              <p class="m-0 text-muted">{{ $t('Manage what you share on X', { platform: 'YouTube'}) }}</p>
            </template>

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
import BaseListGroupItemRadio from '@/layouts/bootstrap/listgroups/BaseListGroupItemRadio.vue'

export default {
  name: 'MyAccount',
  components: {
    BaseCard,
    BaseCheckbox,
    BaseListGroupItemRadio,
    BaseTemplateCard
  },
  methods: {
    handleDarkmode (value) {
      this.$localstorage.create('darkMode', value)
    }
  }
}
</script>
