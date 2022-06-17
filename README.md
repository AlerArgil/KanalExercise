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