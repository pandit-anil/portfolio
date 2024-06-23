from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=300)
    profession = models.CharField(max_length=300)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True,null=True)
    git = models.URLField(blank=True,null=True)
    whatsapp = models.URLField(blank=True,null=True)


class Education(models.Model):
    school_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    degree = models.CharField(max_length=200)
    faculty = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.school_name



class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter proficiency level from 1 to 100")

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.job_title
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Photos(models.Model):
    image1 = models.ImageField(upload_to='images/',blank=True, null=True)
    image2 = models.ImageField(upload_to='images/',blank=True, null=True)
    image3 = models.ImageField(upload_to='images/',blank=True, null=True)
    image4 = models.ImageField(upload_to='images/',blank=True, null=True)