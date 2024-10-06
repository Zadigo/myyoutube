<template>
  <div class="card-body">
    <h4>Age restriction</h4>
    <p class="text-muted">Choose when to publish and who can see your video</p>
    
    <v-checkbox label="Age restricted"></v-checkbox>

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
</template>

<script>
export default {
  name: 'VideoVisiblityComponent'
}
</script>
