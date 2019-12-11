
var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    }
})

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
/*
export default {
    components: { 'vue-cal': vuecal },
    el: '#cal',
    data: () => ({
    events: [
      {
        start: '2018-11-19 10:35',
        end: '2018-11-19 11:30',
        title: 'Doctor appointment'
      },
}
*/



