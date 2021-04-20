<template>
  <div class="mt-10">
    <dashboard :title="getUserName()" :photo="getUserPhoto()"></dashboard>
    <v-row cols="12" class="pb-10">
      <v-col cols="4" style="background-color: #8AE8EF">
        <img class="back-icon" src="/img/back.svg" @click="$router.back()">
        <div class="subtitle">Find a Room...</div>
        <v-text-field
          class="mt-2"
          outlined
          placeholder="I am looking for..."
          append-icon="mdi-magnify"
          rounded
          background-color="#fff"
          color="#8AE8EF"
        ></v-text-field>
        <div class="label-text">All Rooms</div>
        <v-card
          elevation="0"
          class="ma-4"
        >
          <v-virtual-scroll
            :bench="benched"
            :items="rooms"
            height="300"
            item-height="64"
          >
            <!-- <v-tooltip bottom> -->
            <template v-slot:default="{ item }">
              <v-list-item :key="item.id" @click="$router.push(`/room/${item.id}`)">    
                <v-list-item-content>
                  <v-list-item-title>
                    <span>{{item.name}}</span>
                  </v-list-item-title>
                </v-list-item-content>
    
              <v-list-item-action>
                  <v-btn
                    small
                    depressed
                    dark
                    color="#55CBD3"
                  >
                    Join
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider></v-divider>
            </template>
            <!-- <span>{item.name}</span> -->
            <!-- </v-tooltip> -->
          </v-virtual-scroll>
        </v-card>
      </v-col>
      <v-col cols="8">
        <v-row justify="end" style="background-color:#D2F3F5">
          <v-btn 
            dark
            color="#55CBD3">
            LOGOUT
          </v-btn>
          <img class="back-icon ml-4" src="/img/bell.svg"/>
        </v-row>
        <v-row justify="center">
          <v-btn 
            dark
            large
            elevation="0"
            color="#55CBD3"
            class="mt-10"
          >CREATE ROOM</v-btn>
        </v-row>
        <div class="mt-10">
          <div class="title-text pt-5">My Rooms</div>
          <v-sheet
            class="mx-auto"
            elevation="0"
            max-width="800"
          >
            <v-slide-group
              v-model="model"
              class=""
              active-class="success"
              show-arrows
            >
              <v-slide-item
                v-for="room in myRooms"
                :key="room.id"
              >
                <v-card
                  class="ma-2"
                  height="120"
                  width="100"
                  color="#D2F3F5"
                  @click="$router.push(`/room/1`)"
                >
                <div style="text-align: center; color:#646868" class="mt-2">{{room.name}}</div>
                <v-btn
                  class="mt-9 ml-4"
                  style="position: absolute; bottom: 10%"
                  small
                  dark
                  color="#55CBD3">LEAVE
                </v-btn>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
        </div>
        <div class="mt-1">
          <div class="title-text pt-5">My Groups</div>
          <v-sheet
            class="mx-auto"
            elevation="0"
            max-width="800"
          >
            <v-slide-group
              v-model="model"
              class="pa"
              active-class="success"
              show-arrows
            >
              <v-slide-item
                v-for="room in myGruops"
                :key="room.id"
              >
                <v-card
                  class="ma-2"
                  height="120"
                  width="100"
                  color="#D2F3F5"
                  @click="$router.push(`/group/1`)"
                >
                <div style="text-align: center; color:#646868" class="mt-2">{{room.name}}</div>
                <v-btn
                  class="mt-9 ml-4"
                  style="position: absolute; bottom: 10%"
                  small
                  dark
                  color="#55CBD3">LEAVE
                </v-btn>
                </v-card>
              </v-slide-item>
            </v-slide-group>
          </v-sheet>
        </div>
      </v-col>
    </v-row>
    <div class="footer">
      <div>Contact Us</div>
      <div>support@unicollab.com</div>
    </div>
  </div>
</template>

<script>
import dashboard from '../../components/dashboard.vue'
import { mapState } from "vuex"

export default {
  components: { dashboard },
  computed: {
    ...mapState(["user"]),
  },

  // async asyncData({ $axios, params }) {
  //   try {
  //     let rooms = await $axios.$get(`/rooms/`);
  //     let myRooms = await $axios.$get(`${this.user.id}/rooms`);
  //     return { rooms, myRooms }
  //   } catch (e) {
  //     return { group: {} };
  //   }
  // },
  async mounted() {
    try {
      this.rooms = await this.$axios.$get(`/rooms/`);
      this.myRooms = await this.$axios.$get(`student/${this.user.id}/rooms`);
      this.myGruops = await this.$axios.$get(`student/${this.user.id}/groups`);

    }catch(e) {
      console.log(e)
    }
  },
  data() {
    return {
      benched: 0,
      model: null,
      rooms: [],
      myRooms: [],
      myGruops: []
    }
  },
  methods: {
    getUserName() {
      return "welcome " + this.user.name
    },
    getUserPhoto() {
      console.log("http://localhost:8000" + this.user.photo)
      return "http://localhost:8000" + this.user.photo
    }
  },
}
</script>

<style lang="scss" scoped>
.back-icon{
  width: 40px;
}
.footer{
  background-color: #D2F3F5;
  color: #646868;
  text-align: center;
}
.subtitle{
  color: white;
  font-size: 25px;
  font-weight: bold;
  text-align: center;
}
.label-text{
  color: white;
  font-size: 15px;
  font-weight: bold;
}
.title-text{
  color: #55CBD3;
  font-size: 25px;
  // font-weight: bold;
  text-align: center;
}
span {
  width: 100px; /* can be 100% ellipsis will happen when contents exceed it */ 
  display: inline-block;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
span:hover {
  white-space: normal;
  /* or: 
  width: auto;
  */
}
</style>