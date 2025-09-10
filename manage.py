"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the default Django settings module for the 'flint_project'
    # This environment variable points to the main project's settings file.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flint_project.settings')
    try:
        # Import Django's command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # This block catches an ImportError, which typically means Django
        # is not installed or not in the Python path.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Pass the command-line arguments to Django's management utility.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # This block ensures that the main() function is called only
    # when the script is executed directly (not when it's imported).
    main()