serve:
		python3 manage.py runserver

migrations:
		python3 manage.py makemigrations

migrate:
		python3 manage.py migrate

create:
	python3 manage.py createsuperuser --username ${name}

app:
	 python3 manage.py startapp ${appname}