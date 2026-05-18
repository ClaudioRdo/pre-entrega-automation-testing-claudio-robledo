from utils.helpers import login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    login(
        driver,
        "standard_user",
        "secret_sauce"
    )
    # Validar URL
    assert (
        "inventory.html"
        in driver.current_url
    )
    # Validar Products
    title = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text
    assert title == "Products"
    # Validar título navegador
    assert "Swag Labs" in driver.title

def test_catalogo_productos(driver):
    login(
        driver,
        "standard_user",
        "secret_sauce"
    )
    title = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text
    assert title == "Products"

    # Buscar productos visibles
    productos = driver.find_elements(
        By.CSS_SELECTOR,
        "[data-test='inventory-item']"
    )
    assert len(productos) > 0

    # Obtener primer producto
    nombre = productos[0].find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text
    precio = productos[0].find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text
    print(
        f"\nPrimer producto: {nombre}"
    )
    print(
        f"Precio: {precio}"
    )

    # Verificar menú
    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )
    assert menu.is_displayed()

    # Verificar filtro
    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )
    assert filtro.is_displayed()
