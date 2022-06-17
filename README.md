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

# Creating superuser. Give him username and password
python manage.py createsuperuser

# Create crontab jobs
python manage.py crontab add
