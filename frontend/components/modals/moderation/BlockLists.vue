<template>
  <v-dialog v-model="showBlockLists" width="900" scrollable>
    <v-card>
      <v-card-item>
        <h2 class="h4">
          Block lists
        </h2>
      </v-card-item>
      
      <v-card-text>
        <v-text-field variant="solo-filled" placeholder="Search by list names..." flat />
        
        <div class="d-flex gap-2 mb-3">
          <v-btn :disabled="!showBlockedItems" color="dark" variant="tonal" rounded @click="showBlockedItems=false">
            <font-awesome icon="arrow-left" />
          </v-btn>

          <v-btn :disabled="!showBlockedItems" class="mb-3" color="dark" variant="tonal" rounded>
            Use this list
          </v-btn>
          
          <v-btn class="mb-3" color="dark" variant="tonal" rounded @click="showCreateList=true">
            Create my list
          </v-btn>
        </div>
        
        <div v-if="showBlockedItems" class="list-group">
          <div class="list-group-item">
            Something
          </div>
        </div>

        <div v-else class="list-group">
          <a v-for="i in 15" :key="i" href="#" class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" @click.prevent="showBlockedItems=true">
            <span>Utilisateurs Hitchens</span>
            
            <div class="popularity">
              <font-awesome v-for="x in 10" :key="x" icon="star" />
            </div>
          </a>
        </div>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
