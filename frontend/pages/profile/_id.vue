<template>
<div class="mb-10">
  <dashboard :title="userInfo.name" :photo="getUserPhoto"></dashboard>
  <div style="background-color: #D2F3F5">
    <v-row justify="space-between">
      <img class="back-icon ml-3" src="/img/back.svg" @click="$router.back()">
      <img class="back-icon mr-3" src="/img/bell.svg">
    </v-row>
    <v-row class="ma-0 pb-5" align="center" justify="center">
      <v-btn
        v-if="setting==false && userInfo.id == user.id"
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="mr-10"
        @click="setting =!setting"
      >Edit Profile</v-btn>
      <v-btn
        v-else-if="userInfo.id == user.id"
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="mr-10"
        @click="setting = !setting; save()"
      >Save</v-btn>
      <v-avatar
        size="200">
        <img
          :src="getUserInfoPhoto"
        >
      </v-avatar>
      <v-btn
        v-if="userInfo.id == user.id"
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
    <v-row justify="center" v-if="userInfo.id == user.id && setting==true">
      <v-text-field
        class="ml-6 mr-6"
        outlined
        v-model="userInfo.bio"
      >
      </v-text-field>
    </v-row>
    <v-row justify="center" v-else>
      <div class="descri">{{userInfo.bio}}</div>
    </v-row>
    <v-col justify="center" class="mt-6" v-if="setting==true && userInfo.id == user.id">
      <v-row justify="center">
        <div class="lock-text ml-3">Preferred Meeting Location (visible to you only)</div>
      </v-row>
      <v-text-field
        class="mt-5"
        label="Enter the suburb/postcode of your prefferred meeting location"
        outlined
        v-model="userInfo.location"
      >
      </v-text-field>
    </v-col>
    <v-row justify="center" class="mt-6" v-else>
      <v-icon class="material-icons">
        mdi-lock
      </v-icon>
      <div class="lock-text ml-3">Preferred Meeting Location</div>
    </v-row>
  </v-col>
  <v-row cols="12" class="mt-5">
    <v-col cols="6" style="background-color: #A1EEF4">
      <v-row justify="center" class="mb-3">
        <div class="subtitle mt-7">Completed Courses</div>
        <v-dialog
          v-model="dialog"
          width="500"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              v-if="setting==true && userInfo.id == user.id"
              v-on="on"
              v-bind="attrs"
              class="ml-3 mt-7"
              outlined
              icon
            >
              <v-icon>
                mdi-plus
              </v-icon>
            </v-btn>
          </template>
    
          <v-card>
            <v-card-title class="headline grey lighten-2">
              Add Course
            </v-card-title>
    
            <v-card-text>
              <v-text-field
                v-model="newCourse"
              >
              </v-text-field>
            </v-card-text>
    
            <v-divider></v-divider>
    
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="dialog = false; addCourse(newCourse)"
              >
                ADD
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
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
                v-for="course in getCourse.slice((index-1)*4, index*4)"
                :key="course.id"
              >{{course.name}}
                <v-icon
                  class="pb-1"
                  v-if="setting==true"
                >
                  mdi-close
                </v-icon>
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
      <div
        class="mt-5"
        v-for="g in myGroups"
        v-bind:key="g.id"
      >
        <v-row cols="12"
          style="background-color: #5BD1D9"
          class="ml-2 mr-2"
          @click="$router.push(`/group/${g.id}`)"
        >
          <v-col cols="6"
          >
            <v-img
              contain
              :src="getGroupImage(g.photo)"
            />
          </v-col>
          <v-col align-self="center">
            <h3>{{g.room}}: {{g.name}}</h3>
            <p>{{g.descript}}</p>
          </v-col>
        </v-row>
      </div>
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
      let myGroups = await $axios.$get(`student/${params.id}/groups`);
      console.log(myGroups)
      return { userInfo, myGroups };
    } catch (e) {
      return { userInfo: {} };
    }
  },
  data(){
    return{
      newCourse: null,
      dialog: false,
      cols: 2,
      model: null,
      setting: false,
      hobbies: ["play", "sleep", "being lazy", "play", "sleep"]
    }
  },
  methods:{
    goToCalendar() {
      if(this.userInfo.id == this.user.id) {
        this.$router.push(`/profile/calendar/${this.userInfo.id}`)
      }
    },
    getGroupImage(url) {
      var url = url.replace(/^"(.*)"$/, '$1')
      return "http://127.0.0.1:8000/media/" + url
    },
    async addCourse(name) {
      try{
        let res = await this.$axios.$get(`student/${this.user.id}/addcourse/${name}`)
        if (res.name == undefined) {
          alert("Course does not exist")
        }else{
          try{
            this.userInfo = await this.$axios.$get(`/student/` + this.user.id);
          }catch(e) {
            console.log(e)
          }
        }
      }catch(e) {
        console.log(e)
      } 
    },
    async save() {
      try{
        let res = this.$axios.$get(`/student/` + this.user.id + `/location/` + this.userInfo.location)
      }catch(e) {
        console.log(e)
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
    getCourse() {
      return this.userInfo.courses
    }
  },
  mounted() {
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
  font-size: 17px;
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
