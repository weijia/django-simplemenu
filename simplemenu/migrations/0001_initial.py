# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MenuItem'
        db.create_table('simplemenu_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('rank', self.gf('django.db.models.fields.SmallIntegerField')(unique=True, db_index=True)),
            ('urlobj_content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('urlobj_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('urlstr', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('simplemenu', ['MenuItem'])

        # Adding model 'URLItem'
        db.create_table('simplemenu_urlitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('simplemenu', ['URLItem'])


    def backwards(self, orm):
        
        # Deleting model 'MenuItem'
        db.delete_table('simplemenu_menuitem')

        # Deleting model 'URLItem'
        db.delete_table('simplemenu_urlitem')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'simplemenu.menuitem': {
            'Meta': {'ordering': "['rank']", 'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'rank': ('django.db.models.fields.SmallIntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            'urlobj_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'urlobj_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'urlstr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'simplemenu.urlitem': {
            'Meta': {'object_name': 'URLItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['simplemenu']
