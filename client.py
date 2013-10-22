# -*- coding: utf-8 -*-

"""
    eve-demo-client
    ~~~~~~~~~~~~~~~

    Simple and quickly hacked togheter, this script is used to reset the
    eve-demo API to its initial state. It will use standard API calls to:

        1) delete all items in the 'people' and 'works' collections
        2) post multiple items in both collection

    I guess it can also serve as a basic example of how to programmatically
    manage a remot e API using the phenomenal Requests library by Kenneth Reitz
    (a very basic 'get' function is included even if not used).

    :copyright: (c) 2012 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
import requests
import json
import random

ENTRY_POINT = 'http://eve-demo.herokuapp.com'
#ENTRY_POINT = 'http://localhost:5000'


def post_people():
    people = [
        {
            'firstname': 'John',
            'lastname': 'Doe',
            'role': ['author'],
            'location': {'address': '422 South Gay Street', 'city': 'Auburn'},
            'born': 'Thu, 27 Aug 1970 14:37:13 GMT'
        },
        {
            'firstname': 'Serena',
            'lastname': 'Love',
            'role': ['author'],
            'location': {'address': '363 Brannan St', 'city': 'San Francisco'},
            'born': 'Wed, 25 Feb 1987 17:00:00 GMT'
        },
        {
            'firstname': 'Mark',
            'lastname': 'Green',
            'role': ['copy', 'author'],
            'location': {'address': '4925 Lacross Road', 'city': 'New York'},
            'born': 'Sat, 23 Feb 1985 12:00:00 GMT'
        },
        {
            'firstname': 'Julia',
            'lastname': 'Red',
            'role': ['copy'],
            'location': {'address': '98 Yatch Road', 'city': 'San Francisco'},
            'born': 'Sun, 20 Jul 1980 11:00:00 GMT'
        },
        {
            'firstname': 'Anne',
            'lastname': 'White',
            'role': ['contributor', 'copy'],
            'location': {'address': '32 Joseph Street', 'city': 'Ashfield'},
            'born': 'Fri, 25 Sep 1970 10:00:00 GMT'
        },
    ]

    payload = {}
    for person in people:
        payload[person['lastname']] = json.dumps(person)

    r = perform_post('people', payload)
    print "'people' posted", r.status_code

    valids = []
    if r.status_code == 200:
        response = r.json()
        for person in payload:
            result = response[person]
            if result['status'] == "OK":
                valids.append(result['_id'])

    return valids


def post_works(ids):
    works = []
    for i in range(28):
        works.append(
            {
                'title': 'Book Title #%d' % i,
                'description': 'Description #%d' % i,
                'owner': random.choice(ids),
            }
        )

    payload = {}
    for i in range(len(works)):
        payload['work' + str(i + 1)] = json.dumps(works[i])
    r = perform_post('works', payload)
    print "'works' posted", r.status_code


def perform_post(resource, data):
    return requests.post(endpoint(resource), data)


def delete():
    r = perform_delete('people')
    print "'people' deleted", r.status_code
    r = perform_delete('works')
    print "'works' deleted", r.status_code


def perform_delete(resource):
    return requests.delete(endpoint(resource))


def endpoint(resource):
    return '%s/%s/' % (ENTRY_POINT, resource)


def get():
    r = requests.get('http://eve-demo.herokuapp.com')
    print r.json

if __name__ == '__main__':
    delete()
    ids = post_people()
    post_works(ids)
    #get()
