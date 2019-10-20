'use strict';

var app = new Vue({
  el: '#talklist',
  data: {
    items: [],
    userid: '',
    passwd: '',
    subject: '',
    summary: ''
  },

  methods: {
    login: function(userid, passwd) {
      this.userid = '';
      this.passwd = '';
      this.$http.post('/Plone/@login',
                {'login': userid,
                 'password': passwd},
                {headers:
                 {'Content-type':'application/json',
                  'Accept':'application/json'}}).
        then(function(data, status, headers, config){
          localStorage.setItem('jwtoken', data.token);
        }, function(error){
          alert('Could not log you in');
        });
    },
    is_logged_in: function() {
      // we assume the user is logged in when he has a JWT token (that is naive)
      return localStorage.getItem('jwtoken') != null;
    },
    submit_talk: function(subject, summary) {
      this.$http.post('/Plone/talks',
                 {'@type':'talk',
                  'type_of_talk':'Lightning Talk',
                  'audience':['Beginner','Advanced','Professionals'],
                  'title':subject,
                  'description':summary},
                 {headers:
                  {'Content-type':'application/json',
                   'Authorization': 'Bearer ' + localStorage.getItem('jwtoken'),
                   'Accept':'application/json'}}).
        then(function(response){
          if(response.status === 201) { // created
            this.load_talks();
          }
        }, function(error){
          // according to docs, status can be 400 or 500
          // we check wether the token has expired - in this case,
          // we remove it from localStorage and disply the login page.
          // In all other cases, we display the message received
          // from Plone
          if ( (error.status == 400) && (error.data.type == 'ExpiredSignatureError') ) {
            localStorage.removeItem('jwtoken');
            location.reload();
          } else {
            // reason/error msg is contained in response body
            alert(error.message);
          }
        });
    },
    load_talks: function() {
      this.$http.get('/Plone/talks',
                {headers:{'Accept':'application/json'}}).
        then(function(response) {
          this.items = [];
          // get the paths of the talks
          var paths = [];
          for (var i=0; i < response.data.items_total; i++) {
            paths.push(response.data.items[i]['@id'])
          }
          // next get details for each talk
          for (var i=0; i < paths.length; i++) {
            this.$http.get(paths[i],
                      {headers:{'Accept':'application/json'}}).
              then(function(resp) {
                // this is an angular 'promise' - we cannot
                // rely on variables from an outer scope
                var talkdata = resp.data;
                var path = talkdata['@id'];
                var talk = {
                  'pos': paths.indexOf(path),
                  'path': path,
                  'title': talkdata.title,
                  'type': talkdata.type_of_talk,
                  'speaker': (talkdata.speaker != null) ? talkdata.speaker : talkdata.creators[0],
                  'start': talkdata.start,
                  'subjects': talkdata.subjects,
                  'details': (talkdata.details != null) ? talkdata.details.data : talkdata.description
                }
                this.items.push(talk);

              },
              function(error) {});
          }
        },
        function(error) {
          this.items = [];
      });
    }
  },

  mounted: function() {
    // initialize
    this.load_talks();
  }
});
