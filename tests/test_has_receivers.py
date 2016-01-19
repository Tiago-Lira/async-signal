
import asyncio
from async_signal.signals import Signal


class Sender:
    pass


@asyncio.coroutine
def coroutine_receiver():
    pass


def test_signal_has_receivers_when_is_false():
    test_signal = Signal()
    assert test_signal.has_receivers(sender=Sender) is False


def test_signal_has_receivers_when_is_true():
    test_signal = Signal()
    test_signal.connect(sender=Sender, receiver=coroutine_receiver)
    assert test_signal.has_receivers(sender=Sender) is True
