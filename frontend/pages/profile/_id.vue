<template>
<div>
  <dashboard :title="user.name"></dashboard>
  <div style="background-color: #D2F3F5">
    <v-row justify="space-between">
      <img class="back-icon ml-3" src="/img/back.svg" @click="$router.back()">
      <img class="back-icon mr-3" src="/img/bell.svg">
    </v-row>
    <v-row class="ma-0 pb-5" align="center" justify="space-between">
      <v-btn 
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="ml-10"
      >Edit Profile</v-btn>
      <v-avatar
        color="#55CBD3"
        size="200">
      </v-avatar>
      <v-btn 
        dark
        large
        elevation="0"
        color="#55CBD3"
        class="mr-10"
      >Calendar</v-btn>
    </v-row>
  </div>
  <v-row justify="center" class="mt-6">
    <h3 style="text-align:center">Bio</h3>
    <div class="descri">{{user.description}}</div>
    <v-row justify="center" class="mt-5">
      <v-icon class="material-icons">
        mdi-lock
      </v-icon>
      <div class="lock-text ml-3">Preferred Meeting Location</div>
    </v-row>
  </v-row>
  <v-row cols="12" class="mt-10">
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
                v-for="course in user.courses.slice((index-1)*4, index*4)"
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
                v-for="hobbie in user.hobbies.slice((index-1)*2, index*2)"
                :key="hobbie"
              >{{hobbie}}
              </div>
            </div>
            <div class="mb-10 ml-10" v-else>
              <div
                class="hobbies-tag ma-2 pl-6 pr-6 pt-2 pb-2"
                v-for="hobbie in user.hobbies.slice((index-1)*2, index*2)"
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
export default {
  components: { dashboard },
  data(){
    return{
      cols: 2,
      model: null,
      user:{
        id: 1,
        name: "Noah Fence",
        description: "Hi, my name is Noah and I am currently a second year Computer Science student at UNSW. I like graphic design, accounting and meeting new people!",
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
    }
  },
  method:{

  },
  computed: {
    pages_4 () {
      return Math.ceil(this.user.courses.length/4)
    },
    pages_2 () {
      return Math.ceil(this.user.hobbies.length/2)
    }
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
