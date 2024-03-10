<template>
  <div class="col-12">
    <div class="card">
      <div class="card-body">
        <h1 class="h4">When you realize ON AIR that your sister stole your watch</h1>
        <div class="d-flex justify-content-between align-items-center mt-3">
          <div id="left" class="d-flex justify-content-left gap-4">
            <img src="/avatar1.png" class="img-fluid rounded-circle" width="50" height="50" alt="">
            <h3 class="h6">User name</h3>
          </div>

          <div id="right">
            <v-btn size="large" rounded="xl" color="primary" class="me-1" flat>
              <!-- <v-icon name="fa:fas fa-thumbs-down" class="me-3"></v-icon> -->
              <font-awesome-icon icon="fas fa-thumbs-up" class="mr-2" />
              Like
            </v-btn>

            <v-btn size="large" rounded="xl" color="primary" class="me-3" flat>
              <!-- <v-icon name="fa:fas fa-thumbs-down" class="me-3"></v-icon> -->
              <font-awesome-icon icon="fas fa-thumbs-down" class="mr-2" />
              Dislike
            </v-btn>

            <v-menu>
              <template v-slot:activator="{ props }">
                <v-btn size="large" rounded="xl" v-bind="props" color="primary" flat>
                  <font-awesome-icon icon="fas fa-caret-down" class="mr-2" />
                  More
                </v-btn>
              </template>

              <v-list>
                <v-list-item v-for="menuItem in menuItems" :key="menuItem.name" :value="menuItem" @click="handleMoreAction(menuItem)">
                  <v-list-item-title>{{ menuItem.name }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>

            <v-btn size="large" rounded="xl" color="secondary" class="ml-5" flat>
              Subscribe
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const menuItems = [
  {
    name: 'Store'
  },
  {
    name: 'Download'
  },
  {
    name: 'Save'
  },
  {
    name: 'Gift'
  },
  {
    name: 'Donate'
  },
  {
    name: 'Share'
  },
  {
    name: 'Recommendations'
  },
  {
    name: 'Report'
  }
]

export default {
  name: 'UserVideoActions',
  setup () {
    return {
      menuItems
    }
  },
  methods: {
    handleMoreAction (action) {
      console.log(action)
    }
  }
}
</script>
