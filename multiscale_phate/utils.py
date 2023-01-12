import pickle
import sys


def _pickle_protocol():
    """Get the highest working pickle protocol
    
    Pickle protocol 5 is supported on Python 3.7 but doesn't work with loky
    """
    if tuple(sys.version.split(".")[:2]) < ('3', '8'):
        return min(pickle.HIGHEST_PROTOCOL, 4)
    return pickle.HIGHEST_PROTOCOL


def hash_object(X):
    """Description of returned object.
    """
    return hash(pickle.dumps(X, protocol=_pickle_protocol()))
