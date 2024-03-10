<template>
  <div class="card shadow-none">
    <div class="card-body">
      <div class="d-flex justify-content-start align-items-start gap-4">
        <img src="/avatar3.png" width="60" height="60" class="img-fluid rounded-circle" alt="">
        <div class="actions" style="width: 100%;">
          <v-text-field type="textarea" variant="outlined"></v-text-field>

          <div class="action-buttons">
            <v-btn color="secondary" size="small" rounded="xl" flat>
              Cancel
            </v-btn>

            <v-btn color="secondary" size="small" rounded="xl" flat>
              <font-awesome-icon icon="fas fa-thumbs-down" class="mr-2" />
            </v-btn>

            <v-btn color="secondary" size="small" rounded="xl" flat>
              <font-awesome-icon icon="fas fa-thumbs-up" class="mr-2" />
              Comment
            </v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
