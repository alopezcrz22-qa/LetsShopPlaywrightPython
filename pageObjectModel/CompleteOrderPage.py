# from rootFileName import className
from playwright.sync_api import expect

from pageObjectModel.ConfirmationPage import ConfirmationPage


# Definimos el nombre de la clase
class CompleteOrderPage:
    # Definimos un constructor que recibira los parametros self(clase) page(de la nueva pagina)
    def __init__(self, page):
        self.page = page

        # CartPage
        # En este caso para demostrar que se pueden
        # Definir variables y realizar la accion en las metodos(funciones), sin tener que agregar
        # en el constructor
        # self.page.locators("xpath,css,getbyrole,getbyplaceholder").action()

    def complete_cardForm(self, expirityDay, expirityYear, cvvField, cardName):
        # Acompleta la seccion de Datos personales
        # Selecciona la opcion cvv expirity date
        # self.page.locator("(//select[@class='input ddl'])[1]").select_option('09')
        self.page.locator("(//select[@class='input ddl'])[1]").select_option(expirityDay)

        # Selecciona la opcion cvv expirity Age
        # self.page.locator("(//select[@class='input ddl'])[2]").select_option('31')
        self.page.locator("(//select[@class='input ddl'])[2]").select_option(expirityYear)

        # Agrega el numero de CVV
        # self.page.locator("(//input[@class='input txt'])[1]").fill("230")
        self.page.locator("(//input[@class='input txt'])[1]").fill(cvvField)

        # Agrega el nombre de la tarjeta
        # self.page.locator("(//input[@class='input txt'])[2]").fill("ANGEL ALAN LOPEZ CRUZ")
        self.page.locator("(//input[@class='input txt'])[2]").fill(cardName)

    def complete_couponForm(self, couponCode):
        # Agrega un cupon
        # self.page.locator("input[name='coupon']").fill("rahulshettyacademia")
        self.page.locator("input[name='coupon']").fill(couponCode)

        # Da click al buton "Apply Coupon"
        self.page.get_by_role("button", name="Apply Coupon").click()

    def validate_couponCode(self):
        # Valida si es correcto el cupon aplicado
        messageCoupon = self.page.locator("p[class*='mt-1']")
        return messageCoupon

        # expect(messageCoupon).to_be_visible()
        # expect(messageCoupon).to_have_text("* Invalid Coupon")

    def complete_orderForm(self):
        # Agrega el pais de compra
        # En Playwright (Python), locator.press_sequentially("Mexi", delay=150) escribe el texto "Mexi" carácter por carácter
        # dentro del elemento seleccionado, haciendo una pausa de 150 milisegundos entre cada pulsación de tecla ("M": 150ms, "e":150ms  "x":150ms "i":150).
        # Buscadores con autocompletado en tiempo real, campos con máscara personalizada o inputs que reaccionan tecla por tecla.
        self.page.get_by_placeholder("Select Country").press_sequentially('Mexi', delay=150)

        # y selecciona la opcion
        self.page.locator('.ta-results').locator("button[type='button']").filter(has_text=' Mexico').click()

    def go_to_confirmPage(self):
        # Da click al boton place order
        self.page.locator("div[class='actions'] a").click()
        confirmationPage = ConfirmationPage(self.page)
        return confirmationPage





