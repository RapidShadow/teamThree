from models import User, Products
def seed_data():
    productLgoPnkHdie = Products(product_id = 1111, product_name = "Pink Logo Hoodie", product_status = " In Stock", product_price = "$20.00", product_image = "https://i.imgur.com/pKrPYYH.png" ,product_keywords = ["HOODIE","PINK"]).put()
    productLgoGrnSwtr = Products(product_id = 3333, product_name = "Green Logo Sweather", product_status = "In Stock", product_price = "$15.00", product_image = "https://i.imgur.com/JlClENF.png", product_keywords = ["SWEATHER","GREEN"]).put()
    productLgoWhtTsht = Products(product_id = 2222, product_name = "White Logo T-shirt", product_status = " In Stock", product_price = "$10.00", product_image = "https://i.imgur.com/gdPyPrn.png" ,product_keywords = ["WHITE","T-SHIRT"]).put()
