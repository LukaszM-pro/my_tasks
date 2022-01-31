from typing import Tuple


class MyDict(object):
    def __init__(self, my_val_types: Tuple[type], seq=None):
        self._vals = list(seq) if seq is not None else []
        self.val_types = my_val_types

    def __getitem__(self, key):
        return [v[1] for v in self._vals if v[0] == key][0]

    def __setitem__(self, key, val):
        if type(key) is not str:
            raise RuntimeError("Key is not of type STRING!")
        if isinstance(val, self.val_types):
            raise RuntimeError(f'Val type {type(val)} is not of one of permitted types: {self.val_types}')
        self._vals = [v for v in self._vals if v[0] != key]
        self._vals.append((key, val))

    def __len__(self):
        return len(self._vals)
