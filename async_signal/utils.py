

__all__ = ['get_sender_key']


def get_sender_key(sender):
    return sender.__module__ + '.' + sender.__name__
