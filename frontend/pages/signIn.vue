<template>
<div>
  <v-row><div class="frame mt-10"></div></v-row>
  <v-row>
    <div style="height: 10px"></div>
    <v-col cols="1" class="vertical-frame"></v-col>
    <v-col cols="10" class="content">
      <v-row justify="center" class="mt-14"><div class="title-text">Log In</div></v-row>
      <v-row class="ml-6 mr-6 mt-16">
        <v-text-field placeholder="Username (email)" label="Username (email)" outlined></v-text-field>
      </v-row>
      <v-row class="ml-6 mr-6 mt-5">
        <v-text-field
            :value="userPassword"
            label="Password"
            placeholder="Password"
            :append-icon="value ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="() => (value = !value)"
            :type="value ? 'password' : 'text'"
            outlined
        ></v-text-field>
      </v-row>
      <v-row justify="center" class="mt-10">
        <v-btn color="#55CBD3" dark elevation="0">
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
export default {
    data: () => ({
        userPassword: "",
        valid: true,
        value: true,
    })
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