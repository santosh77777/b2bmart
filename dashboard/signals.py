from django.db.models.signals import post_save
from django.contrib.auth.models import User



from .models import UserProfile

def seller_profile(sender, instance, created, **kwargs):
	if created:
		BusinessProfile.objects.create(
			user=instance,
			)
		print('Profile created!')

post_save.connect(seller_profile, sender=User)