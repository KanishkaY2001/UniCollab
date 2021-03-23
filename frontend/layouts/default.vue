<template>
  <v-app id="cApp">
    <v-main>
      <v-row no-gutters justify="center">
        <v-col cols="12" sm="10" lg="8" class="max">
          <nuxt />
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<style>
#cApp {
  font-family: "apercu", "Microsoft JhengHei", "微軟正黑體", Arial;
  background-color:white !important;
}

.max {
  max-width: 1024px;
}

.m0 {
  margin: 0;
}
.mt10 {
  margin-top: 10px;
}
.mt15 {
  margin-top: 15px;
}
.mt20 {
  margin-top: 20px;
}
.mt30 {
  margin-top: 30px;
}
.mt40 {
  margin-top: 40px;
}
.ml10 {
  margin-left: 10px;
}
.ml15 {
  margin-left: 15px;
}
.ml20 {
  margin-left: 20px;
}
.ml30 {
  margin-left: 30px;
}
.mr10 {
  margin-right: 10px;
}
.mr15 {
  margin-right: 15px;
}
.mr20 {
  margin-right: 20px;
}
.mr30 {
  margin-right: 30px;
}
.mb10 {
  margin-bottom: 10px;
}
.mb15 {
  margin-bottom: 15px;
}
.mb20 {
  margin-bottom: 20px;
}
.mb30 {
  margin-bottom: 30px;
}
.pt10 {
  padding-top: 10px;
}
.pt15 {
  padding-top: 15px;
}
.pt20 {
  padding-top: 20px;
}
.pt30 {
  padding-top: 30px;
}
.pt40 {
  padding-top: 40px;
}
.pb10 {
  padding-bottom: 10px;
}
.pb15 {
  padding-bottom: 15px;
}
.pb20 {
  padding-bottom: 20px;
}
.pb30 {
  padding-bottom: 30px;
}
.pb40 {
  padding-bottom: 40px;
}
.f14 {
  font-size: 14px;
}
.f16 {
  font-size: 16px;
}
.f18 {
  font-size: 18px;
}
.f20 {
  font-size: 20px;
}
.f22 {
  font-size: 22px;
}
.f24 {
  font-size: 24px;
}
</style>