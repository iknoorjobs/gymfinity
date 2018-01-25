# GymFinity v1.0

## Setting up on your machine
1.
```
$ sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
$ sudo apt-get update
$ sudo apt install libgdal-dev gdal-bin python-gdal python3-gdal
```

2. Clone this repo

```
$ git clone https://github.com/gurpreetsingh00885/gymfinity.git
```

3. Install requirements

```
$ cd gymfinity
$ pip3 install -r requirements.txt
```

4. Collect staticfiles and run the migrations

```
$ python3 manage.py collectstatic
$ python3 manage.py migrate
```

5. Start the server

```
$ python manage.py runserver
```

6. Open https://127.0.0.1:8000/ in a web browser.

_You will need to add a few gyms in order to test the website since there wouldn't be any in the database yet._
