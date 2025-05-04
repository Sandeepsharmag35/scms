#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
import django
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import execute_from_command_line, call_command

MAX_RETRIES = 10
RETRY_INTERVAL = 5
WAIT_AFTER_FAIL = 20 * 60  # 20 minutes


def wait_for_db():
    retry_phase = 1
    while True:
        for attempt in range(MAX_RETRIES):
            try:
                conn = connections["default"]
                conn.cursor()
                print("✅ Database connection established.")
                return
            except OperationalError:
                print(
                    f"❌ Database unavailable (try {attempt + 1}/{MAX_RETRIES})... waiting {RETRY_INTERVAL}s"
                )
                time.sleep(RETRY_INTERVAL)
        print(
            f"⚠️ Retried {MAX_RETRIES} times. Waiting {WAIT_AFTER_FAIL // 60} minutes before next attempt..."
        )
        time.sleep(WAIT_AFTER_FAIL)


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mart.settings")

    wait_for_db()

    try:
        django.setup()
        print("🛠 Running makemigrations...")
        try:
            call_command("makemigrations", interactive=False)
        except Exception as e:
            print(f"❌ Makemigrations error: {e}")

        print("🛠 Running migrate...")
        try:
            call_command("migrate", interactive=False)
        except Exception as e:
            print(f"❌ Migration error: {e}")

    except Exception as setup_error:
        print(f"❌ Django setup failed: {setup_error}")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
