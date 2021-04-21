<template>
<div class="mb-10">
  <dashboard :title="user.name" :photo="getUserPhoto"></dashboard>
  <div style="background-color: #D2F3F5">
    <v-row justify="space-between">
      <img class="back-icon ml-3" src="/img/back.svg" @click="$router.back()">
      <img class="back-icon mr-3" src="/img/bell.svg">
    </v-row>
    <v-row class="ma-0 pb-5" align="center" justify="center">
      <v-btn 
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="mr-10"
      >Edit Profile</v-btn>
      <v-avatar
        size="200">
        <img
          :src="getUserInfoPhoto"
        >
      </v-avatar>
      <v-btn 
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="ml-10"
        @click="goToCalendar()"
      >Calendar</v-btn>
    </v-row>
  </div>
  <v-col justify="center" class="mt-6">
    <v-row justify="center">
      <h3 style="text-align:center">Bio</h3>
    </v-row>
    <v-row justify="center">
      <div class="descri">{{userInfo.bio}}</div>
    </v-row>
    <v-row justify="center" class="mt-6">
      <v-icon class="material-icons">
        mdi-lock
      </v-icon>
      <div class="lock-text ml-3">Preferred Meeting Location</div>
    </v-row>
  </v-col>
  <v-row cols="12" class="mt-5">
    <v-col cols="6" style="background-color: #A1EEF4">
      <div class="subtitle mt-4">Completed Courses</div>
      <v-sheet
        style="background-color: #A1EEF4"
        class="mx-auto mb-10 pl-6"
        elevation="0"
        height="200"
      >
        <v-slide-group
          v-model="model"
          class="pa"
          active-class="success"
          show-arrows="always"
        >
          <v-slide-item
            v-for="index in (0, pages_4)"
            :key="index"
          >
            <div class="mb-10">
              <div
                class="course-tag ma-2 pl-6 pr-6 pt-2 pb-2"
                v-for="course in userInfo.courses.slice((index-1)*4, index*4)"
                :key="course.id"
              >{{course.name}}
              </div>
            </div>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
      <div class="subtitle">Interests and Hobbies</div>
      <v-sheet
        style="background-color: #A1EEF4"
        class="pl-6 mt-2"
        elevation="0"
        height="200"
      >
        <v-slide-group
          v-model="model"
          class="pa"
          show-arrows
        >
          <v-slide-item
            v-for="index in (0, pages_2)"
            :key="index"
          >
            <div class="mb-10" v-if="pages_2 > 2">
              <div
                class="hobbies-tag ma-2 pl-6 pr-6 pt-2 pb-2"
                v-for="hobbie in hobbies.slice((index-1)*2, index*2)"
                :key="hobbie"
              >{{hobbie}}
              </div>
            </div>
            <div class="mb-10 ml-10" v-else>
              <div
                class="hobbies-tag ma-2 pl-6 pr-6 pt-2 pb-2"
                v-for="hobbie in hobbies.slice((index-1)*2, index*2)"
                :key="hobbie"
              >{{hobbie}}
              </div>
            </div>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </v-col>
    <v-col cols="6" style="background-color: #D2F3F5">
      <div class="subtitle mt-4">Active Groups</div>
    </v-col>
  </v-row>
</div>
</template>



<script>
import dashboard from '../../components/dashboard'
import { mapState } from "vuex"

export default {
  components: { dashboard },
  async asyncData({ $axios, params }) {
    try {
      let userInfo = await $axios.$get(`/student/` + params.id);
      console.log(userInfo)
      return { userInfo };
    } catch (e) {
      return { userInfo: {} };
    }
  },
  data(){
    return{
      cols: 2,
      model: null,
      courses: [
        {id: 1, name: 'COMP1511'},
        {id: 2, name: 'COMP1512'},
        {id: 3, name: 'COMP1513'},
        {id: 4, name: 'COMP1514'},
        {id: 5, name: 'COMP1515'},
        {id: 6, name: 'COMP1516'},
        {id: 7, name: 'COMP1517'},
        {id: 8, name: 'COMP1520'},
        {id: 9, name: 'COMP1522'},
        {id: 10, name: 'COMP1533'},
      ],
      hobbies: ["play", "sleep", "being lazy", "play", "sleep"]
    }
  },
  methods:{
    getUserPhoto(url) {
      return "http://localhost:8000" + url
    },
    goToCalendar() {
      if(this.userInfo.id == this.user.id) {
        this.$router.push(`/profile/calendar/${this.userInfo.id}`)
      }
    }
  },
  computed: {
    pages_4 () {
      return Math.ceil(this.userInfo.courses.length/4)
    },
    pages_2 () {
      return Math.ceil(this.hobbies.length/2)
    },
    ...mapState(['user']),
    getUserPhoto() {
      return "http://localhost:8000" + this.user.photo
    },
    getUserInfoPhoto() {
      console.log( "http://localhost:8000" + this.userInfo.photo)
      return "http://localhost:8000" + this.userInfo.photo
    },
  },
  mounted() {
    // this.getUserPhoto()
  }
}
</script>
<style lang="scss" scoped>
.back-icon{
  width: 50px;
}
.descri{
  text-align: center;
}
.lock-text{
  font-weight: bold;
  color: grey;
}
.subtitle{
  text-align: center;
  font-weight: bold;
  font-size: 25px;
  color: #55CBD3;
}
.course-tag{
  font-size: 18px;
  background-color: white;
  text-align: center;
  width: 148px;
}
.hobbies-tag{
  font-size: 18px;
  background-color: white;
  text-align: center;
  width: 148px;
}
</style>
