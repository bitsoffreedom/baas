from django.core.management.base import BaseCommand, CommandError
from boem.models import TempMail
import json
import os.path

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--file',dest='mailfile',action='store'),
    )
    def handle(self, *args, **options):
        if os.path.exists(options['file']):
            mail = json.loads(options['file'])
            newMail = TempMail.objects.get_or_Create(mailfrom=mail['from'],
                        mailsubj=mail['subj'], mailrcvd=mail['rcvd'],
                        mailhdrs=mail['hdrs'])
        else:
            raise CommandError('File "%s" does not exist' % options['file'])