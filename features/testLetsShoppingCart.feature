#Describe la funcionalidad
Feature: Online Shop
  # Como cliente de la tienda online
  # Quiero agregar productos al carrito
  # Para realizar compras de manera segura

#Precondiciones
  Background:
    Given the user is logged into the online store with "alanbarc614@gmail.com" and ".$vcMuTCM8G$pY!"

#Caso de prueba individual
  Scenario Outline: The user complete an Successful purchase
  #Estado Inicial
    Given the user is on the dashboard page
  #Accion del usuario
    When user add <itemsAddToCart> in to the cart
    And Complete the order purchase
  #Resultadp esperado
    Then the order should be successfully created
    #And an order confirmation number should be generated
    Examples:
    | itemsAddToCart       |
    | ADIDAS ORIGINAL      |

#Caso de prueba individual
  Scenario:The user add product not available in inventory.
  #Estado Inicial
    Given the user is on the dashboard page
  #Accion del usuario
    When user dont agregate product in to the cart
  #Resultadp esperado
    Then the order message "No Products in Your Cart !" should be displayed

#Caso de prueba individual
  Scenario Outline: The user has a valid coupon and must apply a discount.
  #Estado Inicial
    Given the user is on the dashboard page
    And the user add <itemsAddToCart> in to the cart coupon
  #Accion del usuario
    When the user enter a <coupon> in to the Order page
  #Resultadp esperado
    Then should message "* Coupon Applied" be displayed in the order
    And the order should be successfully created
    Examples:
    | itemsAddToCart       | coupon             |
    | ADIDAS ORIGINAL      | rahulshettyacademy |

#Caso de prueba individual
  Scenario Outline: The user has a invalid coupon
  #Estado Inicial
    Given the user is on the dashboard page
    And the user add <itemsAddToCart> in to the cart coupon
  #Accion del usuario
    When the user enter a <coupon> in to the Order page
  #Resultadp esperado
   #Resultadp esperado
    Then should message "* Invalid Coupon" be displayed in the order
    And the order should be successfully created
    Examples:
    | itemsAddToCart       | coupon              |
    | ADIDAS ORIGINAL      | academiaderalshetty |


#Caso de prueba individual
  Scenario Outline: The user can add multiple products to the cart.
  #Accion del usuario
    Given the user is on the dashboard page
  #Resultadp esperado
    When the user add <itemsAddToCart> in to the cart
    And Complete the order purchase
  #Resultadp esperado
    Then the order should be successfully created
    | itemsAddToCart                                   |
    | ADIDAS ORIGINAL, ZARA COAT 3, iphone 13 pro      |


