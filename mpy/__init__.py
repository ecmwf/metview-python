
import keyword

from . import metview


# Add to the module namespace all metview functions except operators like: +, &, etc.
for metview_name in metview.make('dictionary')():
    if metview_name.isidentifier():
        python_name = metview_name
        # NOTE: we append a '_' to metview functions that clash with python reserved keywords
        #   as they cannot be used as identifiers, for example: 'in' -> 'in_'
        if keyword.iskeyword(metview_name):
            python_name += '_'
        globals()[python_name] = metview.make(metview_name)
    else:
        print('metview function %r not bound to python' % metview_name)
