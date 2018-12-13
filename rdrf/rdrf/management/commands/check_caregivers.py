import sys
from datetime import datetime, timedelta
from django.core.management import BaseCommand
from rdrf.models.definition.models import Registry
from rdrf.services.io.notifications.reminders import ReminderProcessor
from rdrf.services.io.notifications.email_notification import process_notification

from registry.groups.models import CustomUser

def send_reminder(user, registry_model, process_func=None):
    if process_func:
        rp = ReminderProcessor(user, registry_model, process_func)
    else:
        rp = ReminderProcessor(user, registry_model)
    sent = rp.process()
    return sent


class Command(BaseCommand):
    help = "Sends out caregiver 12 month check if required"

    def add_arguments(self, parser):
        parser.add_argument('-r', "--registry_code",
                            action='store',
                            dest='registry_code',
                            help='Code of registry to check')

        parser.add_argument("-a", "--action",
                            action="store",
                            dest="action",
                            choices=['print', 'send-reminders'],
                            default='print',
                            help="Action to perform")

        parser.add_argument("-t", "--test-mode",
                            action="store_true",
                            dest="test_mode",
                            default=False,
                            help="Action to perform")


    def handle(self, *args, **options):
        registry_code = options.get("registry_code")
        if registry_code is None:
            self._error("Registry code required")
            sys.exit(1)

        try:
            registry_model = Registry.objects.get(code=registry_code)
        except Registry.DoesNotExist:
            self._error("Registry does not exist")
            sys.exit(1)
