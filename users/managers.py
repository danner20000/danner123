from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password=None, company=None):

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            company=company  # Add the company field here
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
