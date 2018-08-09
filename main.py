import webapp2
import jinja2
import os

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
        #fortnite_response = urlfetch.fetch("https://url").content

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/stats', StatsHandler)
], debug=True)
