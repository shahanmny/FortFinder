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
<<<<<<< HEAD
        header = {'TRN-Api-Key': '44231534-d4ed-41fc-8e82-99ea6733085e'}
=======
        headers = {'TRN-Api-Key': '44231534-d4ed-41fc-8e82-99ea6733085e'}
>>>>>>> 3ee4a390c5b4e0ab255114c0dce97927bbf6025c
        platform = "pc"
        username = "Ninja"
        fortnite_response = urlfetch.fetch("https://api.fortnitetracker.com/v1/profile/" + platform + "/" + username, headers = headers).content
        fortnite_dict = json.loads(fortnite_response)
        self.response.write(fortnite_dict['lifeTimeStats'])

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/stats', StatsHandler)
], debug=True)
