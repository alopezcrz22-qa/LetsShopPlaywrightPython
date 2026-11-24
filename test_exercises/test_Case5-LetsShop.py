from asyncio import timeout

import state
from playwright.sync_api import Playwright, expect


##########The user can add multiple products to the cart.##################

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

    #Localiza la tarjeta que contiene los elementos del producto Title,imagen,resumen,precio
    cardProducts = page.locator("div[class='card']")
    #y de todas las card podemos localizar por el title exacto y realizar cualquie accion

    #Desde el localizador cardProducts filtra el elemento que contiene el texto
    itemsAddToCart = ["ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro"]
    #Una vez filtrado encuantra el boton y da click
    #se puede hacer filtro y extrae el texto o cualquier accion
    for oneitem in itemsAddToCart:
        cardProducts.filter(has_text=oneitem).get_by_role(
            "button",name=" Add To Cart").click()

    #Ahora localizamos el elemento Cart y damos click
    #Es importante cuando un elemento se encuentra en una seccion, localizemos primero la seccion
    page.get_by_role("navigation").get_by_role("button",name="  Cart ").click()

    # Ahora localizamos el elemento Comprar Ahora  y damos click
    #page.locator(".items").filter(has_text='ADIDAS ORIGINAL').get_by_role('button', name="Buy Now").click()
    page.get_by_role("button", name="Checkout").click()

    #CartPage
    #CSS select[class='input ddl']:nth-child(2)
    #XPATH (//select[@class='input ddl'])[1]

    #Acompleta la seccion de Datos personales
    #Selecciona la opcion cvv expirity date
    page.locator("(//select[@class='input ddl'])[1]").select_option('09')
    # Selecciona la opcion cvv expirity date
    page.locator("(//select[@class='input ddl'])[2]").select_option('31')
    #Agrega el numero de CVV
    page.locator("(//input[@class='input txt'])[1]").fill("230")
    #Agrega el nombre de la tarjeta
    page.locator("(//input[@class='input txt'])[2]").fill("ANGEL ALAN LOPEZ CRUZ")

    #Agrega el pais de compra
    #En Playwright (Python), locator.press_sequentially("Mexi", delay=150) escribe el texto "Mexi" carácter por carácter
    # dentro del elemento seleccionado, haciendo una pausa de 150 milisegundos entre cada pulsación de tecla ("M": 150ms, "e":150ms  "x":150ms "i":150).
    #Buscadores con autocompletado en tiempo real, campos con máscara personalizada o inputs que reaccionan tecla por tecla.
    page.get_by_placeholder("Select Country").press_sequentially('Mexi',delay=150)
    #y selecciona la opcion
    page.locator('.ta-results').locator("button[type='button']").filter(has_text=' Mexico').click()

    #Da click al boton place order
    page.locator("div[class='actions'] a").click()

    ####Confirmation Page
    #Valida el mensaje de confirmacion de compra
    #confirmationMessage =  page.locator("h1[class='hero-primary']").text_content()
    expect(page.get_by_text(' Thankyou for the order. ')).to_have_text(' Thankyou for the order. ')
    #Valida que se genereo una orden de compra, en este caso se generan 3 ordenes
    #expect(page.locator("label[class*=ng-star]")).to_be_visible()









