from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import TextInput, ModelForm


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)

    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)

    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=5)
    instagram = models.CharField(blank=True, max_length=5)
    twitter = models.CharField(blank=True, max_length=5)

    aboutus = RichTextUploadingField(blank=True, null=True)
    contact = RichTextUploadingField(blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    message = models.TextField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=30, blank=True)
    note = models.CharField(max_length=100, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage()
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'place_holder': 'Name & Surname'}),
            'email': TextInput(attrs={'class': 'input', 'place_holder': 'Email Address'}),
            'subject': TextInput(attrs={'class': 'input', 'place_holder': 'Subject'}),
            'message': TextInput(attrs={'class': 'input', 'place_holder': 'Your Message', 'rows': '5'})
        }
