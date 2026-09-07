class OwnedObject:
    def __init__(self, owner):
        self.__owner = owner
    @property
    def _boss(self):
        if isinstance(self._owner, OwnedObject):
            return self._owner._boss
        else:
            return self._owner
    @property
    def _owner(self):
        return self.__owner
