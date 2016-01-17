
# async-signal

This package provide a classs to connect signals (using asyncio) to your functions.  
Works on Python3.4+


### Creating a signal

```python
# -*- coding: utf-8 -*-

from async_signal.signals import Signal

# The receiver function will receive these arguments
on_success = Signal(arguments=['message'])

```


### Dispatching Signals

```python


class Example(object):

    def do_stuff(*args, **kwargs):
        # ... do stuff ...
        # all receivers connected to this signal will receive this
        on_success.dispatch(sender=self.__class__, message='Hey, it works')

```


### Connecting a signal

```python

import asyncio


@asyncio.coroutine
def signal_listener(sender, **kwargs):
    print kwargs['message']  # will print "Hey, it works"


on_success.connect(sender=Example, receiver=signal_listener)

```

