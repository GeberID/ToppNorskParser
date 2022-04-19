# Парсер сайта Toppnorsk для удобного сохранения слов в файлы для последующей загрузки в quizlet
from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver:
    # Инициализируем драйвер для работы с сайтом
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                                                 'plugins': 2, 'popups': 2, 'geolocation': 2,
                                                                 'notifications': 2, 'auto_select_certificate': 2,
                                                                 'fullscreen': 2,
                                                                 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                                 'media_stream_mic': 2, 'media_stream_camera': 2,
                                                                 'protocol_handlers': 2,
                                                                 'ppapi_broker': 2, 'automatic_downloads': 2,
                                                                 'midi_sysex': 2,
                                                                 'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                                 'metro_switch_to_desktop': 2,
                                                                 'protected_media_identifier': 2, 'app_banner': 2,
                                                                 'site_engagement': 2,
                                                                 'durable_storage': 2}}
        self.options.add_experimental_option('prefs', self.prefs)
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=self.options)
        # Добавляем переменные для работы с сайтом и со словами
        self.site = None
        self.wordsList = {}
        self.word = None
        self.definition = None
        self.definitionList = {}
        self.file = None
        self.numberFiles = 0
        self.numberWords = 0
        self.iteration = 0

    # Переход на сайт
    def goToTheSite(self, site):
        self.driver.get(site)

    # Находим слова и сохраняем в словарь
    def closrSite(self):
        self.driver.quit()

    def findWords(self):
        for i in range(1000):
            try:
                # Передаем в переменные найденные слова и выражения и из выражения удаляем ранее найденное слово
                # Потому что в выражение парсится слово - выражение и для добавления в словарь нам это не нужно
                self.word = (self.driver.find_element(By.XPATH,
                                                      f'/html/body/div[1]/div/div[1]/main/article/div/div/p[{i + 2}]/strong').text)
                self.definition = (self.driver.find_element(By.XPATH,
                                                            f'/html/body/div[1]/div/div[1]/main/article/div/div/p[{i + 2}]').text)
                self.definition = self.definition.replace(self.word + '\n', '', 1)
                self.wordsList[i] = self.word
                self.definitionList[i] = self.definition
            except:
                break

    def printWordList(self):
        for i in range(1000):
            try:
                print(self.wordsList[i])
            except:
                pass

    # Парсим словарь для того, чтобы определить какие данные закачивать в файлы и сколько файлов создавать"""

    def parseDict(self):
        self.numberWords = len(self.wordsList)
        self.numberFiles = self.numberWords // 10
        if self.numberWords % 10 != 0:
            self.numberFiles += 1

    # Создаю файл по 10 слов и записываю в него данные из списка в формате
    # Ключ|значение
    # Сохраняю файл. Если в файл не умещается 10 слов, то записываю столько, сколько файло надо, чтобы уместить 10 слов +
    # создаю файл с остатком слов

    def createFile(self):
        self.parseDict()
        for i in range(self.numberFiles):
            self.file = open(f"Part{i}.txt", 'w')
            for y in range(10 + self.iteration):
                y = y + self.iteration
                try:
                    self.writeInfoInFile(self.file, y)
                except:
                    pass
            self.iteration += 10

    def writeInfoInFile(self, file, i):
        file.write(self.wordsList[i] + "|" + self.definitionList[i] + "\n\n")


parseSite = Driver();
parseSite.goToTheSite("https://toppnorsk.com/2021/10/24/stor-samling-norske-uttrykk/")
try:
    parseSite.findWords()
    # fixture.printWordList()
    parseSite.createFile()
except:
    print("I can't find elements")
parseSite.closrSite()
