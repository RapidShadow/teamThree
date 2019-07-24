from models import User, Products
def seed_data():
    productLgoPnkHdie = Products(product_id = 1111, product_name = "Pink Logo Hoodie", product_status = " In Stock", product_price = "$20.00", product_image = "../assets/pinkhoodie.png" ,product_keywords = ["HOODIE","PINK"]).put()
    productLgoGrnSwtr = Products(product_id = 3333, product_name = "Green Logo Sweather", product_status = "In Stock", product_price = "$15.00", product_image = "../assets/greensweather.png", product_keywords = ["SWEATHER","GREEN"]).put()
    productLgoWhtTsht = Products(product_id = 2222, product_name = "White Logo T-shirt", product_status = " In Stock", product_price = "$10.00", product_image = "../assets/whitetshirt.png" ,product_keywords = ["WHITE","T-SHIRT"]).put()
    productLgoAirpods = Products(product_id = 4444, product_name = "White Logo Airpods", product_status = "Out of Stock", product_price = "$160.00", product_image = "../assets/airpods.png", product_keywords = ["WHITE","AIRPODS"]).put()
    productLgoPnkHdie = Products(product_id = 5555, product_name = "White Logo Hoodie", product_status = " In Stock", product_price = "$20.00", product_image = "../assets/whitehoodie.png" ,product_keywords = ["HOODIE","WHITE"]).put()
