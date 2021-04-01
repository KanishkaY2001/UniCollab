<template>
  <v-row cols="12" class="frame mt-3">
    <v-col cols="2" align-self="center">
      <v-img contain src="/img/spaceman.png"/>
    </v-col>
    <v-col cols="3" align-self="center">
        <div class="group-title mt-2">GroupName</div>
        <div class="discript-text mt-1">{{discript}}</div>
    </v-col>
    <v-col cols="3">
      <div class="list-title">Looking For...</div>
      <v-sheet
        style="background-color: white;overflow-y: auto;"
        scrollable
        max-height="100">
        <div> 
          <div
            v-for="(item, i) in skills"
            v-bind:key="i"
            class="list-text ml-1">- {{item}}
          </div>
        </div>
      </v-sheet>
    </v-col>
    <v-col cols="2">
      <div class="list-title">Members</div>
        <div style="background-color: white;overflow-y: auto;">
          <div
            v-for="(item, i) in members"
            v-bind:key="i"
          > 
          <div class="list-text ml-3">{{item}}</div>
        </div>
      </div>
    </v-col>
    <v-col cols="2">
      <div class="list-title">Vacancy</div>
      <div class="vacancy-frame">
        <div class="text pt-3">3/5</div>
      </div>
    </v-col>
  </v-row>
</template>

<script>
export default {
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
  }
}
</script>

<style scoped lang="scss">
.frame{
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