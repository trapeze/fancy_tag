Fancy Tag
=========

Overview
--------

``fancy_tag`` is a template tag decorator designed to replace Django's built in
``simple_tag`` decorator. It's backwards compatible with ``simple_tag`` and adds
new calling options like named arguments.

Features
--------

* Named arguments - arguments can be explicitly assigned to parameter specific
  parameters in the template tag function

* Variable length arguments - The "``*args``" and "``**kwargs``" notation

* The trailing "``as <varname>``" to assign the output of the template tag to
  a variable in the template's context.

Installation
------------

1. Add the fancy_tag package to your Python path


2. Instead of::

    @register.simple_tag
    def some_tag(arg1, arg2):
        return '%s %s' % (arg1, arg2)


   Use::

    @fancy_tag(register)
    def some_tag(arg1, arg2):
        return '%s %s' % (arg1, arg2)

Testing
-------

With Django in your python path, run ``tests/run_tests.py``

Source
------

TODO: Add link to github

License
-------

fancy_tag is Copyright © 2010 Sam Bull, Trapeze. It is free software, and
may be redistributed under the terms specified in the LICENSE file.

Credits
-------

fancy_tag is maintained by [Sam Bull](sbull@trapeze.com), and is funded by
[Trapeze](http://trapeze.com)
