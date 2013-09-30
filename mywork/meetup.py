import requests
import json
import time
from time import strftime
import os


def get_events(group_id,number_of_events,key):

    #
    # construct url to call meetup.com using the group_id and key
    #
    endpoint  = 'https://api.meetup.com/2/events?&sign=true&status=upcoming&offset=0&group_id=' + \
          str(group_id)  +'&page=' + '&page=' + str(number_of_events) + '&key=' + key

    #
    # call meetup.com - get the events for this group
    #
    r = requests.get(endpoint)
    content = json.loads(r.content.decode('utf-8'))

    event_list = list()    # create a container for the results
    
    #
    # go through each event and pull out the stuff that we need
    #
    for result in content['results']:

        this_event = dict() # create a dictionary for each event

        this_event['event_name'] = result['name']
        this_event['description']  = result['description']
        this_event['event_time'] =  time.strftime('%A %B %d, %Y',time.localtime(result['time']/1000))
        venue = result['venue']
        this_event['venue_name'] =  venue['name']
        this_event['address'] =  venue['address_1']
        this_event['city'] =  venue['city']
        this_event['state'] = venue['state']


        #add dictionary to return list
        event_list.append(this_event)

    return event_list
#
# main - call get_events
#

if __name__ == '__main__':
    
         
    ## get keys from the environment
    MEETUP_KEY = os.getenv('MEETUP_KEY')


    # make the call
    group_id = 263790 #NYC Python 
    number_of_events = 2
    meetups = get_events(group_id,number_of_events,MEETUP_KEY)
    
    # print the tweets
    for event in meetups:
        print (event['event_name'])
        print (event['description'])
        print (event['event_time'])
        print (event['venue_name'])
        print (event['address'])
        print (event['city'])
        print (event['state'])
        print('-----------------------------')
