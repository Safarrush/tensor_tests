# Тестовое задание для компании "Тензор" - автотестирование

Целью данного проекта было создание автотеста, способного провести тест по трем заданным сценариям.

## Запуск всех сценариев теста c формированием отчета через скрипт:
# Windows

### 1) Склонировать репозиторий:
```
Клонировать репозиторий (git clone) и перейти в него в командной строке (cd)
```

### 2) Установить Java Runtime Environment (JRE):
```
- Перейдите на официальный сайт Oracle Java: https://www.oracle.com/java/technologies/javase-downloads.html
- В разделе "Java SE" выберите версию JRE для Windows. Обычно, рекомендуется выбирать последнюю стабильную версию.
- Принимайте лицензионное соглашение и выберите версию JRE для загрузки. В большинстве случаев это будет "Windows x64 Installer" для 64-разрядной версии Windows или "Windows x86 Installer" для 32-разрядной версии Windows.
- Загрузите установочный файл JRE с официального сайта Oracle. Это будет исполняемый файл с расширением ".exe".
- Запустите скачанный установочный файл и следуйте инструкциям мастера установки. По умолчанию, JRE будет установлена в каталог "C:\Program Files\Java".
```
### 3) Установить Node.js:
```
- Скачайте и установите Node.js с официального сайта: https://nodejs.org. После установки Node.js, npm (Node Package Manager) будет автоматически установлен.
```
### 4) Запустите скрипт через терминал:
```
./run_tests_windows.sh
```

# MacOS

### 1) Склонировать репозиторий:
```
Клонировать репозиторий (git clone) и перейти в него в командной строке (cd)
```

### 2) Установить Java Runtime Environment (JRE):
```
- Скачайте и установите JRE с официального сайта Java: http://www.java.com
```
### 3) Установить Node.js (можно через терминал):
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install node 
```
### 4) Запустите скрипт через терминал:
```
chmod +x run_tests_mac.sh
./run_tests_mac.sh
```

## Запуск всех сценариев теста в ручную (Windows):

### 1) Склонировать репозиторий:
Клонировать репозиторий (git clone) и перейти в него в командной строке (cd)

### 2) Создать и активировать виртуальное окружение для проекта
```
python -m venv venv
source venv/scripts/activate
```

### 3) Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
python pip install -r requirements.txt
```

### 4) Запустить тесты без формирования отчета
```
pytest -s -v tests/*.py
```

### 4) Запустить тесты с отчетом (заранее нужно установить доп.модули, по инструкции выше)
```
pytest tests/*.py --alluredir=./allure-results
npm install --save-dev allure-commandline
npx allure-commandline serve
```

# Об авторе
- Сафаргалеев Рушан
- Россия, г. Уфа
- E-mail: safargaleevrushan@yandex.ru
- Telegram: @safa_ru
