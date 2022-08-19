<template>
  <section id="algorithm">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12 col-md-8">
          <div class="card">
            <div class="card-body">
              <p class="alert alert-info">
                If no options are selected, YouTube will use your viewing history
                to recommend the most relevant videos
              </p>
              <div class="form-check form-switch my-4">
                <input id="recommendation-preference" class="form-check-input" type="checkbox" role="switch" />
                <label class="form-check-label" for="recommendation-preference">
                  Let YouTube decide which are the most relevant videos for me
                </label>
              </div>

              <div class="card shadow-none">
                <div class="card-body">
                  <label for="categories">Select the categories for which you will have the most interest</label>
                  <input type="text" class="form-control p-2" placeholder="Categories" name="categories">
                  <input type="text" class="form-control p-2 my-2" placeholder="Subcategories" name="subcategories" disabled>

                  <div class="list-group list-group-flush">
                    <div class="list-group-item ps-0">
                      <div class="form-check form-switch">
                        <input id="recommend-from-current" class="form-check-input" type="checkbox" role="switch" />
                        <label class="form-check-label" for="recommend-from-current">
                          Let YouTube recommend the most popular videos from what
                          users have also watched based on the video that you
                          are currently viewing
                        </label>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-12 col-md-4">
          <div class="card">
            <div class="card-header">
              <h3>Preferred categories</h3>
            </div>

            <div class="card-body">
              <h4 class="fw-bold h5 mb-1">Sports</h4>
              <div class="list-group my-3">
                <a class="list-group-item list-group-item-action d-flex justify-content-between">
                  <span>WNBA</span>
                  <button type="button" class="btn btn-sm btn-rounded btn-dark shadow-none">
                    <font-awesome-icon icon="fa-solid fa-trash"></font-awesome-icon>
                  </button>
                </a>
              </div>
            </div>

            <div class="card-footer text-right">
              <button type="button" class="btn btn-danger">
                <font-awesome-icon icon="fa-solid fa-eraser"></font-awesome-icon>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
