#Importamos libreria json
import json
#Importamos libreria path
from pathlib import Path

import pytest
#Importamos funcionalidad sync de PLaywright
from playwright.sync_api import Playwright, expect

#Importamos el root del objeto que creamos LoginPage, ya que este no viene precedida de ningun otra clase
from pageObjectModel.LoginPage import LoginPage

# Construye la ruta absoluta hacia el archivo 'credentials.json', subiendo dos niveles desde el archivo actual y entrando a la carpeta 'data'
credentials_path = Path(__file__).resolve().parent.parent / 'dataset' / 'credentials.json'
# Abre el archivo JSON en modo lectura con codificación UTF-8 y carga su contenido como un diccionario de Python
with credentials_path.open(encoding='utf-8') as f:
    test_data = json.load(f)
# Extrae la lista de credenciales de usuario desde el diccionario cargado
user_credentials_list = test_data['user_credentials']


##########The user complete an Successful purchase##################
# Parametriza la prueba para que Pytest la ejecute una vez por cada juego de credenciales en la lista
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case1LetsShop(playwright:Playwright ,browserInstance , user_credentials, request):
    #Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    #browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    #context = browser.new_context()
    # Abrir una nueva page
    #page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    #En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    #userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    #Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    #Para extraer únicamente el primer elemento de la lista itemsAddToCart, debes agregar el índice [0] al acceder al diccionario:
    itemsAddToCart =user_credentials['itemsAddToCart'][1]
    # del objeto ya creado de dashboard page, inicializamos el method de agregar productos al carrito
    dashboardPage.add_product_toCart(itemsAddToCart)
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En CartPage, damos clic al boton Buy
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria completeOrderPage
    completeOrderPage = cartPage.go_to_completeOrderPage()

    # CompleteOrderPage
    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_orderForm()
    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria confirmationPage
    confirmationPage = completeOrderPage.go_to_confirmPage()

    # ConfirmationPage
    # En CompleteOrderPage, guardamos el valor que nos retorno el mensaje confirmationMessage
    confirmationMessage = confirmationPage.confirmation_Message()
    #y validamos si este contiene el texto definido por el equipo de diseno
    expect(confirmationMessage).to_have_text(' Thankyou for the order. ')

    # En CompleteOrderPage, guardamos el valor que nos retorno de la funcion
    # el ID Order
    confirmationId = confirmationPage.confirmation_Id()
    # y validamos si es visible el ID Order
    expect(confirmationId).to_be_visible()

##########The user add product not available in inventory.##################
# Parametriza la prueba para que Pytest la ejecute una vez por cada juego de credenciales en la lista
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case2LetsShop(playwright:Playwright, browserInstance, user_credentials):
    # Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    # browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    # context = browser.new_context()
    # Abrir una nueva page
    # page = context.new_page()

    # Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    # En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    # Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    # userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    # Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En cartpage, como no agregamos ningun producto  validamos si se muestra el mensaje de no hay prodcutos
    #en el carrito
    cartPage.validate_messageCart()

##########The user has a valid coupon and must apply a discount.##################
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case3LetsShop(playwright:Playwright,browserInstance, user_credentials,request):
    # Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    # browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    # context = browser.new_context()
    # Abrir una nueva page
    # page = context.new_page()

    # Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    # En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    # Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    # userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    # Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = user_credentials['itemsAddToCart']
    # del objeto ya creado de dashboard page, inicializamos el method de agregar productos al carrito
    dashboardPage.add_product_toCart(itemsAddToCart)
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En CartPage, damos clic al boton Buy
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria completeOrderPage
    completeOrderPage = cartPage.go_to_completeOrderPage()

    # CompleteOrderPage
    #Definimos los valores ascii en el formulario
    expirityDay = '12'
    expirityYear = '31'
    cvvField = '900'
    cardName = 'ANGEL SEBASTIAN LOPEZ'
    # En CompleteOrderPage, damos completamos el formulario de datos personales(tarjeta)
    completeOrderPage.complete_cardForm(expirityDay, expirityYear, cvvField, cardName)

    #Definimos el valor del coupon
    #En este caso extraemos el valor de couponCode del JSON, posicion 0
    couponCode = user_credentials['couponCode'][0]
    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_couponForm(couponCode)

    #Guarda en una variable el retorno del valor del mensaje si el cupon es valido o falso
    messageCoupon = completeOrderPage.validate_couponCode()
    # Valida si el valor del coupon, tiene el valor correcto
    expect(messageCoupon).to_be_visible()
    expect(messageCoupon).to_have_text("* Coupon Applied")

    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_orderForm()

    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria confirmationPage
    confirmationPage = completeOrderPage.go_to_confirmPage()

    # ConfirmationPage
    # En CompleteOrderPage, guardamos el valor que nos retorno el mensaje confirmationMessage
    confirmationMessage = confirmationPage.confirmation_Message()
    #y validamos si este contiene el texto definido por el equipo de diseno
    expect(confirmationMessage).to_have_text(' Thankyou for the order. ')

    # En CompleteOrderPage, guardamos el valor que nos retorno de la funcion
    # el ID Order
    confirmationId = confirmationPage.confirmation_Id()
    # y validamos si es visible el ID Order
    expect(confirmationId).to_be_visible()


##########The user has a invalid coupon##################
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case4LetsShop(playwright:Playwright, user_credentials, browserInstance, request):
    # Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    # browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    # context = browser.new_context()
    # Abrir una nueva page
    # page = context.new_page()

    # Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    # En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    # Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    # userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    # Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = user_credentials['itemsAddToCart']
    # del objeto ya creado de dashboard page, inicializamos el method de agregar productos al carrito
    dashboardPage.add_product_toCart(itemsAddToCart)
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En CartPage, damos clic al boton Buy
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria completeOrderPage
    completeOrderPage = cartPage.go_to_completeOrderPage()

    # CompleteOrderPage
    #Definimos los valores ascii en el formulario
    expirityDay = '12'
    expirityYear = '31'
    cvvField = '900'
    cardName = 'ANGEL SEBASTIAN LOPEZ'
    # En CompleteOrderPage, damos completamos el formulario de datos personales(tarjeta)
    completeOrderPage.complete_cardForm(expirityDay, expirityYear, cvvField, cardName)

    #Definimos el valor del coupon
    couponCode = user_credentials['couponCode'][1]
    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_couponForm(couponCode)

    #Guarda en una variable el retorno del valor del mensaje si el cupon es valido o falso
    messageCoupon = completeOrderPage.validate_couponCode()
    # Valida si el valor del coupon, tiene el valor correcto
    expect(messageCoupon).to_be_visible()
    expect(messageCoupon).to_have_text("* Invalid Coupon")

    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_orderForm()

    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria confirmationPage
    confirmationPage = completeOrderPage.go_to_confirmPage()

    # ConfirmationPage
    # En CompleteOrderPage, guardamos el valor que nos retorno el mensaje confirmationMessage
    confirmationMessage = confirmationPage.confirmation_Message()
    #y validamos si este contiene el texto definido por el equipo de diseno
    expect(confirmationMessage).to_have_text(' Thankyou for the order. ')

    # En CompleteOrderPage, guardamos el valor que nos retorno de la funcion
    # el ID Order
    confirmationId = confirmationPage.confirmation_Id()
    # y validamos si es visible el ID Order
    expect(confirmationId).to_be_visible()


##########The user can add multiple products to the cart.##################
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case5LetsShop(playwright:Playwright, user_credentials , browserInstance, request):
    # Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    # browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    # context = browser.new_context()
    # Abrir una nueva page
    # page = context.new_page()

    # Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    # En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    # Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    # userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    # Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = user_credentials['itemsAddToCart']
    # del objeto ya creado de dashboard page, inicializamos el method de agregar productos al carrito
    dashboardPage.add_products_toCart(itemsAddToCart)
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En CartPage, damos clic al boton Buy
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria completeOrderPage
    completeOrderPage = cartPage.go_to_checkoutPage()

    # CompleteOrderPage
    # En CompleteOrderPage, damos completamos el formulario de direccion de envio
    completeOrderPage.complete_orderForm()
    # Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria confirmationPage
    confirmationPage = completeOrderPage.go_to_confirmPage()

    # ConfirmationPage
    # En CompleteOrderPage, guardamos el valor que nos retorno el mensaje confirmationMessage
    confirmationMessage = confirmationPage.confirmation_Message()
    #y validamos si este contiene el texto definido por el equipo de diseno
    expect(confirmationMessage).to_have_text(' Thankyou for the order. ')

    #Ya no validamos porque se generan 3 IDs
    # En CompleteOrderPage, guardamos el valor que nos retorno de la funcion
    # el ID Order
    #confirmationId = confirmationPage.confirmation_Id()
    # y validamos si es visible el ID Order
    #expect(confirmationId).to_be_visible()




##########Using method > Agregar uno o varios Productos##################
# Parametriza la prueba para que Pytest la ejecute una vez por cada juego de credenciales en la lista
@pytest.mark.parametrize('user_credentials', user_credentials_list, indirect=True)
def test_Case6_methodProducts(playwright:Playwright ,browserInstance , user_credentials, request):
    #Eliminamos el context,browser y page ya que estaremos ejecutando esta funcionalidad en conftest.py
    # Creamos una variable browser que abrira(lanzara) el navegador
    #browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    #context = browser.new_context()
    # Abrir una nueva page
    #page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    #En este caso recibira broswer
    loginPage = LoginPage(browserInstance)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    #userName(valor del metodo) = user_credentials(valor de la lista)['username'(valor del archiv json)]
    userName = user_credentials['userName']
    userPassword = user_credentials['userPassword']

    #Mandamos a llamar el metodo de completar el usuario y la contrasena
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    #Para extraer únicamente el primer elemento de la lista itemsAddToCart, debes agregar el índice [0] al acceder al diccionario:
    itemsAddToCart =user_credentials['itemsAddToCart']
    # del objeto ya creado de dashboard page, inicializamos el method de agregar productos al carrito
    dashboardPage.ifelse_add_products_toCart(itemsAddToCart,3)
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria cartPage
    cartPage = dashboardPage.go_to_cart()

    #CartPage
    #En CartPage, damos clic al boton Buy
    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    # entonces instanciamos el objeto de la nueva pestana que en es caso seria completeOrderPage
    completeOrderPage = cartPage.go_to_checkoutPage()
