<template>
  <div class="card">
    <div class="card-body">
      <h4>Visibility</h4>
      <p class="text-muted">Choose when to publish and who can see your video</p>
      <div class="form-check">
        <input id="public" class="form-check-input" type="radio" name="visibility" checked>
        <label class="form-check-label" for="public">
          Public
        </label>
      </div>
      <div class="form-check">
        <input id="private" class="form-check-input" type="radio" name="visibility">
        <label class="form-check-label" for="private">
          Private
        </label>
      </div>
    </div>

    <div class="card-footer">
      <button type="button" class="btn btn-lg btn-primary" @click="$emit('cancel')">
        Cancel
      </button>

      <button type="button" class="btn btn-lg btn-primary" @click="$emit('next')">
        Next
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoVisibility',
  emits: {
    'cancel': () => true,
    'next': () => true
  },
}
</script>

<style scoped>

</style>
