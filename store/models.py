from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	date_modified = models.DateTimeField(User, auto_now=True)
	phone = models.CharField(max_length=20, blank=True)
	address1 = models.CharField(max_length=200, blank=True)
	address2 = models.CharField(max_length=200, blank=True)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=200, blank=True)
	zipcode = models.CharField(max_length=200, blank=True)
	country = models.CharField(max_length=200, blank=True)
	old_cart = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up

	def create_profile(sender, instance, created, **kwargs):
		if created:
			user_profile = Profile(user=instance)
			user_profile.save()


# Automate the profile thing
	post_save.connect(create_profile, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=200, default='any_name')
    description = models.TextField(max_length=100, default='this product made by pilot company for kids wear hope u enjoy in our site ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # active = models.BooleanField(default='true')
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    def __str__(self):
        return self.name

