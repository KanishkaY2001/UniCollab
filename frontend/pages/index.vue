<template>
  <div>
    <v-row cols="12" class="mt-3">
      <v-col cols="6">
        <img class="logo1" style="margin-left: 10px; margin-top: 10px" src="/img/logo.svg"/>
      </v-col>
      <v-col cols="6">
        <v-btn :right="true" :absolute="true" large style="margin-top: 45px" color="#55CBD3" dark elevation="0" @click="$router.push(`/signin`)" x-large>
          LOGIN
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <div class="welcome"> 
        <div class="welcome-text">Welcome to UniCollab!</div>
      </div>
      <div style="height: 300px"></div>
    </v-row>
    <v-row align="bottom" justify="space-around">
      <div style="height: 50px; width: 100%">
        <div class="sign-up">Sign-up to start collaborating</div>
      </div>
    </v-row>
    <v-row>
       <div style="height: 50px; width: 100%">
        <v-btn class="get-started" style="margin-top: 2%" height="75" width="200" color="#55CBD3" dark elevation="0" @click="$router.push(`/signup`)" :style="{left: '50%', transform:'translateX(-50%)'}">
          GET STARTED
        </v-btn>
      </div>
    </v-row>
  </div>
</template>


<script>
export default {
  layout: 'welcome',
  head() {
    return {
      title: "Home page"
    };
  },
};
</script>

<style scoped lang="scss">
.get-started {
  font-size: 20px;
}
.welcome {
  height: 150px;
  width: 100%;
  background-color: #A1EEF4;
  .welcome-text {
    font-size: 40px;
    color: white;
    font-weight: bold;
    text-align: center;
    vertical-align: middle;
    line-height: 150px;
  }
}
.sign-up {
  color: grey;
  text-align: center;
  font-size: 40px;
}
.text-box p {
  color: grey;
  font-size: 8px;
  font-weight: lighter;
}
</style>