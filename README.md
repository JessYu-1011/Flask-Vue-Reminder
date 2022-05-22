# Flask-Vue-Reminder
Demo URL: https://schedule.jessyu.xyz
## Initial the project

#### 1.Download the dependencies

1. ```shell
   git clone https://github.com/JessYu-1011/Flask-Vue-Reminder
   ```

2. ```shell
   cd Flask-Vue-Reminder/frontend
   yarn install
   ```

3. ```shell
   cd ../backend
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt
   ```

4. ```shell
   cd ../tasks
   python3 -m venv venv
   source ./venv/bin/activate
   pip install -r requirements.txt 
   ```

#### Config file settings

1. **Backend settings**
   
   (1) *We can add three types of config files in backend/config/* 
   
   - reminder-config-default.json
   
   - reminder-config-docker.json
     
     > Local config(secret): reminder-config.json
     > 
     > The order that will be initialed：
     > 
     > reminder-config.json > reminder-config-default.json > 
     > 
     > reminder-config-docker.json
   
   (2) *We can add three types of config files in tasks/config/*
   
   - tasks-config-default.json
   
   - tasks-config-docker.json
     
     > Local config(secret): tasks-config.json
     > 
     > The order that will be initialed：
     > 
     > tasks-config.json > tasks-config-default.json > 
     > 
     > tasks-config-docker.json

## The framework Flask-Vue-Reminder used

- Backend：```Flask 2```

- Frontend：```Vue 3```

## Some used Flask plugins

- `flask-restx` => Using to create **API**

- `flask-sqlalchemy` => **ORM** 

- `flask-marshmallow` => Turn **Object** to **JSON**
  
  - with `marshmallow-sqlalchemy`

- `mysqlclient` => communicate with **MySQL**

## Some used Vue pugins and framework

- vue-router@4.x => To create router for Vue

- vue-axios@3.x =>  To fetch the **API** from backend

- tailwindcss 2 => CSS framework

## Backend Structure

```markup-templating
├── backend
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apis
│   │   │   ├── __init__.py
│   │   │   ├── account_api.py
│   │   │   └── subjects_api.py
│   │   ├── models.py
│   │   └── schema.py
│   ├── app-local.ini
│   ├── app.ini
│   ├── app.py
│   ├── config
│   │   ├── reminder-config-default.json
│   │   ├── reminder-config-docker.json
│   │   └── reminder-config.json
│   ├── config.py
│   └── requirements.txt
```

``app.py``: Entry point of backend

``config.py``: config class import the config file from  ``config/`` 

``models.py``: **ORM** related (Using **Flask-SQLAlchemy**)

``schema.py``: **Flask-Marshmallow**

``app.ini`` and ``app-local.ini`` for ``uwsgi``.
First one is for **Dev**, second one is for **Production** 

``app/admin.py``: **Flask-Admin** settings

``app/apis``: **API** codes



## Frontend Structure

```markup-templating
├── frontend
│   ├── Dockerfile
│   ├── README.md
│   ├── nginx.conf
│   ├── postcss.config.js
│   ├── src
│   │   ├── App.vue
│   │   ├── api
│   │   │   └── ip.js
│   │   ├── assets
│   │   │   ├── logo.png
│   │   │   └── tailwind.css
│   │   ├── components
│   │   │   └── Navbar.vue
│   │   ├── main.js
│   │   ├── router
│   │   │   └── index.js
│   │   └── views
│   │       ├── About.vue
│   │       ├── Create.vue
│   │       ├── Home.vue
│   │       └── Modify.vue
│   ├── tailwind.config.js
│   └── yarn.lock
```

``src/api``: **API** origin setting

``src/components``: the components

``src/views``: the pages

- ``About.vue`` => about page

- ``Create.vue`` => create new task page

- ``Home.vue`` => Home page, task page

- ``Modify.vue`` => modify page

# Tasks (Celery)

```markup-templating
 └── tasks
    ├── Dockerfile
    ├── celerybeat-schedule
    ├── config
    │   ├── tasks-config-default.json
    │   ├── tasks-config-docker.json
    │   └── tasks-config.json
    ├── config.py
    ├── mail.py
    ├── models.py
    ├── requirements.txt
    ├── schema.py
    └── tasks.py
```



- <mark>To watch the modification of the database</mark>

- To send the **Mail** to user

- Using **SQLAlchemy** to seize the data

- Mashmallow turn db Object to JSON format

- Celery check whether the data is due every minute
  
  1. After the program started, get the the data from database
     
     order by 
     
     - done
     
     - reminding_date
     
     - reminding_time
  
  2. Turn the Object dat to  JSON format
  
  3. Using async function to check whther the data is due
     
     (1.) If the data is due, wrap the data to mail format then send to user
     
     (2.) Turn ```done``` field of data to True 
     
     (3). Recatch the data from database
