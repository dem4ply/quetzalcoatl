import os


os.environ[ 'QUETZALCOATL__RABBITMQ__KEY__URL' ]

#mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ[ 'QUETZALCOATL__DATABASE__NAME' ],
        'USER': os.environ[ 'QUETZALCOATL__DATABASE__USER' ],
        'PASSWORD': os.environ[ 'QUETZALCOATL__DATABASE__PASSWORD' ],
        'HOST': os.environ[ 'QUETZALCOATL__DATABASE__HOST' ],
        'PORT': os.environ[ 'QUETZALCOATL__DATABASE__PORT' ],
    },
}
