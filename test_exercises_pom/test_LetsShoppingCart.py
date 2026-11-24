#Importamos funcionalidad sync de PLaywright
from playwright.sync_api import Playwright, expect

#Importamos el root del objeto que creamos LoginPage, ya que este no viene precedida de ningun otra clase

from pageObjectModel.LoginPage import LoginPage

##########The user complete an Successful purchase##################
def test_Case1LetsShop(playwright:Playwright , browserInstance):
    # Creamos una variable browser que abrira(lanzara) el navegador
    #browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    #context = browser.new_context()
    # Abrir una nueva page
    #page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    #loginPage = LoginPage(page)
    loginPage = LoginPage(browserInstance)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    userName ='aalanlz210m@gmail.com'
    userPassword = '@reS1823'
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = ("ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro")
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
def test_Case2LetsShop(playwright:Playwright):
    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    # Abrir una nueva page
    page = context.new_page()

    # Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    loginPage = LoginPage(page)
    # Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    userName = 'aalanlz210m@gmail.com'
    userPassword = '@reS1823'
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
def test_Case3LetsShop(playwright:Playwright):
    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    # Abrir una nueva page
    page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    loginPage = LoginPage(page)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    userName ='aalanlz210m@gmail.com'
    userPassword = '@reS1823'
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = ("ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro")
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
    couponCode = "rahulshettyacademy"
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
def test_Case4LetsShop(playwright:Playwright):
    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    # Abrir una nueva page
    page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    loginPage = LoginPage(page)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    userName ='aalanlz210m@gmail.com'
    userPassword = '@reS1823'
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = ("ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro")
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
    couponCode = "academiaderahulshetty"
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
def test_Case5LetsShop(playwright:Playwright):
    # Creamos una variable browser que abrira(lanzara) el navegador
    browser = playwright.chromium.launch(headless=False)
    # Creamos un nuevo contexto que en este caso es abrir una nueva pestana sin cookies y sin ningun configuracion
    context = browser.new_context()
    # Abrir una nueva page
    page = context.new_page()

    #Creamos un objeto e instanciamos la clase la cual enviaremos el parametro Abrir una nueva pagina(page)
    loginPage = LoginPage(page)
    #Del objeto creado, mandamos a llamar el metodo "Ir a la pagina" de la clase login
    loginPage.goto_login_page()

    ######## #este metodo recibe parametros , entonces desde @test los enviamos
    userName ='aalanlz210m@gmail.com'
    userPassword = '@reS1823'
    loginPage.login_shop(userName, userPassword)

    #Al usar la funcionalidad POM, despues de una accion que nos llevara a la siguiente pagina
    #entonces instanciamos el objeto de la nueva pestana que en es caso seria dashboardPage
    dashboardPage = loginPage.go_toDashboardPage()

    # DashboardPage
    # Definimos una lista con los productos que vamos a agregar
    itemsAddToCart = ("ADIDAS ORIGINAL", "ZARA COAT 3", "iphone 13 pro")
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