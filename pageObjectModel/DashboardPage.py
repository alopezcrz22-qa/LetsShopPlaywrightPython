#from rootFileName import className
from pageObjectModel.CartPage import CartPage


#Definimos el nombre de la clase
class DashboardPage:
    #Definimos un constructor que recibira los parametros self(clase) page(de la nueva pagina)
    def __init__(self,page):
        self.page = page
        # DashboardPage
        #Definimos variables de instancia la cuales sera nuestro locators elements
        #self.myElement = page.locatorElements

        # Localiza la tarjeta que contiene los elementos del producto Title,imagen,resumen,precio
        #cardProducts = page.locator("div[class='card']")
        self.cardProducts = page.locator("div[class='card']")
        # y de todas las card podemos localizar por el title exacto y realizar cualquie accion

        # Desde el localizador cardProducts filtra el elemento que contiene el texto
        #itemsAddToCart = "ADIDAS ORIGINAL"
        # Una vez filtrado encuantra el boton y da click
        # se puede hacer filtro y extrae el texto o cualquier accion
        #cardProducts.filter(has_text=itemsAddToCart).get_by_role(
        #    "button", name=" Add To Cart").click()

        # Ahora localizamos el elemento Cart y damos click
        # Es importante cuando un elemento se encuentra en una seccion, localizemos primero la seccion
        #page.get_by_role("navigation").get_by_role("button", name="  Cart ").click()
        self.btnCart = page.get_by_role("navigation").get_by_role("button", name="  Cart ")


    #Funcion basic, agregar un solo producto a mi carrito este metodo lo eliminaremos cuando agregemos
    #la configuracion del JSON
    def add_product_toCart(self, itemsAddToCart):
        # Desde el localizador cardProducts filtra el elemento que contiene el texto
        # itemsAddToCart = "ADIDAS ORIGINAL"
        # Una vez filtrado encuantra el boton y da click
        # se puede hacer filtro y extrae el texto o cualquier accion
        self.cardProducts.filter(has_text=itemsAddToCart[0]).get_by_role(
               "button", name=" Add To Cart").click()

    def add_products_toCart(self, itemsAddToCart):
        # Desde el localizador cardProducts filtra el elemento que contiene el texto
        #itemsAddToCart = ["ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro"]
        # Una vez filtrado encuantra el boton y da click
        # se puede hacer filtro y extrae el texto o cualquier accion
        for oneitem in itemsAddToCart:
            self.cardProducts.filter(has_text=oneitem).get_by_role(
                "button", name=" Add To Cart").click()

    def go_to_cart(self):
        self.btnCart.click()
        cartPage = CartPage(self.page)
        return cartPage

    #Definimos un metodo que validara si es solo un producto o varios , y conforme sea entrara a dicho statement
    #y hara la accion requerida
    def ifelse_add_products_toCart(self, itemsAddToCart,noProducts):
        if noProducts == 1:
            self.cardProducts.filter(has_text=itemsAddToCart).get_by_role(
                "button", name=" Add To Cart").click()

        elif noProducts >= 2:
            # Desde el localizador cardProducts filtra el elemento que contiene el texto
            #itemsAddToCart = ["ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro"]
            # Una vez filtrado encuantra el boton y da click
            # se puede hacer filtro y extrae el texto o cualquier accion
            for oneitem in itemsAddToCart:
                self.cardProducts.filter(has_text=oneitem).get_by_role(
                    "button", name=" Add To Cart").click()