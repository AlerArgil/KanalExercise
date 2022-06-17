# Test
Testing exercise

# Create Enviroment
python3.X -m venv testenv

# Init Enviroment
source testenv/bin/activate

# Install all packages
pip install -r requirements.txt

# Copy content .env.example to .env and set database credentials
# Init migration
python manage.py migrate

# Set actual exchange rate
python manage.py set_exchange_rate

# Create crontab jobs
python manage.py crontab add

# Starting bot for notify delivery time
python manage.py start_bot


Для связи с гугл сервисами использовался сервис аккаунт. Получить данные от него можно при наличии доступа по ссылке(скачать и прописать в env место расположение)
https://drive.google.com/file/d/1uvEFea39T9TQJzpnDI86sjODzIK36jtJ/view?usp=sharing

Реализованы два способа получение информации из файла.
1. Через крон. Работает по умолчанию, обращается к файлу на предмет изменений каждую минуту
2. Через вебхук google drive. Для его реализации необходимо выполнить команду
python manage.py set_watcher
предварительно указав в env файле GOOGLE_HTTPS_URL_NOTIFY как актуальный https роут до /test/ на текущем проекте


сам файл для тестов доступен по ссылке
https://docs.google.com/spreadsheets/d/1wh19iNoT1nQx1EoeDXzlODoY5892NL2WoQPRhUgvoy4/edit?usp=sharing