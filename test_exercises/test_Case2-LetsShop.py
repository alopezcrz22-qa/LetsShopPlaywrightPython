from idlelib import browser

from playwright.sync_api import Playwright, expect



##########The user add product not available in inventory.##################
def test_Case1LetsShop(playwright:Playwright):
    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    # Abrir una nueva page
    page = context.new_page()

    # Login Page
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    # Localiza el campo de correo por su ID '#userEmail' e ingresa el email correspondiente
    page.locator('#userEmail').fill('alanbarc614@gmail.com')
    # Localiza el campo de contraseña por su ID '#userPassword' e ingresa la contraseña
    page.locator('#userPassword').fill('.$vcMuTCM8G$pY!')
    # Busca el botón de inicio de sesión usando el atributo CSS selector `input[id='login']` y le da clic
    page.locator("input[id='login']").click()

    #DashboardPage

    #Ahora localizamos el elemento Cart y damos click
    #Es importante cuando un elemento se encuentra en una seccion, localizemos primero la seccion
    page.get_by_role("navigation").get_by_role("button",name="  Cart ").click()

    #Valida el mensaje de no hay productos en tu carrito
    #confirmationMessage =  page.locator("h1[class='hero-primary']").text_content()
    expect(page.get_by_text("No Products in Your Cart !")).to_have_text('No Products in Your Cart !')
