<template>
  <div>
    <v-row cols="12" class="mt-3">
      <v-col cols="11">
        <img class="logo1" style="margin-left: 40px" src="/img/logo.svg"/>
      </v-col>
      <v-btn large style="margin-top: 40px" color="#55CBD3" dark elevation="0" @click="$router.push(`/signin`)">
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
    <v-col>
       <div style="height: 50px; width: 100%; margin-bottom: 20px">
        <v-btn large color="#55CBD3" dark elevation="0" @click="$router.push(`/signup`)" style="width: 150px;margin-left: -75px;left: 50%">
          GET STARTED
        </v-btn>
       </div>
       <div style="height: 50px; width: 100%">
        <v-btn large color="#F56040" dark elevation="0" style="width: 250px;margin-left: -123px;left: 50%">
          <v-icon class="mr40">
            mdi-instagram
          </v-icon>
          SIGN IN WITH INSTAGRAM
        </v-btn>
      </div>
       <div style="height: 50px; width: 100%">
        <v-btn large color="#4267B2" dark elevation="0" style="width: 250px;margin-left: -123px;left: 50%">
          <v-icon class="mr40">
            mdi-facebook
          </v-icon>
          SIGN IN WITH FACEBOOK
        </v-btn>
      </div>
       <div style="height: 50px; width: 100%">
        <v-btn large color="#4285F4" dark elevation="0" style="width: 250px;margin-left: -123px;left: 50%">
          <v-icon style="margin-right: 12px">
            mdi-google
          </v-icon>
          SIGN IN WITH GOOGLE
        </v-btn>
      </div>
    </v-col>
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
.logo1 {
  width: 80px;
  height: 80px;
  margin-top: 10px;
  margin-left: 10px;
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
  font-size: 20px;
}
.text-box p {
  color: grey;
  font-size: 8px;
  font-weight: lighter;
}
</style>