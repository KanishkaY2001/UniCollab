<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>Student List</h3>
        </div>
      </div>
      <template v-for="student in students">
        <div :key="student.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <student-card :student="student" :onDelete="deleteStudent"></student-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>
import studentCard from "~/components/studentCard.vue";

const sampleData = [
  {
    id: 1,
    name: "Jollof Rice",
  },
  {
    id: 2,
    name: "Macaroni",
  },
  {
    id: 3,
    name: "Fried Rice",
  }
];

export default {
  created() {

  },
  head() {
    return {
      title: "Student list"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let students = await $axios.$get(`/students/`);
      return { students };
    } catch (e) {
      return { students: [] };
    }
  },
  components: {
    studentCard
  },
  data() {
    return {
      students: []
    };
  },
  methods: {
    async deleteStudent(id) {
      try {
        await this.$axios.$delete(`/students/${id}/`); // delete recipe
        let newStudent = await this.$axios.$get("/students/"); // get new list of recipes
        this.students = newStudent; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>