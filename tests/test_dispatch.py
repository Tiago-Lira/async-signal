
import pytest
import asyncio
from async_signal.signals import Signal
from async_signal.exceptions import ArgumentError


class Sender:
    pass


@asyncio.coroutine
def coroutine_receiver_double_multiplier(sender, number):
    return 2 * number


def test_signal_dispatch_with_wrong_arguments():
    with pytest.raises(ArgumentError):
        test_signal = Signal()
        test_signal.dispatch(sender=Sender, some_arg=True)


def test_signal_dispatch_with_correct_arguments():
    test_signal = Signal(arguments=['number'])
    test_signal.connect(
        sender=Sender, receiver=coroutine_receiver_double_multiplier)

    task = test_signal.dispatch(sender=Sender, number=2)[0]
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(task)
    assert result == 4
    loop.close()
