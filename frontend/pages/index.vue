<template>
  <div>
    <v-row cols="12">
      <v-col cols="10" style="margin-left: 10px">
        <img class="logo1 ml-5" src="/img/logo.svg"/>
      </v-col>
      <v-btn style="margin-top: 20px; margin-right: 20px" color="#55CBD3" dark elevation="0">
        LOGIN
      </v-btn>
    </v-row>
    <v-row>
      <div class="welcome"> 
        <div class="welcome-text">Welcome to UniCollab!</div>
      </div>
      <div style="height: 300px"></div>
    </v-row>
    <v-row align="center" justify="space-around">
      <div style="height: 50px; width: 100%">
        <div class="sign-up">Sign-up to start collaborating</div>
      </div>
    </v-row>
    <v-row>
       <div style="height: 50px; width: 100%">
        <v-btn color="#55CBD3" dark elevation="0" style="width: 150px;margin-left: -75px;left: 50%">
          GET STARTED
        </v-btn>
      </div>
    </v-row>
  </div>
</template>


<script>
export default {
  head() {
    return {
      title: "Home page"
    };
  },
};
</script>

<style scoped lang="scss">
.logo1 {
  left: 5%;
  width: 80px;
  height: 80px;
}
.welcome {
  height: 150px;
  width: 100%;
  background-color: #A1EEF4;
  .welcome-text {
    font-size: 25px;
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
}
.text-box p {
  color: grey;
  font-size: 8px;
  font-weight: lighter;
}
</style>