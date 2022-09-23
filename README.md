## Project name: Hotel

## Cloning code:

## for HTTPS:

https://github.com/AkkiEldar/Hotels.git

## for SSH key:

git@github.com:AkkiEldar/Hotels.git

## Next steps:

### 1.Install venv in project:

#### python3 -m venv venv

### 2.Start virtualenv:

#### source venv/bin/activate

### 3.Installing all requirements:

#### pip install -r requirements.txt

### 4.need to add env vars: DATABASE_NAME ...

## To start project:
### 1)sudo su (+ your password)

### 2)docker-compose up --build(to building docker and run server)

### 3)In another terminal: docker-compose exec web python manage.py migrate --noinput

### 4)go to your browser and write in the search bar: 127.0.0.1:8000

## 1.In terminal:

### docker ps -a

### You mast get a name hotel_web_1 sh

### Next: docker exec -it magazin_eldar_web_1 sh

### AND WRITE THIS FOR CREATING SUPERUSER(ADMIN):

### python manage.py createsuperuser

### Anything urls you have in dir "magazine", file "urls.py"

## Tests: Dir "account_app", File "tests.py"

### 1)go to your browser and write in the search bar: 127.0.0.1:8000

### Admin panel: (127.0.0.1:8000/admin/)

