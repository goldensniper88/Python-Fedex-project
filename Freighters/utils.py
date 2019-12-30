

class FreighterObject:
    pass


class FreighterModules(list):
    """
    Extended list element.
    Force to only take objects of type FreighterObject
    """
    modules = list()


    def __init__(self, freigher_obj_list):
        if self.is_freighter(freigher_obj_list):
            self.modules = freigher_obj_list

    def __add__(self, other):
        if  (self.is_freighter(isinstance())):
            self.modules = self.modules + [other]
        return self.modules

    def __iadd__(self, other):
        if  (self.is_freighter(other)):
            self.modules = self.modules + [other]
        return self.modules

    def append(self, object):
        if self.is_freighter(object):
            self.modules[len(self.modules):] = [object]
        return self.modules

    @staticmethod
    def is_freighter(obj):
        if (isinstance(obj, list)):
            return min([ isinstance(i, FreighterObject) for i in obj])
        return False
