#
# Any machine specific settings when using development settings.
#

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "opentaak",
        "USER": "opentaak",
        "PASSWORD": "opentaak",
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost
        # through TCP.
        "HOST": "",
        "PORT": "",  # Set to empty string for default.
    }
}
