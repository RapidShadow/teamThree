from google.appengine.ext import ndb

class User(ndb.Model):
    first_name =  ndb.StringProperty(required=True)
    last_name =  ndb.StringProperty(required=True)
    user_id = ndb.KeyProperty(required=True)
class Products(ndb.Model):
    product_id = ndb.IntegerProperty(required=True)
    product_name = ndb.StringProperty(required=True)
    product_status = ndb.StringProperty(required=True)
    product_price = ndb.StringProperty(required=True)
    product_image = ndb.StringProperty(required=False)
    product_keywords = ndb.JsonProperty(required=True)
