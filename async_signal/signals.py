
import asyncio

from async_signal.exceptions import ArgumentError
from async_signal.utils import get_sender_key


__all__ = ['Signal']


ERRORS = {
    'argument': 'argument "{}" is not allowed',
    'coroutine_required': '"{}" must be an asyncio coroutine function!',
}


class Signal(object):

    def __init__(self, arguments=[]):
        self.arguments = arguments
        self.receivers = {}

    def connect(self, sender, receiver):

        if not asyncio.iscoroutinefunction(receiver):
            raise ArgumentError(ERRORS['coroutine_required'].format(receiver))

        sender_key = get_sender_key(sender)
        receivers = self.receivers.get(sender_key, [])
        receivers.append(receiver)
        self.receivers[sender_key] = receivers

    def dispatch(self, sender, **kwargs):
        for key, value in kwargs.items():
            if key not in self.arguments:
                raise ArgumentError(ERRORS['argument'].format(key))

        sender_key = get_sender_key(sender)
        receivers = self.receivers.get(sender_key, [])
        tasks = [receiver(sender=sender, **kwargs) for receiver in receivers]
        return [asyncio.async(task) for task in tasks]

    def has_receivers(self, sender):
        sender_key = get_sender_key(sender)
        return bool(self.receivers.get(sender_key, None))
