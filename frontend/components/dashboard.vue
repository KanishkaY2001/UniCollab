<template>
<div>
  <v-row cols="12" justify="space-between">
    <v-col cols="2">
      <v-img contain class="logo1" src="/img/logo.svg"/>
    </v-col>
    <v-col cols="8" justify="center" class="pr-6 mt-3">
      <div class="room-name">{{this.title}}</div>
    </v-col>
    <v-col cols="2">
      <v-avatar
        class="mt-2"
        color="#55CBD3"
        size="67">
      </v-avatar>
    </v-col>
  </v-row>
</div>
</template>

<script>
export default {
  props: ["title"],
  data() {
    return {
      roomName: "SENG2021 PROJECTS"
    }
  }
}
</script>

<style scoped>
.logo1 {
  width: 100px;
  height: 100px;
}

.room-name{
  color: #55CBD3;
  font-size: 40px;
  font-weight: light;
  text-align: center;
}
</style>