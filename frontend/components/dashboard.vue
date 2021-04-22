<template>
<div>
  <v-row cols="13" class="mt-10 mb-5" justify="space-between">
    <v-col cols="2">
      <v-row justify="center">
        <v-img contain class="logo1" src="/img/logo.svg" @click="goToUserPage()"/>
      </v-row>
    </v-col>
    <v-col cols="8" align-self="center">
      <v-row justify="center" class="ml-2">
        <div class="room-name">{{this.title}}</div>
      </v-row>
    </v-col>
    <v-col cols="2" align-self="center">
      <v-row justify="end">
        <v-avatar
          @click="goToProfile()"
          class="mr-4"
          size="73">
          <img
            :src="photo"
          >
        </v-avatar>
      </v-row>
    </v-col>
  </v-row>
</div>
</template>

<script>
import { mapState } from "vuex"

export default {
  props: ["title", "photo"],
  computed: {
    ...mapState(['user'])
  },
  methods: {
    goToProfile() {
      this.$router.push(`/profile/${this.user.id}`)
    },
    goToUserPage() {
      this.$router.push(`/user/${this.user.id}`)
    }
  }
}
</script>

<style scoped>
.logo1 {
  width: 90px;
  height: 90px;
}

.room-name{
  color: #55CBD3;
  font-size: 40px;
  font-weight: light;
  text-align: center;
}
</style>