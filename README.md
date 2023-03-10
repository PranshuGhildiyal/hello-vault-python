# hello-vault-python sample_app

pip install -r requirements.txt

python -m django startproject sample_app .

python manage.py makemigrations sample_app

python manage.py migrate

python manage.py runserver

curl --location 'http://127.0.0.1:8000/api/product'
