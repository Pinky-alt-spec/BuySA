from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import TextInput, ModelForm, Textarea


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keyword = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    
    phone = models.CharField(blank=True, max_length=17)
    whatsappcontact = models.CharField(blank=True, max_length=17)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    status = models.CharField(max_length=10, choices=STATUS)
    
    name1 = models.CharField(blank=True, max_length=50)
    name2 = models.CharField(blank=True, max_length=50)
    name3 = models.CharField(blank=True, max_length=50)
    position1 = models.CharField(blank=True, max_length=50)
    position2 = models.CharField(blank=True, max_length=50)
    position3 = models.CharField(blank=True, max_length=50)
    
    icon = models.ImageField(blank=True, upload_to='images/')
    
    aboutus = RichTextUploadingField(blank=True, null=True)
    contact = RichTextUploadingField(blank=True, null=True)
    workinghours = RichTextUploadingField(blank=True, max_length=100)
    contactcomment = RichTextUploadingField(blank=True, max_length=200)
    
    slide1 = RichTextUploadingField(blank=True, max_length=200)
    slide2 = RichTextUploadingField(blank=True, max_length=200)
    slide3 = RichTextUploadingField(blank=True, max_length=200)
    slidecomment1 =RichTextUploadingField(blank=True, max_length=200)
    slidecomment2 = RichTextUploadingField(blank=True, max_length=200)
    slidecomment3 =  RichTextUploadingField(blank=True, max_length=200)
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
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
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }
