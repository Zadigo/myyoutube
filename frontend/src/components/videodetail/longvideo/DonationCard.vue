<template>
  <div class="card mb-2">
    <div class="card-body">
      <h3 class="text-warning">Donation</h3>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis asperiores ullam quas
        suscipit. Distinctio eos numquam expedita quia earum cum veniam vitae nesciunt nobis? Ad
        temporibus reprehenderit rerum velit? Quia?
      </p>
      <div class="d-flex justify-content-between align-items-center">
        <h3 class="fw-bold p-3 bg-primary rounded text-white">$356 000</h3>
        <div class="donators p-3 rounded">
          <div class="users d-flex justify-content-between">
            <div v-for="i in 20" :key="i" class="d-flex flex-column justify-content-between align-items-center mx-2">
              <img src="https://via.placeholder.com/300" width="100" height="100" class="img-thumbnail mt-2" alt="Image 8">
              <p>$300</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
