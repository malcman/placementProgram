"""Helper functions to dynamically load views and models.

Inspired by and largely taken from Bobby Waycott's blog:
https://bobwaycott.com/blog/how-i-use-flask/organizing-flask-models-with-automatic-discovery/
"""
from inspect import isclass
from importlib import import_module
from os import walk
from os.path import abspath, basename, dirname, join
from flask.views import View
from flask_sqlalchemy import Model

# main project path & module name
PROJ_DIR = abspath(join(dirname(abspath(__file__)), '../placemaster'))
APP_MODULE = basename(PROJ_DIR)


def get_modules(module):
    """Return all .py modules in given `module` directory that are not `__init__`.

    Usage:
      get_modules('models')

    Yields dot-notated module paths for discovery/import.
    Example:
      /proj/app/models/foo.py > app.models.foo
    """
    file_dir = abspath(join(PROJ_DIR, module))
    for root, _, files in walk(file_dir):
        mod_path = '{}{}'.format(
            APP_MODULE,
            root.split(PROJ_DIR)[1]).replace('/', '.')
        for filename in files:
            if (filename.endswith('.py') and not
                    filename.startswith('__init__')):
                yield '.'.join([mod_path, filename[0:-3]])


def dynamic_loader(module, compare):
    """Iterate over all .py files in `module` directory, finding all classes that
    match `compare` function AND have __all__ declared.
    Other classes/objects in the module directory will be ignored.

    Returns unique list of matches found.
    """
    items = []
    for mod in get_modules(module):
        module = import_module(mod)
        if hasattr(module, '__all__'):
            objs = [getattr(module, obj) for obj in module.__all__]
            items += [o for o in objs if compare(o) and o not in items]
    return items


def get_views(subdir=None):
    """Dynamic view finder.
    If subdir is not specified, searches directly in app package views module.
    If subdir is specified, only search in the views directory of that module.
    """
    module_dir = 'views'
    if subdir:
        module_dir = join(subdir, module_dir)
    return dynamic_loader(module_dir, is_view)


def is_view(item):
    """Determine if `item` is a `View` subclass.

    (we don't want to register `View` itself).
    """
    return item is not View and isclass(item) and issubclass(item, View)


def get_models():
    """Dynamic model finder."""
    return dynamic_loader('model', is_model)


def is_model(item):
    """Determines if `item` is a `Model` subclass."""
    return isclass(item) and issubclass(item, Model)


def load_models():
    """Load application models for management script & app availability."""
    for model in get_models():
        setattr(modules[__name__], model.__name__, model)
