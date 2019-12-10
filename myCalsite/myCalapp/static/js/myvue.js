/*new Vue({
    el: '#app',
    data: () => ({
      type: 'month',
      start: '2019-01-01',
      end: '2019-01-06',
      typeOptions: [
        { text: 'Day', value: 'day' },
        { text: '4 Day', value: '4day' },
        { text: 'Week', value: 'week' },
        { text: 'Month', value: 'month' },
        { text: 'Custom Daily', value: 'custom-daily' },
        { text: 'Custom Weekly', value: 'custom-weekly' }
      ]
    })
}) */

var app4 = new Vue({
  el: '#app-4',
  data: {
      posts: [],
  },

  created: function() {
      this.fetchPostList();
      this.timer = setInterval(this.fetchPostList, 10000);
  },
  methods: {
  fetchPostList: function() {
      axios
      .get('calendar/')
      .then(response => (this.posts = response.data.posts))
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

