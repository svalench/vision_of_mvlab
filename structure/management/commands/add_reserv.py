from django.core.management.base import BaseCommand, CommandError

from structure.models import Reserv_1, Reserv_2


class Command(BaseCommand):
    """команда для создание в резервных таблицах структуры связей"""
    help = 'add reserve struct'

    def add_arguments(self, parser):
        parser.add_argument('name_str1', type=str, help='write name for structure 1')
        parser.add_argument('name_str2', type=str, help='write name for structure 2')

    def handle(self, *args, **options):
        try:
            struct1 = Reserv_1(name=options['name_str1'])
            struct2 = Reserv_2(name=options['name_str2'], res1=struct1)
            struct1.save()
            struct2.save()
        except:
            raise CommandError('Struct "%s" does not write' % options['name_str1'])
        self.stdout.write(self.style.SUCCESS(
            'Successfully write struct 1 -"%s" and 2 - "%s"' % (options['name_str1'], options['name_str2'])))
