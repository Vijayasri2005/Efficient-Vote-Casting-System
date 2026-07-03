"""
WSGI config for Voting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Voting.settings')

application = get_wsgi_application()

# Add this line below to let Vercel bind to the application instance smoothly
app = application