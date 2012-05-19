from django.db import models

# Configuration
class Level(models.Model):
    name = models.CharField(max_length=20)
    redirect = models.URLField()
    
    def __unicode__(self):
        return self.name
    
class Question(models.Model):
    prompt = models.CharField(max_length=150)
    level =  models.ForeignKey(Level, blank=True) # Blank = ask all
    
    def __unicode__(self):
        return self.prompt
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    label = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.label
    
# Actual guests
class Guest(models.Model):
    RSVP_CHOICES = ((10, 'Kies een...'),
                    (0, 'Helaas niet'),
                    (1, "Wij zijn er bij!"),
                    (3, "Misschien, ik laat het voor 5 aug weten"))
    
    first_name = models.CharField(max_length=25, blank=True) # Optional 
    last_name = models.CharField(max_length=75) #Identifying
    postcode = models.CharField(max_length=7)
    people = models.PositiveIntegerField(default=1) # Party of atleast 1
    
    level = models.ForeignKey(Level)
    reply = models.PositiveSmallIntegerField(choices=RSVP_CHOICES, default=10)
        
    message = models.TextField(blank=True) 
    
    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.level)
    
class Response(models.Model):
    guest = models.ForeignKey(Guest)
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Answer)