<template>
<div>
  <dashboard :title="getRoomName(group.room)" :photo="getUserPhoto()"></dashboard>
  <div class="frame pb-10 mb-10">
    <v-row class="mt-10" cols="12" justify="space-between">
      <img class="back-icon ml-3" src="/img/back.svg" @click="$router.back()">
      <v-col cols="8">
        <div class="group-name ml-5">{{group.name}}</div>
      </v-col>
      <img class="back-icon mr-4" src="/img/bell.svg">
    </v-row>
    <v-divider class="mt-3"></v-divider>
    <v-row class="group-info" cols="12" justify="center">
      <v-col cols="10">
        <v-row>
          <v-img class="ml-3 mt-7" style="width: 170px; height: 115px" :src="getImageURL()"/>
          <v-col cols="7" class="pt-8 ml-7">
            <div style="background-color: white; border-radius: 10px; height: 100px" class="pl-4 pt-2">
              <div style="color: #55CBD3; font-size: 20px">About us</div>
              <div style="font-size: 16px; color: #646868">
                {{group.descript}}
              </div>
            </div>
          </v-col>
          <!-- <v-btn dark color="#55CBD3" class="mt-10 mr-8">JOIN</v-btn> -->
          <join
            v-if="permission.inGroup==false"
            :userId="user.id"
            :groupId="group.id"
          ></join>
          <v-btn
            small
            v-else-if="permission.isMember==false"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
            @click="joinGroup()"
          >Request Sent</v-btn>
          <v-btn
            small
            v-else-if="permission.isOwner==true && setting==false"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
            @click="setting = !setting"
          >Setting</v-btn>
          <v-btn
            small
            v-else-if="permission.isOwner==true && setting==true"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
            @click="setting = !setting"
          >Save</v-btn>
          <v-btn
            v-else-if="permission.isOwner==false"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
            @click="leaveGroup()"
          >LEAVE</v-btn>        
        </v-row>
      </v-col>
    </v-row>
    <v-row cols="12" justify="space-between">
    <v-col cols="3" class="mt-10 ml-10 skill-section">
      <div class="subtitle mt-2">We have:</div>
      <div class="we-have mt-5">
        <v-row class="ml-6 pt-3 mb-3">
          <!-- <div> -->
            <p
              class="mr-7"
              style="color: #646868"
              v-for="skill in group.skills"
              v-bind:key="skill"
            >{{skill}}</p>
          <!-- </div> -->
        </v-row>
      </div>
      <div class="subtitle mt-6">Looking for:</div>
      <div class="we-have mt-5">
        <v-row class="ml-6 pt-3 mb-3">
          <!-- <div> -->
            <p
              class="mr-7"
              style="color: #646868"
              v-for="skill in group.skills"
              v-bind:key="skill"
            >{{skill}}</p>
          <!-- </div> -->
        </v-row>
      </div>
      <div class="subtitle mt-6">Member:</div>
      <div class="mt-4 mb-4">
        <v-row
          class="ml-4"
          style="color: #646868"
          v-for="mem in group.members"
          v-bind:key="mem.id"
        >
          <v-avatar
            @click="$router.push(`/profile/${mem.id}`)"
            class="mt-2"
            size="40">
            <img
              :src="getPhoto(mem.photo)"
            >
          </v-avatar>
          <p class="ml-4 mt-4">{{mem.name}}</p>
        </v-row>
        <v-btn
          small
          v-if="permission.isOwner==true"
          class="mt-10 ml-2"
          @click="$router.push(`/room/member/1`)"
        >Invite Members</v-btn>
      </div>
    </v-col>
    <v-col cols="8" class="mr-3">
      <div class="mt-10 schedule-title mb-3">Preferred Meeting Times</div>
      <v-sheet
        tile
        height="56"
        class="d-flex"
      >
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.prev()"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-select
          v-model="type"
          dense
          disabled
          outlined
          hide-details
          class="ma-2"
          label="week"
        ></v-select>
        <v-select
          v-model="weekday"
          :items="weekdays"
          dense
          outlined
          hide-details
          label="weekdays"
          class="ma-2"
        ></v-select>
        <v-spacer></v-spacer>
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.next()"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="value"
          :weekdays="weekday"
          :type="type"
          :events="events"
          :event-overlap-mode="mode"
          :event-overlap-threshold="30"
          :event-color="getEventColor"
          @change="getEvents"
        ></v-calendar>
      </v-sheet>
    </v-col>
    </v-row>
  </div>
</div> 
</template>

<script>
import dashboard from "@/components/dashboard"
import join from "@/components/group/join"
import { mapState } from "vuex"

export default {
  async asyncData({ $axios, params }) {
    try {
      let group = await $axios.$get(`/group/` + params.id);
      // console.log(group.gasdg)
      // console.log(permission)
      // permission=  {
      //   'inGroup': true,
      //   'isMember': true,
      //   'isOwner': true,
      // }
      return { group };
    } catch (e) {
      return { group: {} };
    }
  },
  components: {dashboard, join},
  data() {
    return {
      setting: false,
      permission:  {
        'inGroup': false,
        'isMember': false,
        'isOwner': false,
      },

      type: 'week',
      types: ['month', 'week', 'day', '4day'],
      // types: ['month', 'week', 'day', '4day'],
      mode: 'stack',
      modes: ['stack', 'column'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      weekdays: [
        { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
      ],
      value: '',
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
    }
  },
  computed: {
    ...mapState(["user"]),
  },
  methods: {
    ...mapMutations(["SAVE_GROUP"]),
    getRoomName() {
      //save group id
      this.SAVE_GROUP(this.group.id)
      return "Room: " + this.group.room
    },
    getUserPhoto() {
      console.log("http://localhost:8000" + this.user.photo)
      return "http://localhost:8000" + this.user.photo
    },
    getImageURL() {
      var url = this.group.photo.replace(/^"(.*)"$/, '$1')
      if(url.length > 2){
        var url = url.replace(/^"(.*)"$/, '$1')
        return "http://127.0.0.1:8000/media/" + url
      }else{
        return "/img/spaceman.png"
      }
    },
    getPhoto(path) {
      return "http://localhost:8000" + path
    },
    getEvents ({ start, end }) {
      const events = []

      Array.from(this.group.events).forEach( e => {
        start = new Date(e.start)
        end = new Date(e.end)

        var d = start.getDate()
        var y = start.getFullYear()
        var m = start.getMonth() + 1
        var h = start.getHours()
        var mins = start.getMinutes()
        start = y+'-'+m+'-'+d + ' ' + h +':'+mins+'0'
        
        d = end.getDate()
        y = end.getFullYear()
        m = end.getMonth() + 1
        h = end.getHours()
        mins = end.getMinutes()
        end = y+'-'+m+'-'+d + ' ' + h +':'+mins+'0'

        events.push({
          name: e.eventName,
          start: start,
          end: end,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
        })
      })
      this.events = events
      console.log(this.events)
    },
    getEventColor (event) {
      return event.color
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    async getPermission() {
      try{
        let permission = await this.$axios.$get(`/group/` + this.$route.params.id + `/user/${this.user.id}/permission`);
        this.permission = permission
      }catch(e) {
        console.log(e)
      }
    },
    async leaveGroup() {
      try {
        // let res = await this.$axios.$get(``)
      }catch(e) {

      }
    },
  },
  async mounted() {
    this.getPermission()
    // try {
    //   let permission = await this.$axios.$get(`/group/${route.params.id}/user/${userId}/permission/`);
    //   this.permission = permission;
    //   console.log(permission)
    // } catch (e) {
    //   console.log(e);
    // }
  }
}
</script>

<style scoped lang="scss">
.frame {
  background-color: #D2F3F5;
}
.group-name{
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  color: #646868;
}
.back-icon{
  width: 40px;
}
.skill-section{
  border-radius: 10px;
  background-color: #55CBD3;
  .subtitle{
    color: #646868;
    font-weight: bold;
  }
  .we-have{
    border-radius: 10px;
    background-color: #D2F3F5;

  }
}
.schedule-title{
  font-weight: bold;
  color:#55CBD3;
  font-size: 20px;
}
</style>