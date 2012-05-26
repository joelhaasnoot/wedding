# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Question.level'
        db.alter_column('rsvp_question', 'level_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Level'], null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Question.level'
        raise RuntimeError("Cannot reverse this migration. 'Question.level' and its values cannot be restored.")


    models = {
        'rsvp.answer': {
            'Meta': {'object_name': 'Answer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Question']"})
        },
        'rsvp.guest': {
            'Meta': {'object_name': 'Guest'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Level']"}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'people': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'reply': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'})
        },
        'rsvp.level': {
            'Meta': {'object_name': 'Level'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'redirect': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'rsvp.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Level']", 'null': 'True', 'blank': 'True'}),
            'prompt': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'rsvp.response': {
            'Meta': {'object_name': 'Response'},
            'guest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Guest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Question']"}),
            'response': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Answer']"})
        }
    }

    complete_apps = ['rsvp']
