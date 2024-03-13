from datetime import datetime

data_path: str = "C:\\Users\\achoudhary\\Desktop\\inSiteGPT\\data\\"
TIMESTAMP: datetime= datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
index_pattern: str = "my_product"
source=["ProductName","Description"]
field= "NameDescriptionVector"
k=10,
num_candidates=500