from django.db import models

class MaxPriorityQueue(models.Model):
    name = models.CharField(max_length = 200)

class MinPriorityQueue(models.Model):
    name = models.CharField(max_length = 200)

class MixinPriorityQueue(models.Model):
    name = models.CharField(max_length = 200)