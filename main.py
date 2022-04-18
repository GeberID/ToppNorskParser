#Парсер сайта Toppnorsk для удобного сохранения слов в файлы для последующей загрузки в quizlet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
class Driver:
#Инициализируем драйвер для работы с сайтом
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=self.options)
#Добавляем переменные для работы с сайтом и со словами
        self.site = None
        self.wordsList = {}
        self.word = None
        self.definition = None
#Переход на сайт.
    def goToTheSite(self,site):
        self.driver.get(site)

#Находим слова и сохраняем в словарь
    def closrSite(self):
        self.driver.close()
    def findWords(self):
        try:
            for i in range(1000):
                try:
#Передаем в переменные найденные слова и выражения и из выражения удаляем ранее найденное слово.
#Потому что в выражение парсится слово - выражение и для добавления в словарь нам это не нужно

                    self.word=(self.driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[1]/main/article/div/div/p[{i+2}]/strong').text)
                    self.definition=(self.driver.find_element(By.XPATH,f'/html/body/div[1]/div/div[1]/main/article/div/div/p[{i+2}]').text)
                    self.definition.replace(self.word,'')
                    self.wordsList[self.word]==self.definition
                    print(self.word)
                    print(self.definition)
                    print(self.wordsList)
                except:
                    break
        except:
            print("I can't find elements")

    def printWordList(self):
        print(self.wordsList)

fixture = Driver();
fixture.goToTheSite("https://toppnorsk.com/2021/10/24/stor-samling-norske-uttrykk/")
fixture.findWords()
fixture.printWordList()
fixture.closrSite()