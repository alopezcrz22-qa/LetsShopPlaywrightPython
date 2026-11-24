#Este archivo se centrara en guardar y compartir fixtures,hooks,configuraciones globalmente
#el archivo por default lo nombraremos conftest.py
from urllib import request

import pytest

# Hook de pytest para agregar un argumento personalizado a la línea de comandos
#Este hook proviene de la pagina oficial de pytest
#https://docs.pytest.org/en/stable/example/simple.html

#Ejecuta el archivo en especifico y ejecutalo en un navegador y en el ambiente
#ya definidos en el archivo global conftest
#pytest testAdvance/test_LetsShopConfigTest.py --browser_name firefox --ur_name SIT
def pytest_addoption(parser):
  parser.addoption(
      '--browser_name',
      action='store',
      default='chrome',
      help='Especifica el tipo de navegador (ej. chrome, firefox)',
  )
  parser.addoption(
      '--url_name',
      action='store',
      default='SIT',
      help='Especifica el ambiente en el que se esta ejecutando (ej. SIT, UAT, PERF)'
  )

# Fixture para manejar credenciales de usuario parametrizadas a nivel de sesión
#Uso en el archivo de JSON

#Este scope se ejecutara en sesion, una sola vez para todaos los test de la sesion que usen dicho fixture
@pytest.fixture(scope='session')
#request: Es una fixture interna de Pytest que contiene el contexto de la prueba que se está ejecutando en ese momento.
def user_credentials(request):
    # request.param: Accede al valor actual que se está iterando dentro de una lista de parámetros.
    return request.param


# Fixture para inicializar y gestionar el ciclo de vida y eleccion del navegador con Playwright
@pytest.fixture
def browserInstance(playwright, request):
#Definimos una variable global browser que nos permitira usar dicha variable dentro de
# ciclos,funciones que pertenezcan aqui
  global browser
  # Obtiene y define el valor del argumento '--browser_name' pasado desde la línea de comandos
  #parser.addoption
  browser_name = request.config.getoption('browser_name')

  # Obtiene  y define el valor del argumento '--url_name' pasado desde la línea de comandos
  #url_name = request.config.getoption('--url_name')

  # Inicia el navegador correspondiente en modo con interfaz gráfica (headless=False)
  if browser_name == 'chrome':
    browser = playwright.chromium.launch(headless=False)
  elif browser_name == 'firefox':
    browser = playwright.firefox.launch(headless=False)
  # Crea un nuevo contexto de navegador aislado ya que es independiente a los navegadores
  context = browser.new_context()
  # Abre una nueva página/pestaña dentro del contexto
  page = context.new_page()

  # Indica la direccion del ambiente correspondiente
  #if url_name =='SIT':
  #  page.goto('https://www.sit.papel.com.mx')
  #elif url_name == 'UAT':
  #  page.goto('https://www.uat.papel.com.mx')
  #elif: url_name == 'PERF':
  #  page.goto('https://www.perf.papel.com.mx')

  # pausa este ficture > 'yield' entrega el comando
  # al test login envia el parametro page para que la prueba se ejecute
  yield page

  # Código de limpieza (teardown) que se ejecuta al terminar la prueba
  context.close()
  browser.close()