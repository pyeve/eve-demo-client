Eve Demo Client
===============

Simple and quickly hacked togheter, this script is used to reset the `Eve-Demo
<https://github.com/nicolaiarocci/eve-demo>`_ REST API to its inital state.

It will use standard API calls to:

    1) delete all items in the 'people' and 'works' collections
    2) post default items in both collections

I guess it can also serve as a basic example of how to programmatically manage
a remote API using the phenomenal Requests library by Kenneth Reitz.
