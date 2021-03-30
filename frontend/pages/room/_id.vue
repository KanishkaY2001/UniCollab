<template>
<div class="mt-10">
  <dashboard></dashboard>
  <div class="intro">
    <v-row>
      <img class="back-icon" src="/img/back.svg"></img>
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
      <v-btn class="mt-6 ml-4" color="#55CBD3" dark>
        create Group
      </v-btn>
    </v-row>
  </div>
  <div class="mt-10">
      <div class="intro-text ml-6 mr-6">{{groupIntro}}</div>
      <groupitem
        class="mt-10 mb-10"
        v-for="g in groups"
        v-bind:key="g.id"
      
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

export default {
  components: { dashboard, groupitem },
  data() {
    return {
      findGroupText: "Find a group by scrolling through the list below, or filtering your search using the search bar filter tool",
      roomId: this.$route.params.id,
      groupIntro: "Groups with proposed meeting times that match your calendar commitments will be displayed green, if you are are partially available for a groups proposed meeting times, the group will be displayed yellow. Incompatible groups will be listed as red. You may click a box to see more information about the group.",
      groups:[{'id': 1}, {'id': 2}],
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