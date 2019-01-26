from utils.logger import Logger
from django.contrib import admin
from .models import MaxPriorityQueue, MinPriorityQueue, MixinPriorityQueue

logger = Logger(prefix = 'Dashboard', level = 'Info')
logger.info('admin', 'init')

admin.site.register(MaxPriorityQueue)
admin.site.register(MinPriorityQueue)
admin.site.register(MixinPriorityQueue)


