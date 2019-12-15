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