from django.core.mail import send_mail
from b2bmart.settings.base import EMAIL_HOST_USER

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "b2bmart.settings.base")
print("Dilippppppppppppppppp", EMAIL_HOST_USER)
send_mail(
    'Subject here','Here is the message.',EMAIL_HOST_USER, ['dilipsapkota.d@gmail.com'],fail_silently=False)

print("Dilippppppppppppppppp", EMAIL_HOST_USER)