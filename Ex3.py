def introspection_info(obj):
    obj_type = type(obj).__name__
    attribute = dir(obj)
    metods = [metod for metod in attribute if callable(getattr(obj, metod))]
    modul = obj.__class__.__module__
    information = {'type': obj_type, 'attribyte': attribute, 'metod': metods, 'modul': modul}
    return information

number_info = introspection_info(42)
print(number_info)
print('________________________________________')

string_info = introspection_info('Hi')
print(string_info)
print('________________________________________')

list_info = introspection_info([1, 2, 3, 56.7, 'cat'])
print(list_info)
