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

new Vue({
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
})

