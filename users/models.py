from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Prefer not to say', 'Prefer not to say')
)

EDUCATION_CHOICES = (
    ('No formal education', 'No formal education'),
    ('Primary education', 'Primary education'),
    ('Secondary education', 'Secondary education'),
    ('Vocational qualification', 'Vocational qualitifaction'),
    ("Bachelor's Degree", "Bachelor's Degree"),
    ("Master's Degree", "Master's Degreee"),
    ("Doctorate Degree", "Doctorate Degree"),
    ("Others", "Others"),
)

HEARING_LOSS_INTENSITY = (
    ('Normal hearing (0-20 dB)', 'Normal hearing (0-20 db)'),
    ('Mild hearing loss (20-40 dB)', 'Mild hearing loss (20-40 dB)'),
    ('Moderate hearing loss (40-60 dB)', 'Moderate hearing loss (40-60 dB)'),
    ('Severe hearing loss (60-80 dB)', 'Severe hearing loss (60-80 dB)'),
    ('Severe-to-Profound hearing loss (80-90 dB)', 'Severe-to-Profound hearing loss (80-90 dB)'),
    ('Profound hearing loss (>90 dB)', 'Profound hearing loss (>90 dB)'),
)

HEARING_IMPAIRMENT_TYPE = (
    ('Sensorineural', 'Sensorineural'),
    ('Conductive', 'Conductive'),
    ('Mixed', 'Mixed'),
    ('Others', 'Others'),
)

HEARING_AID_TYPE = (
    ('Hearing aid', 'Hearing aid'),
    ('Cochlearn implant', 'Cochlear implant'),
    ('No hearing aid', 'No hearing aid'),
)

PREFFERED_MODE_OF_COMMUNICATION = (
    ('Lipreading and speech', 'Lipreading and speech'),
    ('Sign language', 'Sign language'),
    ('Gestures', 'Gestures'),
    ('Others', 'Others'),
)

LIPREADING_EXPERTISE = (
    ('Beginner', 'Begineer'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
    ('Expert', 'Expert'),
)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField()
    gender = models.CharField(default=None, blank=True, null=True, max_length=20, choices=GENDER)
    education = models.CharField(default=None, blank=True, null=True, max_length=30, choices=EDUCATION_CHOICES, help_text="Your highest level of education")
    parents_education = models.CharField(default=None, blank=True, null=True, max_length=30, choices=EDUCATION_CHOICES, help_text="Your parents highest level of education")
    hearing_loss_age = models.IntegerField(default=None, null=True, help_text="Age at which hearing loss occurred")
    hearing_loss_intensity = models.CharField(default=None, null=True, max_length=50, choices=HEARING_LOSS_INTENSITY)
    hearing_impairment_type = models.CharField(default=None, null=True, max_length=20, choices=HEARING_IMPAIRMENT_TYPE)
    hearing_aid_type = models.CharField(default=None, null=True, max_length=20, choices=HEARING_AID_TYPE)
    preferred_mode_of_communication = models.CharField(default=None, null=True, max_length=30, choices=PREFFERED_MODE_OF_COMMUNICATION)
    lipreading_expertise = models.CharField(default=None, null=True, max_length=20, choices=LIPREADING_EXPERTISE)

    def __str__(self):
        return self.user.username