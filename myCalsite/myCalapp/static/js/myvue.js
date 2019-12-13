new Vue({
    el: '#cal',
    vuetify: new Vuetify(),
    data: () => ({
      events: [
        {
          name: 'Vacation',
          start: '2018-12-30',
          end: '2019-01-02',
        },
        {
        name: 'Meeting',
        start: '2019-01-07',
        },
    ],
}),
})

var app4 = new Vue({
  el: '#app-4', //change to events
  data: {
      events: [],
  },

  created: function() {
      this.fetchEventList();
      this.timer = setInterval(this.fetchEventList, 10000);
  },
  methods: {
  fetchEventList: function() {
      axios
      .get('events/')
      .then(response => (this.events = response.data.events))
      console.log(this.posts)
      this.seen=false
      this.unseen=true
  },
  cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
  clearInterval(this.timer)
  }

})