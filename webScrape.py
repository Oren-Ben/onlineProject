import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')     #like a web browser
# print(res.text) # read the resposse because we received a document
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stoires_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'],reverse=True)    # sort the hnlist by the rvotes

def create_custom_HN(links,subtext):
    hn = []
    for index,item in enumerate(links): # I used enumerate to run over the subtext in the loop in the vote parameter

        # title = links[index].getText() # another option
        title = item.getText()
        href = links[index].get('href', None)    # default = None
        vote = subtext[index].select('.score')
        if len(vote):   # take only if there are points in the page
            points = int(vote[0].getText().replace(' points', ''))  # take only the points
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stoires_by_votes(hn)


pprint.pprint(create_custom_HN(links, subtext))
