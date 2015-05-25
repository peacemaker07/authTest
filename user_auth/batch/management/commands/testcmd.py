# coding: utf-8

import logging
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<target_id target_id ...>'
    help = u'カスタムAdminコマンドのテストです'

    def handle(self, *args, **options):
        for target_id in args:
            logging.info('target_id: %s' % target_id)
            logging.debug('target_id: %s' % target_id)
            print(target_id)