<template>
  <v-row cols="12" class="mt-3" v-bind:class="{frame0: zero, frame1: one, frame2: two}">
    <v-col cols="2" align-self="center">
      <v-img  :src="getGroupImage(group.photo)"/>
    </v-col>
    <v-col cols="3" align-self="center">
        <div class="group-title mt-2"
          @click="goToGroup()"
        >{{group.name}}</div>
        <div class="discript-text mt-1">{{group.discript}}</div>
    </v-col>
    <v-col cols="3">
      <div class="list-title">Looking For...</div>
      <v-sheet
        style="background-color: white;overflow-y: auto;"
        scrollable
        max-height="100">
        <div> 
          <div
            v-for="(item, i) in group.lookingFor"
            v-bind:key="i"
            class="list-text ml-1">- {{item}}
          </div>
        </div>
      </v-sheet>
    </v-col>
    <v-col cols="2">
      <div class="list-title">Members</div>
        <div style="background-color: white;overflow-y: auto;">
        <v-sheet
          style="background-color: white;overflow-y: auto;"
          scrollable
          max-height="100">
          <div> 
            <div
              v-for="(item, i) in group.members"
              v-bind:key="i"
              class="list-text ml-1">- {{item.name}}
            </div>
          </div>
        </v-sheet>
      </div>
    </v-col>
    <v-col cols="2">
      <div class="list-title">Vacancy</div>
      <div class="vacancy-frame">
        <div class="text pt-3">{{group.members.length}}/5</div>
      </div>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: ["group"],
  data() {
    return {
      scrollInvoked: 0,
      members: ['Aiden', 'Fitan', 'James'],
      skills: ['python', 'Vue', 'Low-Fi Prototyping', 'Figma', 'Django'],
      discript: "Find a group by scrolling through the list below, or filtering your search using the search bar filter tool",
    }
  },
  methods: {
    onScroll () {
      this.scrollInvoked++
    },
    goToGroup() {
      this.$router.push(`/group/${this.group.id}`)
    },
    getGroupImage(url) {
      if(url.length > 2){
        var url = url.replace(/^"(.*)"$/, '$1')
        return "http://127.0.0.1:8000/media/" + url
      }else{
        return "/img/spaceman.png"
      }
    },
  },
  computed: {
    zero: function(){
      return this.group.match == 0 || this.group.match == null
    },
    one: function(){
      return this.group.match == 1
    },
    two: function(){
      return this.group.match == 2
    }
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
  text-align: center;
  color: #55CBD3;
  font-size: 22px;
  background-color: white;
  border: #55CBD3;
  border-style: solid;
}
.discript-text{
  color: #646868;
  font-size: 10px;
  text-align: center;
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