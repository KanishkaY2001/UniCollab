<template>
<div class="mb-10">
  <div class="mt-10 schedule-title mb-3" style="text-align: center; font-size: 26px">Your Calendar</div>
  <v-row justify="end">
    <v-btn color="#55CBD3" dark elevation="0" large class="mt-3" @click="sync()">
      Sync
    </v-btn>
  </v-row>
    <v-sheet
        tile
        height="56"
        class="d-flex"
      >
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.prev()"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        <v-select
          v-model="type"
          dense
          disabled
          outlined
          hide-details
          class="ma-2"
          label="week"
        ></v-select>
        <v-select
          v-model="weekday"
          :items="weekdays"
          dense
          outlined
          hide-details
          label="weekdays"
          class="ma-2"
        ></v-select>
        <v-spacer></v-spacer>
        <v-btn
          icon
          class="ma-2"
          @click="$refs.calendar.next()"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="value"
          :weekdays="weekday"
          :type="type"
          :events="events"
          :event-overlap-mode="mode"
          :event-overlap-threshold="30"
          :event-color="getEventColor"
          @change="getEvents"
        ></v-calendar>
    </v-sheet>
</div>
</template>

<script>
export default {
  async asyncData({ $axios, params }) {
    try {
      let userInfo = await $axios.$get(`/student/` + params.id);
      return { userInfo };
    } catch (e) {
      return { userInfo: {} };
    }
  },
  data() {
    return {
      type: 'month',
      types: ['month', 'week', 'day', '4day'],
      // types: ['month', 'week', 'day', '4day'],
      mode: 'stack',
      modes: ['stack', 'column'],
      weekday: [0, 1, 2, 3, 4, 5, 6],
      weekdays: [
        { text: 'Sun - Sat', value: [0, 1, 2, 3, 4, 5, 6] },
        { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
        { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
        { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
      ],
      value: '',
      events: [],
      colors: ['blue', 'indigo', 'deep-purple', 'cyan', 'green', 'orange', 'grey darken-1'],
      names: ['Meeting', 'Holiday', 'PTO', 'Travel', 'Event', 'Birthday', 'Conference', 'Party'],
      dragEvent: null,
      dragStart: null,
      createEvent: null,
      createStart: null,
      extendOriginal: null,
    }
  },
  methods: {
    getEvents ({ start, end }) {
      const events = []

      Array.from(this.userInfo.calendar).forEach( e => {
        start = new Date(e.start)
        end = new Date(e.end)

        var d = start.getDate()
        var y = start.getFullYear()
        var m = start.getMonth() + 1
        var h = start.getHours()
        var mins = start.getMinutes()
        start = y+'-'+m+'-'+d + ' ' + h +':'+mins
        if(start[-2] == ":"){
          start += "0"
        }
        
        d = end.getDate()
        y = end.getFullYear()
        m = end.getMonth() + 1
        h = end.getHours()
        mins = end.getMinutes()
        end = y+'-'+m+'-'+d + ' ' + h +':'+mins

        if(end[-2] == ":"){
          end += "0"
        }

        events.push({
          name: e.name,
          start: start,
          end: end,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
        })
      })
      this.events = events
      console.log(this.events)
    },
    getEventColor (event) {
      return event.color
    },
    rnd (a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a
    },
    rndElement (arr) {
      return arr[this.rnd(0, arr.length - 1)]
    },
    async sync() {
      try{
        let res = await this.$axios.$get(`/student/${this.$route.params.id}/sync`)
        this.userInfo = await this.$axios.$get(`/student/` + params.id);
        this.getEvents()
        console.log("here")
      }catch(e) {
        console.log(e)
      }
    }
  },
}
</script>


<style lang="scss" scoped>
.v-event-draggable {
padding-left: 6px;
}

.v-event-timed {
user-select: none;
-webkit-user-select: none;
}

.v-event-drag-bottom {
position: absolute;
left: 0;
right: 0;
bottom: 4px;
height: 4px;
cursor: ns-resize;

&::after {
  display: none;
  position: absolute;
  left: 50%;
  height: 4px;
  border-top: 1px solid white;
  border-bottom: 1px solid white;
  width: 16px;
  margin-left: -8px;
  opacity: 0.8;
  content: '';
}

&:hover::after {
  display: block;
}
}
</style>