// import moment from 'moment'
// Vue.prototype.moment = moment

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    }
})


var app4 = new Vue({
  el: '#app-4',
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

// Vue.filter('chat_name', function (value) {
//   if (!value) return ''
//   value = value.toString()
//   return value
// })

// Vue.filter('datetostring', function (value) {
//   if (!value) return ''
//   value = value.toString()
//   return value
// })




