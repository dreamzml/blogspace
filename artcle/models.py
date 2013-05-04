# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
import datetime
from django.db import models
from django.utils.encoding import force_unicode
from tinymce.models import HTMLField

class DrArtAttLog(models.Model):
    art_id = models.IntegerField()
    att_id = models.IntegerField()
    class Meta:
        db_table = 'dr_art_att_log'
    def __str__(self):
        return self.title
    class Admin:
        pass

class DrArtcle(models.Model):
    art_id = models.IntegerField(primary_key=True)
    art_title = models.CharField(max_length=50L, blank=True)
    art_author = models.CharField(max_length=10L, blank=True)
    art_seotitle = models.CharField(max_length=50L, blank=True)
    art_seokey = models.CharField(max_length=50L, blank=True)
    art_seodescribe = models.CharField(max_length=200L, blank=True)
    art_summary = models.CharField(max_length=200L, blank=True)
    art_content = HTMLField(default="ffffffffffff")
 #   art_content = models.TextField(blank=True)
    inputtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'dr_artcle'
    def __str__(self):
        return self.art_title
    class Admin:
        pass

class DrAttachmant(models.Model):
    att_id = models.IntegerField(primary_key=True)
    att_title = models.CharField(max_length=100L, blank=True)
    att_url = models.CharField(max_length=100L, blank=True)
    att_file_type = models.CharField(max_length=50L, blank=True)
    att_file_size = models.IntegerField(null=True, blank=True)
    inputtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'dr_attachmant'
    def __str__(self):
        return self.att_title
    class Admin:
        pass

class DrCatArtLog(models.Model):
    cat_id = models.IntegerField()
    art_id = models.IntegerField()
    class Meta:
        db_table = 'dr_cat_art_log'
    def __str__(self):
        return self.cat_id
    class Admin:
        pass

class DrCategory(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_title = models.CharField(max_length=50L, blank=True)
    cat_describe = models.CharField(max_length=200L, blank=True)
    cat_seotitle = models.CharField(max_length=50L, blank=True)
    cat_seokey = models.CharField(max_length=50L, blank=True)
    cat_seodescribe = models.CharField(max_length=200L, blank=True)
    inputtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'dr_category'
    def __str__(self):
        return self.cat_title
    class Admin:
        pass

class DrCommend(models.Model):
    cmm_id = models.IntegerField(primary_key=True)
    art_id = models.IntegerField()
    cmm_type = models.IntegerField()
    cmm_parentid = models.IntegerField(null=True, blank=True)
    cmm_content = models.TextField(blank=True)
    inputtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'dr_commend'
    def __str__(self):
        return self.art_id
    class Admin:
        pass

