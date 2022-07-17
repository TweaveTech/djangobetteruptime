=====
Django Better Uptime
=====

Polls is a Django app which gives you access to a decorator. 
Upon succesful completion of your function, the decorator will inform your betteruptime heartbeat.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'betteruptime',
    ]

2. Include the polls URLconf in your project urls.py like this::

    @send_heartbeat('someheartbeatid')
