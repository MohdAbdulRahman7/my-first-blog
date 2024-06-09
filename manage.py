#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
a script that helps with management of the site.
With this we will be able to start a web server on our computer without installing anything else.
"""
"""
1. To create a database for our blog, let's run the following in the console: python manage.py migrate
2. start the web server by running python manage.py runserver
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marahmanBlog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
