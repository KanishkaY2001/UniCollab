<template>
<div>
  <v-row><div class="frame mt-10"></div></v-row>
  <v-row>
    <div style="height: 10px"></div>
    <v-col cols="1" class="vertical-frame"></v-col>
    <v-col cols="10" class="content">
      <v-row justify="center" class="mt-14"><div class="title-text">Log In</div></v-row>
      <v-row class="ml-6 mr-6 mt-16">
        <v-text-field
          v-model="email"
          placeholder="Username (email)"
          label="Username (email)"
          outlined>
        </v-text-field>
      </v-row>
      <v-row class="ml-6 mr-6 mt-5">
        <v-text-field
            v-model="pwd"
            label="Password"
            placeholder="Password"
            :append-icon="value ? 'mdi-eye-off' : 'mdi-eye'"
            outlined
        ></v-text-field>
      </v-row>
      <v-row justify="center" class="mt-10">
        <v-btn color="#55CBD3" dark elevation="0" @click="login">
          Login
        </v-btn>
        <v-btn @click="$router.push(`/signup`)" color="#55CBD3" dark elevation="0" class="ml-10">
          Sign Up
        </v-btn>
      </v-row>

      <v-row justify="center" class="mt-10">
        <v-btn color="#55CBD3" dark elevation="0" @click="$router.push(`/`)">
          Cancel
        </v-btn>
      </v-row>

    </v-col>
    <v-col cols="1.25" class="vertical-frame"></v-col>
  </v-row>
  <v-row><div class="bottom-frame"></div></v-row>
</div>
</template>

<script>
import { mapMutations } from "vuex"

export default {
  data: () => ({
      pwd: "",
      email: "",
      studentId: "",
      value: false
  }),
  methods: {
    ...mapMutations(["SAVE_USER"]),
    async login() {
      try{
        let user = await this.$axios.get(`student/login/${this.email}/${this.pwd}`)
        console.log(user.data)
        if(user.data != {}) {
          let info = user.data
          this.SAVE_USER(info)
          this.$router.push(`/user/${info.id}`)
        }else{
          alert("incorrect username or password")
        }
      }catch(e) {
        console.log(e)
      }
    }
  },
}
</script>

<style scoped lang="scss">
.frame{
  top: 50%;
  height: 70px;
  width: 100%;
  background-color: #93E8EE
}
.vertical-frame{
  height: 600px;
  width: 100%;
  background-color: #93E8EE
}
.bottom-frame{
  height: 70px;
  width: 100%;
  background-color: #93E8EE;
}
.content{
  background-color: white;
  .title-text{
    color: #55CBD3;
    font-size: 40px;
    font-weight: bold;
  }
}
</style>