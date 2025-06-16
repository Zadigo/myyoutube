<template>
  <v-dialog v-model="showCreateList" :persistent="true" width="400">
    <v-card>
      <v-card-item>
        <h2 class="h4">
          New list
        </h2>
      </v-card-item>

      <v-card-text>
        <VoltInputText  placeholder="Name of your list" flat />
        <VoltInputText  placeholder="Search for users..." flat />
      </v-card-text>
      
      <v-card-actions>
        <v-btn variant="tonal" @click="showCreateList=false">
          Cancel
        </v-btn>

        <v-btn variant="tonal" @click="showCreateList=false">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
