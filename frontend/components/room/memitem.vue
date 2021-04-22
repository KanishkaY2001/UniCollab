<template>
  <v-row cols="12" class="mt-3" v-bind:class="{frame0: zero, frame1: one, frame2: two}">
    <v-col cols="3" align-self="center">
      <v-img height=120 :src="getUserImage(mem.photo)"/>
    </v-col>
    <v-col cols="3">
        <div class="group-title mt-1"
          @click="goToGroup()"
        >{{mem.name}}</div>
        <div class="discript-text mt-1">{{mem.bio}}</div>
    </v-col>
    <v-col cols="4">
      <div class="list-title mt-1">Matched Skills</div>
      <v-sheet
        style="background-color: white;overflow-y: auto;"
        scrollable
        max-height="100">
        <div> 
          <div
            v-for="(item, i) in mem.skills"
            v-bind:key="i"
            class="list-text ml-1">- {{item}}
          </div>
        </div>
      </v-sheet>
    </v-col>
    <v-col cols="1" align-self="center">
      <v-btn
        outlined
        @click="invite()"
      >
        Invite
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from "vuex"
export default {
  props: ["mem"],
  data() {
    return {
      skills: {}
    }
  },
  methods: {
    check() {
      console.log(this.skills)
    },
    onScroll () {
      this.scrollInvoked++
    },
    goToUser() {
      this.$router.push(`/user/${this.mem.id}`)
    },
    getUserImage(url) {
      console.log(url)
      if(url.length > 2){
        var url = url.replace(/^"(.*)"$/, '$1')
        return "http://127.0.0.1:8000/media/" + url
      }else{
        return "/img/spaceman.png"
      }
    },
    async invite() {
      // path('<int:gid>/join/<int:id>', joinGroup),
      let res = await this.$axios.$get(`group/${this.currentGroup}/join/${this.mem.id}`)
    }
  },
  computed: {
    ...mapState(['currentGroup']),
    zero: function(){
      return this.mem.match == 0
    },
    one: function(){
      return this.mem.match == 1
    },
    two: function(){
      return this.mem.match == 2  || this.mem.match == null
    }
  },
  mounted() {
    this.check()
  }
}
</script>

<style scoped lang="scss">
.frame0{
  margin: 0px;
  background-color: #F0AFAF;
}
.frame1{
  margin: 0px;
  background-color: #ECE7C0;
}
.frame2{
  margin: 0px;
  background-color: #C7DAC7;
}
.group-title{
  width: 100%;
  // text-align: center;
  font-size: 22px;
}
.discript-text{
  color: #646868;
  font-size: 14px;
}
.list-title{
  font-size: 22px;
  color:#646868;
  font-weight: 10px;
  height: 35px;
}
.list-text{
  color: #646868;
  font-size: 15px;
}
.vacancy-frame{
  height: 70px;
  width: 90px;
  background-color: #7FCED3;
  .text{
    color: white;
    text-align: center;
    font-size: 30px;
  }
}
</style>