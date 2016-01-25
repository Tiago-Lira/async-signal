
# async-signal
[![PyPI version](https://badge.fury.io/py/async-signal.svg)](https://badge.fury.io/py/async-signal)
[![Build Status](https://travis-ci.org/Tiago-Lira/async-signal.svg?branch=master)](https://travis-ci.org/Tiago-Lira/async-signal)
[![Coverage Status](https://coveralls.io/repos/github/Tiago-Lira/async-signal/badge.svg?branch=master)](https://coveralls.io/github/Tiago-Lira/async-signal?branch=master)

This package provide a class to connect signals (using asyncio) to your functions.  
Works on Python3.4+

### Install

Install via pip:

```bash
$ pip install async-signal

```


### Getting started

This package provides a class to create signals with asyncio. The main concepts to understand how to use are:
* Sender   - the class that will dispatch the signal
* Receiver - the asyncio coroutine that will receive this signal

For this work, you need to connect a "Receiver" to a "Sender". see the example below:

#### Creating a "was_multiplied" signal

```python

from async_signal.signals import Signal

# The receiver function will receive these arguments
was_multiplied = Signal(arguments=['result'])

```


#### Creating the Sender to Dispatch the Signal

The sender must be a function, class or some object that have the attributes ```__module__``` and ```__name__```

```python


def multiply_by_2(self, number):
    result = number * 2
    # This will emit to all receivers this result
    was_multiplied.dispatch(sender=self, result=result)

```


#### Connecting a receiver to this signal

The `receiver` must use the `@asyncio.coroutine` decorator

```python

import asyncio


@asyncio.coroutine
def listen_multiply(sender, result):
    # Every time that the function multiply_by_2 is called
    # This signal will receive the result
    # if multiply_by_2(10) is called, this function will print:
    # >> 20
    print(result)


on_success.connect(sender=multiply_by_2, receiver=listen_multiply)

```
