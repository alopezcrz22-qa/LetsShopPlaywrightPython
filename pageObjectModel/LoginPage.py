# from rootFileName import className
from pageObjectModel.DashboardPage import DashboardPage


# Definimos el nombre de la clase
class LoginPage:
    # Definimos un constructor que recibira los parametros self(clase) page(de la nueva pagina)
    def __init__(self, page):
        self.page = page
        # Login Page

        # Definimos variables de instancia la cuales sera nuestro locators elements
        # self.myElement = page.locatorElements

        # Localiza el campo de correo por su ID '#userEmail' e ingresa el email correspondiente
        # page.locator('#userEmail').fill('alanbarc614@gmail.com')
        self.userEmail = page.locator('#userEmail')
        # Localiza el campo de contraseña por su ID '#userPassword' e ingresa la contraseña
        # page.locator('#userPassword').fill('.$vcMuTCM8G$pY!')
        self.userPassword = page.locator('#userPassword')
        # Busca el botón de inicio de sesión usando el atributo CSS selector `input[id='login']` y le da clic
        # page.locator("input[id='login']").click()
        #self.btnLogin = page.locator('#btnLogin')

    # Definimos la funcion "Ir a la pagina principal"
    # Se agrega aqui ya que siempre al momento de abrir la pagina estaremos en login
    def goto_login_page(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    # Definimos la funcion "Login"
    # def functionName(self[class], getparameters)
    def login_shop(self, userName, userPassword):
        # self.instanceVariables[constructor].action()
        self.userEmail.fill(userName)
        self.userPassword.fill(userPassword)

    def go_toDashboardPage(self):
        #self.btnLogin.click()
        self.page.locator("input[id='login']").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage