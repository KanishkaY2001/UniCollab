<template>
<div>
  <dashboard :title="roomName"></dashboard>
  <div class="frame pb-10">
    <v-row class="mt-10" cols="12" justify="space-between">
      <img class="back-icon" src="/img/back.svg">
      <v-col cols="8">
        <div class="group-name ml-5">{{groupName}}</div>
      </v-col>
      <img class="back-icon mr-4" src="/img/bell.svg">
    </v-row>
    <v-divider class="mt-3"></v-divider>
    <v-row class="group-info" cols="12" justify="center">
      <v-col cols="9">
        <v-row>
          <v-img contain class="ml-4 mt-7" style="max-width: 120px" src="/img/spaceman.png"/>
          <v-col cols="7" style="background-color: white" class="mt-7 ml-7">
            <div style="color: #55CBD3">About us</div>
            <div style="font-size: 13px; color: #646868">
              {{description}}
            </div>
          </v-col>
        </v-row>
      </v-col>
      <v-btn dark color="#55CBD3" class="mt-10 mr-8">JOIN</v-btn>
    </v-row>
    <v-row cols="12" justify="space-between">
    <v-col cols="3" class="mt-10 ml-10 skill-section">
      <div class="subtitle">We have:</div>
      <div class="we-have mt-5">
        <v-row class="ml-6 pt-3 mb-3">
          <!-- <div> -->
            <p
              class="mr-7"
              style="color: #646868"
              v-for="skill in haveSkill"
              v-bind:key="skill"
            >{{skill}}</p>
          <!-- </div> -->
        </v-row>
      </div>
      <div class="subtitle">Looking for:</div>
      <div class="we-have mt-5">
        <v-row class="ml-6 pt-3 mb-3">
          <!-- <div> -->
            <p
              class="mr-7"
              style="color: #646868"
              v-for="skill in needSkill"
              v-bind:key="skill"
            >{{skill}}</p>
          <!-- </div> -->
        </v-row>
      </div>
      <div class="subtitle">Member:</div>
      <div class="mt-4 mb-4">
        <!-- <v-col> -->
          <v-row
            class="ml-4"
            style="color: #646868"
            v-for="mem in members"
            v-bind:key="mem.is"
          >
            <v-avatar
              class="mt-2"
              color="#D2F3F5"
              size="40">
            </v-avatar>
            <p class="ml-2 mt-4">{{mem.name}}</p>
          </v-row>
        <!-- </v-col> -->
      </div>
    </v-col>
    <v-col cols="7" class="ml-1">
      <div class="mt-10 schedule-title">Preferred Meeting Times</div>
      <v-sheet class="mt-10" height="300" width="400">
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          :events="events"
          color="primary"
          type="week"
        ></v-calendar>
      </v-sheet>
    </v-col>
    </v-row>
  </div>
</div> 
</template>

<script>
import dashboard from "@/components/dashboard"
export default {
  components: {dashboard},
  data() {
    return {
      members: [{'id': 1, 'image': "", 'name': "Sam"},{'id': 2, 'image': "", 'name': "Amy"}],
      haveSkill: ["python", "JavaScript", "python", "sususususususlong"],
      needSkill: ["React", "CSS", "FLASK"],
      roomName: "Room: SENG2021 PROJECTS",
      groupName: "Attack on HD",
      description: "We are passionate, enthusiastic, with highly capable coding abilties to ATTACK that HD with full force! Join us if u wanna work hard :)"
    }
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