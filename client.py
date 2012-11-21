import requests
import json
import random

#ENTRY_POINT = 'http://eve-demo.herokuapp.com'
ENTRY_POINT = 'http://localhost:5000'


def post_people():
    people = [
        {
            'firstname': 'John',
            'lastname': 'Doe',
            'role': ['author'],
            'location': {'address': '422 South Gay Street', 'city': 'Auburn'},
            'born': 'Thu, 27 Aug 1970 14:37:13 UTC'
        },
        {
            'firstname': 'Serena',
            'lastname': 'Love',
            'role': ['author'],
            'location': {'address': '363 Brannan St', 'city': 'San Francisco'},
            'born': 'Wed, 25 Feb 1987 17:00:00 UTC'
        },
        {
            'firstname': 'Mark',
            'lastname': 'Green',
            'role': ['copy', 'author'],
            'location': {'address': '4925 Lacross Road', 'city': 'New York'},
            'born': 'Sat, 23 Feb 1985 12:00:00 UTC'
        },
        {
            'firstname': 'Julia',
            'lastname': 'Red',
            'role': ['copy'],
            'location': {'address': '98 Yatch Road', 'city': 'San Francisco'},
            'born': 'Sun, 20 Jul 1980 11:00:00 UTC'
        },
        {
            'firstname': 'Anne',
            'lastname': 'White',
            'role': ['contributor', 'copy'],
            'location': {'address': '32 Joseph Street', 'city': 'Ashfield'},
            'born': 'Fri, 25 Sep 1970 10:00:00 UTC'
        },
    ]

    payload = {}
    for person in people:
        payload[person['lastname']] = json.dumps(person)

    r = perform_post('people', payload)

    valids = []
    if r.status_code == 200:
        response = r.json['response']
        for person in payload:
            result = response[person]
            if result['status'] == "OK":
                valids.append(result['_id'])

    return valids


def post_works(ids):
    titles = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
    works = []
    for i in range(5):
        works.append(
            {
                'title': '%s Book Title' % titles[i],
                'description': '%s description' % titles[i],
                'owner': random.choice(ids),
                #'contributors':  random.sample(ids, random.randint(1, 5))
            }
        )

    payload = {}
    for i in range(len(works)):
        payload['work' + str(i+1)] = json.dumps(works[i])
    r = perform_post('works', payload)
    print r.json

def perform_post(resource, data):
    return requests.post(endpoint(resource), data)


def delete():
    perform_delete('people')
    perform_delete('works')


def perform_delete(resource):
    return requests.delete(endpoint(resource))


def endpoint(resource):
    return '%s/%s/' % (ENTRY_POINT, resource)


def get():
    r = requests.get('http://eve-demo.herokuapp.com')

if __name__ == '__main__':
    delete()
    ids = post_people()
    post_works(ids)
    #get()
