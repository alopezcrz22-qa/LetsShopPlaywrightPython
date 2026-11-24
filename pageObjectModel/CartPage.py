#from rootFileName import className
from playwright.sync_api import expect

from pageObjectModel.CompleteOrderPage import CompleteOrderPage

#Definimos el nombre de la clase
class CartPage:
    #Definimos un constructor que recibira los parametros self(clase) page(de la nueva pagina)
    def __init__(self,page):
        self.page = page

        # CartPage
        # Definimos variables de instancia la cuales sera nuestro locators elements
        # self.myElement = page.locatorElements

        # Ahora localizamos el elemento Comprar Ahora  y damos click
        self.btnBuyNow = page.get_by_role('button', name="Buy Now")

        # Ahora localizamos el elemento Checkout  y damos click
        # page.locator(".items").filter(has_text='ADIDAS ORIGINAL').get_by_role('button', name="Buy Now").click()
        self.btnCheckout = page.get_by_role("button", name="Checkout")

        # Valida el mensaje de no hay productos en tu carrito
        # confirmationMessage =  page.locator("h1[class='hero-primary']").text_content()
        #expect(self.page.get_by_text("No Products in Your Cart !")).to_have_text('No Products in Your Cart !')
        self.messageCart = page.get_by_text("No Products in Your Cart !")

    def validate_messageCart(self):
        # Valida el mensaje de no hay productos en tu carrito
        # confirmationMessage =  page.locator("h1[class='hero-primary']").text_content()
        #expect(self.page.get_by_text("No Products in Your Cart !")).to_have_text('No Products in Your Cart !')
        return self.messageCart

    def go_to_checkoutPage(self):
        self.btnCheckout.click()
        completeOrderPage = CompleteOrderPage(self.page)
        return completeOrderPage

    def go_to_completeOrderPage(self):
        # Da click al boton place order
        self.btnBuyNow.click()
        completeOrderPage= CompleteOrderPage(self.page)
        return completeOrderPage





