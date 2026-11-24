# Definimos el nombre de la clase
class ConfirmationPage:
    # Definimos un constructor que recibira los parametros self(clase) page(de la nueva pagina)
    def __init__(self, page):
        self.page = page
        # Login Page

        # Definimos variables de instancia la cuales sera nuestro locators elements
        # self.myElement = page.locatorElements
        ####Confirmation Page
        # Valida el mensaje de confirmacion de compra
        # confirmationMessage =  page.locator("h1[class='hero-primary']").text_content()
        #expect(page.get_by_text(' Thankyou for the order. ')).to_have_text(' Thankyou for the order. ')
        self.confirmationMessage = page.get_by_text(' Thankyou for the order. ')
        # Valida que se genereo una orden de compra
        #expect(page.locator("label[class*=ng-star]")).to_be_visible()
        self.confirmationId = page.locator("label[class*=ng-star]")

    def confirmation_Message(self):
        confirmationMessage = self.page.get_by_text(' Thankyou for the order. ')
        return confirmationMessage
        #return confirmationMessage

    def confirmation_Id(self):
        confirmationId = self.page.locator("label[class*=ng-star]")
        return confirmationId
        #return self.confirmationId

