# Django Better Uptime

Polls is a Django app which gives you access to a decorator. 
Upon succesful completion of your function, the decorator will inform your betteruptime heartbeat.

## Quick start

1. Add the app to your requirements.txt or install via pip:

    ```
    git+ssh://git@bitbucket.org/slaapadviesbvba/djangobetteruptime.git
    ```

2. Add "betteruptime" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...
        'betteruptime',
    ]
    ```

3. Include the polls URLconf in your project urls.py like this:

    ```
    # Add your decorator to any function by supplying the heartbeat id
    from betteruptime.decorators import send_heartbeat
   
    @send_heartbeat('someheartbeatid')
    def my_function():
        pass
        
    # or if you're using this inside of a class and you have a 
    # self.heartbeat_id available:
    
    from betteruptime.decorators import send_heartbeat
    
    class MyClass:
        heartbeat_id = 'some_id'

        @send_heartbeat()
        def run(self):
            pass
    
    # Or by including the mixin and calling it manually.
    # Dont forget to either supply the heartbeat_id to the
    # function or setting it in your class as a static or dynamic id.
    
    from betteruptime.mixins import SendHeartBeatMixin
    
    class MyClass(SendHeartBeatMixin):
        heartbeat_id = '123abcd'
        
        def __init__(self):
            self.heartbeat_id = 'some_other_id'

        def run(self):
            self.send_heartbeat('123abc')
            # or, if you declared it on your class
            self.send_heartbeat()  	
    ```

