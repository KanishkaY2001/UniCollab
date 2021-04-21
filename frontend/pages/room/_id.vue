<template>
<div class="mt-10">
  <dashboard :title="room.name" :photo="getUserPhoto"></dashboard>
  <div class="intro">
    <v-row cols="12">
      <img class="back-icon" src="/img/back.svg" @click="$router.back()">
      <v-col cols="8">
        <div class="intro-text ml-5">{{findGroupText}}</div>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="4">
      <v-text-field
        outlined
        placeholder="Search for group.."
        append-icon="mdi-magnify"
      ></v-text-field>
      </v-col>
      <v-menu
        top
        :close-on-click="filter"
      >
        <template v-slot:activator="{ on }">
          <v-icon class="material-icons mb-5" v-on="on">
            mdi-filter
          </v-icon>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in filter_type"
            :key="index"
            @click="sortBy(item)"
            link
          >
            <v-list-item-title>
            {{ item }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-dialog
        v-model="dialog"
        width="500"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn class="mt-6 ml-4" color="#55CBD3" dark
            v-on="on"
            v-bind="attrs"
          >
            create Group
          </v-btn>
        </template>
  
        <v-card class="pa-3">
          <v-card-title class="headline grey lighten-2">
            Create a group
          </v-card-title>
          <v-text-field
            class="mt-3"
            v-model="groupName"
            outlined
            label="Group name"
          />

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false; createGroup()"
            >
              Create
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
  <div class="mt-10">
      <div class="intro-text ml-6 mr-6">{{groupIntro}}</div>
      <groupitem
        class="mt-10 mb-10"
        v-for="g in groups"
        v-bind:key="g.id"
        :group="g"
      ></groupitem>
  </div>
  <div class="footer mt-10">
    <div>Contact Us</div>
    <div>support@unicollab.com</div>
  </div>
</div>
</template>


<script>
import dashboard from "@/components/dashboard"
import groupitem from "@/components/room/groupitem"
import { mapState } from "vuex"

export default {
  components: { dashboard, groupitem },
  async asyncData({ $axios, params }) {
    try {
      let groups = await $axios.$get(`/rooms/${params.id}/groups`)
      let room = await $axios.$get(`/rooms/${params.id}`)
      return { groups, room }
    }catch(e){
      console.log(e)
      return { groups: {} };
    }
  },
  data() {
    return {
      dialog: false,
      filter: false,
      filter_type: ['Overall Match', 'Timetable', 'Location', 'Skillset'],
      findGroupText: "Find a group by scrolling through the list below, or filtering your search using the search bar filter tool",
      roomId: this.$route.params.id,
      groupIntro: "Groups with proposed meeting times that match your calendar commitments will be displayed green, if you are are partially available for a groups proposed meeting times, the group will be displayed yellow. Incompatible groups will be listed as red. You may click a box to see more information about the group.",
      groupName: ""
    }
  },
  computed: {
    getUserPhoto() {
      return "http://localhost:8000" + this.user.photo
    },
    ...mapState(['user'])
  },
  methods: {
    async createGroup() {
      try {
        let res = await this.$axios.$get(`rooms/${this.user.id}/${this.room.id}/creategroup/${this.groupName}`)
        console.log(res)
        if(res.id){
          this.$router.push(`/group/${res.id}`)
        }else{
          alert("Fail")
        }
      }catch(e) {
        console.log(e)
      }
    },
    async sortBy(item) {
      if(item == "Location"){
        try{
          // '<int:id>/location/<int:rid>'
          let res = await this.$axios.$get(`rooms/${this.user.id}/location/${this.room.id}`)
          console.log(res)
          this.groups = res
        }catch(e){
          console.log(e)
        }
      }
    }
  }
}

</script>
<style scoped lang="scss">
.back-icon{
  width: 50px;
}
.intro{
  background-color: #D2F3F5;
  .intro-text{
    color: #646868;
  }
}
.intro-text{
  font-size: 15px;
  color: #55CBD3;
}
.footer{
  background-color: #D2F3F5;
  color: #646868;
  text-align: center;
}
</style>