
import keyword

from . import metview


# Add to the module namespace all metview functions except operators like: +, &, etc.
for func in metview.make('dictionary')():
    if func.isidentifier() and not keyword.iskeyword(func):
        globals()[func] = metview.make(func)
    else:
        print('excluding %r' % func)
