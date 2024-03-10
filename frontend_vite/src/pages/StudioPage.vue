<template>
  <section id="studio">
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
            <div class="d-flex justify-content-between gap-4 align-items-center">
              <div class="actions">
                <v-btn color="primary" rounded="xl">
                  <font-awesome-icon :icon="['fas', 'fa-upload']" class="me-2" />
                  Upload
                </v-btn>

                <v-btn color="primary" rounded="xl">
                  <font-awesome-icon :icon="['fas', 'fa-chart-simple']" class="me-2" />
                  Statistics
                </v-btn>
              </div>

              <v-text-field variant="outlined" style="width:40%;"></v-text-field>
            </div>
          </div>

          <div class="card-body">
            <div class="list-group">
              <article v-for="i in 5" :key="i" class="list-group-item list-group-item-action p-4 d-flex gap-4 justify-content-left align-items-center" aria-label="">
                <img src="https://via.placeholder.com/100x100" class="img-fluid rounded" alt="">
                
                <div class="infos p-2 mx-1 flex-shrink-1">
                  <h5>Quick title</h5>
                  <p class="mb-2"> Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ratione error alias voluptatibus doloremque adipisci, inventore quas? Ipsum commodi </p>
                  <p class="d-flex justify-content-left text-muted"><span>4456 vues</span> - <span class="mx-2">400 likes</span></p>
                </div>

                <div class="actions">
                  <v-btn color="primary" rounded="xl">
                    <font-awesome-icon :icon="['fas', 'fa-pen']" />
                  </v-btn>
                  
                  <v-btn color="primary" rounded="xl">
                    <font-awesome-icon :icon="['fas', 'fa-ellipsis-vertical']" />

                  </v-btn>
                </div>
              </article>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
