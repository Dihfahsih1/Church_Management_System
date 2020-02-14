import psycopg2
conn = psycopg2.connect(
	'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'MugoYA23?',
        'HOST': 'localhost',
        'PORT': '5432',
        ) 
print('connected successfully')