import webapp2
import jinja2
import os
import json


the_jinja_env = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template = the_ninja_env.get_template("Templates/index.html")
        self.response.write(index_template.render())

class StatsHandler(webapp2.RequestHandler):
    def get(self):
        header = {'TRN-Api-Key': '44231534-d4ed-41fc-8e82-99ea6733085e'}
        fortnite_response = urlfetch.fetch("https://api.fortnitetracker.com/v1/profile/" + platform + "/" + username, headers = headers).content
        run = requests.get(fortnite_response, header)
        platform = pc
        username = Ninja
        results = run.json()[lifeTimeStats]
        print(results)

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/stats', StatsHandler)
], debug=True)
