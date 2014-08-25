#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lnkdin.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "view.settings")
>>>>>>> dd3c11a33a155d7bfb3e8dae5e6a89be48fd9b9b

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
