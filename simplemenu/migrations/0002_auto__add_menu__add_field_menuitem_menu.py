# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Menu'
        db.create_table('simplemenu_menu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('simplemenu', ['Menu'])

        # Adding field 'MenuItem.menu'
        db.add_column('simplemenu_menuitem', 'menu', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['simplemenu.Menu']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Menu'
        db.delete_table('simplemenu_menu')

        # Deleting field 'MenuItem.menu'
        db.delete_column('simplemenu_menuitem', 'menu_id')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'simplemenu.menu': {
            'Meta': {'object_name': 'Menu'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'simplemenu.menuitem': {
            'Meta': {'ordering': "['rank']", 'object_name': 'MenuItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplemenu.Menu']"}),
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
