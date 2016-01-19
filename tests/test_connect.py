
import pytest
import asyncio
from async_signal.signals import Signal
from async_signal.exceptions import ArgumentError
from async_signal.utils import get_sender_key


class Sender:
    pass


def not_coroutine_receiver():
    pass


@asyncio.coroutine
def coroutine_receiver():
    pass


def test_signal_connect_when_isnt_coroutine():
    with pytest.raises(ArgumentError):
        test_signal = Signal()
        test_signal.connect(sender=Sender, receiver=not_coroutine_receiver)


def test_signal_connect_when_is_coroutine():
    test_signal = Signal()
    test_signal.connect(sender=Sender, receiver=coroutine_receiver)
    key = get_sender_key(Sender)
    assert coroutine_receiver in test_signal.receivers[key]
