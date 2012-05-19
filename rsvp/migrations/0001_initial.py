# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Level'
        db.create_table('rsvp_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('redirect', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('rsvp', ['Level'])

        # Adding model 'Question'
        db.create_table('rsvp_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prompt', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Level'], blank=True)),
        ))
        db.send_create_signal('rsvp', ['Question'])

        # Adding model 'Answer'
        db.create_table('rsvp_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Question'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('rsvp', ['Answer'])

        # Adding model 'Guest'
        db.create_table('rsvp_guest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('people', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Level'])),
            ('reply', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('rsvp', ['Guest'])

        # Adding model 'Response'
        db.create_table('rsvp_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Guest'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Question'])),
            ('response', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvp.Answer'])),
        ))
        db.send_create_signal('rsvp', ['Response'])


    def backwards(self, orm):
        
        # Deleting model 'Level'
        db.delete_table('rsvp_level')

        # Deleting model 'Question'
        db.delete_table('rsvp_question')

        # Deleting model 'Answer'
        db.delete_table('rsvp_answer')

        # Deleting model 'Guest'
        db.delete_table('rsvp_guest')

        # Deleting model 'Response'
        db.delete_table('rsvp_response')


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
            'reply': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
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
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rsvp.Level']", 'blank': 'True'}),
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
