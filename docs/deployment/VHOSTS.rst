Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess opentaak-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/opentaak/log/apache2/error.log"
        CustomLog "/srv/sites/opentaak/log/apache2/access.log" common

        WSGIProcessGroup opentaak-<target>

        Alias /media "/srv/sites/opentaak/media/"
        Alias /static "/srv/sites/opentaak/static/"

        WSGIScriptAlias / "/srv/sites/opentaak/src/opentaak/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-opentaak-<target>]
    user = <user>
    command = /srv/sites/opentaak/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/opentaak/src/opentaak/wsgi/wsgi_<target>.py
    home = /srv/sites/opentaak/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/opentaak/log/uwsgi_err.log
    stdout_logfile = /srv/sites/opentaak/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_opentaak_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/opentaak/log/nginx-access.log;
      error_log /srv/sites/opentaak/log/nginx-error.log;

      location /500.html {
        root /srv/sites/opentaak/src/opentaak/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/opentaak/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/opentaak/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_opentaak_<target>;
      }
    }
