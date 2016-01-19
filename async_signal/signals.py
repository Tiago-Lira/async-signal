
import asyncio

from async_signal.exceptions import ArgumentError
from async_signal.utils import get_sender_key


__all__ = ['Signal']


ERRORS = {
    'argument': 'argument "{}" is not allowed',
    'coroutine_required': '"{}" must be an asyncio coroutine function!',
}


class Signal(object):

    """ Signal to use with asyncio

    Class Attributes:

    arguments -- Extra-arguments that receiver can receive (default [])
    receivers -- The registered receivers

    """

    def __init__(self, arguments=[]):
        self.arguments = arguments
        self.receivers = {}

    def connect(self, sender, receiver):
        """ Connects a receiver to listen an event of the sender

        Keyword arguments:

        sender   -- the sender that will dispatch the signal
        receiver -- the asyncio coroutine that will receive the signal

        """

        if not asyncio.iscoroutinefunction(receiver):
            raise ArgumentError(ERRORS['coroutine_required'].format(receiver))

        return self.__register_receiver(sender, receiver)

    def dispatch(self, sender, **arguments):
        """ Emit the signal to all receivers registered for this signal

        Keyword arguments:

        sender      -- the sender that will dispatch the signal
        **arguments -- all arguments allowed by "self.arguments"

        """

        for key, value in arguments.items():
            if key not in self.arguments:
                raise ArgumentError(ERRORS['argument'].format(key))

        receivers = self.__get_receivers(sender)
        return self.__execute_tasks(receivers, sender=sender, **arguments)

    def has_receivers(self, sender):
        """ Returns if the sender has receivers registered

        Keyword arguments:

        sender      -- the sender that will dispatch the signal

        """
        return bool(self.__get_receivers(sender))

    def __register_receiver(self, sender, receiver):
        """ Register a receiver
        """
        sender_key = get_sender_key(sender)
        receivers = self.receivers.get(sender_key, [])
        receivers.append(receiver)
        self.receivers[sender_key] = receivers

    def __get_receivers(self, sender):
        """ Returns receivers of the sender
        """
        sender_key = get_sender_key(sender)
        return self.receivers.get(sender_key, [])

    def __execute_tasks(self, receivers, **arguments):
        """ Execute the receivers with aynscio.async
        """
        tasks = [
            receiver(**arguments) for receiver in receivers
        ]
        return [asyncio.async(task) for task in tasks]
