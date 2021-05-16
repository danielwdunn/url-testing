import requests
import csv
from pandas import read_csv

#Set List of URLs to Audit in CSV Format. Column 1 = URL, Column 2 = Category

data = read_csv('masterlist.csv')

#Set Variables
sites = data['url'].tolist()
category = data['category_code'].tolist()

#Set Browser Headers
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch, identity',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}

#Try URLs and write to CSV
for s, c in zip(sites,category):
    try:
        response = requests.get(s, headers=headers, timeout=3)
        print(s,c,response)
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s,c,response])
    except requests.exceptions.HTTPError as exception:
        print(s,c,'httperror')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s,c, 'httperror'])
    except requests.exceptions.ConnectionError as e:
        print(s,c,'connection error')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s,c, 'connection error'])
    except requests.exceptions.Timeout as timeout:
        print(s,c,'timeout')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s,c, 'timeout error'])
    except requests.exceptions.TooManyRedirects as results_file:
        print(s, c, 'too many redirects')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s, c, 'Too many redirects'])
    except requests.exceptions.InvalidURL as results_file:
        print(s, c, 'Invalid Url')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s, c, 'Invalid Url'])
    except requests.exceptions.MissingSchema as results_file:
        print(s, c, 'Null Value for Url')
        with open('results.csv', mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([s, c, 'Null'])
