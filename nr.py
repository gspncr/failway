import logging
import threading
import io
import datetime as dt
from flask import *
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from oneagent.sdk import SDK, ChannelType, Channel

app = Flask(__name__)
logging.basicConfig(filename='trc.log',level=logging.INFO,format='%(asctime)s %(message)s')

timeHour = dt.datetime.now().hour
hour = str(timeHour)
currentNow = str(dt.datetime.now())

if timeHour < 10:
    my_url = 'http://ojp.nationalrail.co.uk/service/timesandfares/WHP/LTN/today/0' + hour + '00/dep'
else:
    my_url = 'http://ojp.nationalrail.co.uk/service/timesandfares/WHP/LTN/today/' + hour + '00/dep'

def trains():
    timeHour = dt.datetime.now().hour
    hour = str(timeHour)
    currentNow = str(dt.datetime.now())

    if timeHour < 10:
        my_url = 'http://ojp.nationalrail.co.uk/service/timesandfares/WHP/LTN/today/0' + hour + '00/dep'
    else:
        my_url = 'http://ojp.nationalrail.co.uk/service/timesandfares/WHP/LTN/today/' + hour + '00/dep'

    #my_url = 'http://ojp.nationalrail.co.uk/service/timesandfares/WHP/LTN/today/' + hour + '00/dep'

    #opening connection, grabbing page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #html parsing
    page_soup = soup(page_html, "html.parser")

    #grab each train
    rows = page_soup.findAll("tr",{"class":"mtx"})

    # len(rows) --count the rows (mx)
    #   rows[0] --display row 1 (mx 1)

    #get time of train
    row = rows[0]
    entries = str(len(rows))
    #print("---------------------------------------")
    found = "found " + entries + " valid journeys on page " + my_url
    logging.info(found)
    #print("---------------------------------------")
    time = row.findAll("td", {"class":"dep"})
    #print(time[0].text)
    logging.info(time[0].text)

    status = row.findAll("div", {"class":"journey-status"})
    #print(status[0].text.strip())
    logging.info(status[0].text.strip())
    journeys = []
    for trn in rows:

        time = trn.findAll("td", {"class":"dep"})
        #print(time[0].text)

        time[0].text
        logging.info(time[0].text)

        status = trn.findAll("div", {"class":"journey-status"})
        ans = status[0].text.strip()

        #print("train time: " + time[0].text)
        logging.info("train time: " + time[0].text)
        #print("train status: " + ans)
        logging.info("train status: " + ans)
        #print("service " + time[0].text + " has status " + ans)
        logging.info("service " + time[0].text + " has status " + ans)
        #print("---------------------------------------")
        varb="service " + time[0].text + " has status " + ans
        #for journey in journeys:
        journeys.append(varb.strip())
        timeSt = str(time[0].text)
        writeDelays(timeSt, ans)

    else:
        logging.info("done all " + entries + " entries at: " + currentNow)

    #print(journeys)
    #print (len(journeys))
    return(journeys)

def writeDelays(train, status):
    with open('file.txt', 'a') as file:
        file.writelines(train)
        file.writelines(",")
        file.writelines(status)
        file.writelines('\n')

@app.route('/', methods=["GET"])
def index():
    return render_template("layout.html", train = trains, url=my_url, session=hour)

@app.route('/about/')
def about():
    return '<a href="/">return home</a><br>hi, this is a quick something by gary spencer <a href="http://twitter.com/gspncr">@gspncr</a>'

@app.route('/batch/', methods=['GET'])
def metrics():
    return redirect('static/batch.txt')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.errorhandler(503)
def page_not_found(e):
    return render_template('500.html'), 503

#if __name__ == '__main__':
#    app.run(host='localhost', port=8070)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
