var myevents = new Vue({
  el: '#myevents',
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

var mytasks = new Vue({
    el: '#mytasks', //change to events
    data: {
        tasks: [],
        seen: true,
        unseen: false
    },
  
    created: function() {
        this.fetchTaskList();
        this.timer = setInterval(this.fetchTaskList, 10000);
    },
    methods: {
    fetchTaskList: function() {
        axios
        .get('tasks/')
        .then(response => (this.tasks = response.data.tasks))
        console.log(this.tasks)
        this.seen=false
        this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
    clearInterval(this.timer)
    }
  
  })

var myfriends = new Vue({
    el: '#myfriends', //change to events
    data: {
        friends: [],
    },
  
    created: function() {
        this.fetchFriendList();
        this.timer = setInterval(this.fetchFriendList, 10000);
    },
    methods: {
    fetchFriendList: function() {
        axios
        .get('friends/')
        .then(response => (this.friends = response.data.friends))
        console.log(this.friends)
        this.seen=false
        this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
    },
    beforeDestroy() {
    clearInterval(this.timer)
    }
  })