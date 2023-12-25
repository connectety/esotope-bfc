# This is a part of Esotope Brainfuck Compiler.

class gentype(type):
    def __new__(self, name, bases, dict):
        if '__slots__' not in dict:
            dict['__slots__'] = ()
        if 'gen' in dict:
            dict['gen'] = staticmethod(dict['gen'])
        return type.__new__(self, name, bases, dict)

    def __call__(self, *args, **kwargs):
        obj = self.gen(self, *args, **kwargs)
        if obj is NotImplemented:
            obj = type.__call__(self, *args, **kwargs)
        return obj


class genobject(object, metaclass=gentype):
    gen = type.__call__
