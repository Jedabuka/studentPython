import inspect
import sys


class MyClass:
    def __init__(self, obj):
        self.obj = obj
        self.introspection_info()

    def introspection_info(self):
        intro_dict = {}
        attributes = []
        methods = []
        intro_dict.update({'type': type(self.obj).__name__})
        for attr in dir(self.obj):
            if callable(getattr(self.obj, attr)):
                methods.append(attr)
                intro_dict.update({'methods': methods})
            else:
                attributes.append(attr)
                intro_dict.update({'attributes': attributes})
        intro_dict.update({'module': inspect.getmodule(MyClass)})
        intro_dict.update({'builtin': inspect.isbuiltin(self.obj)})
        intro_dict.update({'id': id(self.obj)})
        intro_dict.update({'size': sys.getsizeof(self.obj)})

        return print(intro_dict)


my_class = MyClass(42)
