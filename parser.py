import requests
from bs4 import BeautifulSoup


def getResponse(url=''):
    response = ''
    try:
        response = requests.get(url)
    except Exception:
        print('Ups, something went wrong!')
    return response


def getRandomQuote():
    output = ''
    html = getResponse('https://bash.im/random/')
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'html.parser')
        outputList = soup.find('div', class_ = 'quote__body').contents
        output = quoteToString(outputList)
    return output


def quoteToString(inputList):
    output = ''
    for i in range(len(inputList)):
        if i == 0:
            output += str(inputList[i]).strip()
        elif str(inputList[i]) == '<br/>':
            output += '\n'
        elif str(inputList[i]).strip()[0:4] == '<div':
            break
        else:
            output += str(inputList[i])
    return output
