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
          <v-img contain class="ml-4 mt-7" style="max-width: 120px" :src="getImageURL()"/>
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
          ></join>
          <v-btn
            small
            v-else-if="permission.isMember==false"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
          >Request Sent</v-btn>
          <v-btn
            small
            v-else-if="permission.isOwner==true"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
          >Setting</v-btn>
          <v-btn
            v-else-if="permission.isOwner==false"
            dark
            color="#55CBD3"
            class="mt-10 ml-2"
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
        <!-- <v-col> -->
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
        <!-- </v-col> -->
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
      members: [{'id': 1, 'image': "", 'name': "Sam"},{'id': 2, 'image': "", 'name': "Amy"}],
      haveSkill: ["python", "JavaScript", "sususususususlong"],
      needSkill: ["React", "CSS", "FLASK"],
      roomName: "Room: SENG2021 PROJECTS",
      groupName: "Attack on HD",
      description: "We are passionate, enthusiastic, with highly capable coding abilties to ATTACK that HD with full force! Join us if u wanna work hard :)",
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
    getRoomName() {
      return "Room: " + this.group.room
    },
    getUserPhoto() {
      console.log("http://localhost:8000" + this.user.photo)
      return "http://localhost:8000" + this.user.photo
    },
    getImageURL() {
      var url = this.group.photo.replace(/^"(.*)"$/, '$1')
      return "http://127.0.0.1:8000/media/" + url
    },
    getPhoto(path) {
      return "http://localhost:8000" + path
    },
    getEvents ({ start, end }) {
      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      const days = (max.getTime() - min.getTime()) / 86400000
      const eventCount = this.rnd(days, days + 20)

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0
        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        })
      }
      this.events = events
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

    }
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