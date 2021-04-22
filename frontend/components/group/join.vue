<template>
<v-col cols="auto">
  <v-dialog
    transition="dialog-bottom-transition"
    max-width="600"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-bind="attrs"
        v-on="on"
        dark
        color="#55CBD3"
        class="mt-10 ml-2"
      >JOIN</v-btn>
    </template>
    <template v-slot:default="dialog">
      <v-card>
        <div class="form-head pt-10">Request to join</div>
        <v-textarea
          class="ma-6"
          solo
          outlined
          height=300
          label="Tell us a bit about yourself">
        </v-textarea>
        <v-card-actions class="justify-end">
          <v-btn
            text
            color="#55CBD3"
            @click="sendJoinRequest(); dialog.value = false"
          >SEND</v-btn>
        </v-card-actions>
      </v-card>
    </template>
  </v-dialog>
</v-col>
</template>


<script>
export default {
  props: ["userId", "groupId"],
  methods: {
    async sendJoinRequest() {
      try{
        let res = await this.$axios.$get(`group/${this.groupId}/join/${this.userId}`)
      }catch(e){
        console.log(e)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.form-head{
  color: #55CBD3;
  font-size: 25px;
  text-align: center;
  font-weight: bold;
}

</style>