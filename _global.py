config = {
    "Database file":'',
    "Company name":"",
    "report dir":''
}

class store:
    def __init__(self,name:str,brand:str,alais:str,size:str,upc:str,sku:str) -> None:
        self .name = name
        self .brand = brand
        self .alais = alais
        self .size = size
        self .upc = upc
        self .sku = sku
    def get_name(self):
        return self.name
    def get_brand(self):
        return self.brand
    