# the import section
import webapp2
import jinja2
import os

from models import User, Products
from seed_data import seed_data
# this initializes the jinja2 environment

the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


counter = 0
# the handler section
class HomeHandler(webapp2.RequestHandler): #homepage "/"
    def get(self):
        global counter
        if counter == 0:
            seed_data()
            counter += 1

        home_template = the_jinja_env.get_template('templates/home.html') #pulls in "home.html" template
        self.response.write(home_template.render()) #serves home.html template back to front-end

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Explore.html')
        self.response.write(about_template.render())

class StoreHandler(webapp2.RequestHandler):
    def get(self):
        store = Products.query().fetch()
        store_template = the_jinja_env.get_template("templates/shop.html")
        self.response.write(store_template.render({'store_info' : store}))
class SearchHandler(webapp2.RequestHandler):
    def get(self):
        searchkey = self.request.get("search")
        search = Products.query().fetch()
        # searchfiltered = search.filter(product_keywords == searchkey.upper())
        # search = Products.query(Products.product_keywords.IN([searchkey.upper()]))
        # return search
        search_template = the_jinja_env.get_template("templates/search.html")
        template_vars = { 'searchterm': search, "keyword" : searchkey }
        self.response.write(search_template.render(template_vars))
app = webapp2.WSGIApplication([
  ('/', HomeHandler),
  ('/about', AboutHandler),
  ('/store', StoreHandler),
  ('/search', SearchHandler),
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
