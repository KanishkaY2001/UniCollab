<template>
  <div class="card recipe-card">
    <div class="card-body">
      <h5 class="card-title">{{ student.name }}</h5>
      <div class="action-buttons">
        <v-btn :to="`/students/${student.id}/`" class="btn btn-sm btn-success"> View </v-btn>
        <v-btn :to="`/students/${student.id}/edit/`" class="btn btn-sm btn-primary"> Edit </v-btn>
        <button @click="onDelete(student.id)"  class="btn btn-sm btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    props: ["student", "onDelete"]
};
</script>
<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>