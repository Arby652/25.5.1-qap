import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'D:\arby6\Downloads\chromedriver\chromedriver.exe')

    # Переход на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    pytest.driver.find_element_by_id('email').send_keys('arby652@mail.ru')
    pytest.driver.find_element_by_id('pass').send_keys('Slamdunk123')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    assert pytest.driver.find_element_by_tag_name('h1').text == 'PetFriends'
    yield
    pytest.driver.quit()

def test_show_my_pets():

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element_by_id('email').send_keys('arby652@mail.ru')

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element_by_id('pass').send_keys('Slamdunk123')

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    assert pytest.driver.current_url == 'http://petfriends1.herokuapp.com/my_pets'

imagesS = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
namesS = pytest.driver.find_elements_by_css_selector('.card-deck .card-body .card-title')
descriptionsS = pytest.driver.find_elements_by_css_selector('.card-deck .card-body .card-text')

for i in range(len(namesS)):
   assert imagesS[i].get_attribute('src') != ''
   assert namesS[i].text != ''
   assert descriptionsS[i].text != ''
   assert ', ' in descriptionsS[i]
   parts = descriptionsS[i].text.split(", ")
   assert len(parts[0]) > 0
   assert len(parts[1]) > 0

# проверка таблицы питомцев
def test_table_my_pets():
   # Явное ожидание
   element = WebDriverWait(pytest.driver, 5).until( EC.presence_of_element_located((By.ID, "email")))
   pytest.driver.find_element_by_id('email').send_keys('Arby652@mail.ru')
   element = WebDriverWait(pytest.driver, 5).until( EC.presence_of_element_located((By.ID, "pass")))
   pytest.driver.find_element_by_id('pass').send_keys('Slamdunk123')

   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   pytest.driver.find_element_by_xpath('//a[contains(text(), "Мои питомцы")]').click()

   count_of_my_pets = pytest.driver.find_element_by_css_selector('div.\\.col-sm-4.left').text.split()

   all_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr')


   images = pytest.driver.find_elements_by_tag_name('img')
   value_of_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td')
   names = value_of_my_pets[::4]
   breed = value_of_my_pets[1:-1:4]
   age = value_of_my_pets[2:-1:4]

 # Присутствуют все питомцы
   for i in range(len(all_my_pets)):
      assert len(all_my_pets) is int(count_of_my_pets[(2)])

   # у половины питомцев есть фото,
   for i in range(len(all_my_pets)):
      assert len(images) / len(all_my_pets) > 0, 5

   # У всех питомцев есть имя, возраст и порода,
   for i in range(len(value_of_my_pets)):
      assert value_of_my_pets[i].text != ''

   # У всех питомцев разные имена,
   for i in range(len(names)):
      assert len(names) is len(set(names))