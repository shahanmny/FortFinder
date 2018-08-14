import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch


the_jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template = the_jinja_env.get_template("Templates/index.html")
        self.response.write(index_template.render())

    def post(self):
        self.response.write('hi')

class StatsHandler(webapp2.RequestHandler):
    def get(self):
        stats_template = the_jinja_env.get_template("Templates/stats.html")
        self.response.write(stats_template.render())
        #for question_dict in trivia_as_json['results']:
        #            self.response.write(question_dict['question'])
        #            self.response.write(question_dict['correct_answer'])
        #            self.response.write('<br><br>')

    def post(self):
        stats_template = the_jinja_env.get_template("Templates/stats.html")
        headers = {'TRN-Api-Key': '44231534-d4ed-41fc-8e82-99ea6733085e'}
        platform = self.request.get('platform')
        username = self.request.get('username')
        game = self.request.get('games')
        fortnite_response = urlfetch.fetch("https://api.fortnitetracker.com/v1/profile/" + platform + "/" + username, headers = headers).content
        fortnite_dict = json.loads(fortnite_response)
        #for lifeTimeStats in fortnite_dict['Stats']
        #    for kills in lifeTimeStats['Kills']

        kills = {}
        wins = {}
        matches = {}
        win_percentage = {}
        kill_death = {}
        for each_stat in fortnite_dict['lifeTimeStats']:
            if each_stat['key'] == "Kills":
                kills = each_stat
            if each_stat['key'] == "Wins":
                wins = each_stat
            if each_stat['key'] == "Matches Played":
                matches = each_stat
            if each_stat['key'] == "Win%":
                win_percentage = each_stat
            if each_stat['key'] == "K/d":
                kill_death = each_stat

        var_dict = {
            "kills": kills['value'],
            "wins": wins['value'],
            "matches": matches['value'],
            "win_percentage": win_percentage['value'],
            "k_d": kill_death['value']
        }

        self.response.write(stats_template.render(var_dict))

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/stats', StatsHandler)
], debug=True)
