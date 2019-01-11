#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 20:40:52 2019

@author: mark
"""
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import re
import webbrowser
import os

payload = {
    # type your used email here with quote around it like this 'email', I assume you use the same set of account and password for all the application
    'email': '',
    'password': ''  # type your password here with quote around it like this 'password'
}

with open("input.json") as input_file:
    login_urls = json.load(input_file)
    e = []

    for url in login_urls:
        session_requests = requests.session()
        result = session_requests.post(url, data=payload)
        c = result.content
        soup = BeautifulSoup(c, "lxml")
        table = soup.find('table', {"class": "nohighlight table"})
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() or 'Null' for ele in cols]
                cols.extend([re.search('\w+(?=\.+edu)', url).group(0)])
                e.append([ele for ele in cols if ele])  # Get rid of empty values}


    df = pd.DataFrame(e).rename(
        columns={1: 'Status', 2: 'Item', 3: 'Date', 4: 'College'})
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.groupby('College')
    htmls = [grp.to_html(classes='order-table ui celled table')
             for team, grp in df]
    dataframe_html = u''.join(htmls)
    # for df, df_region in df.groupby('4'):
        # print(df_region)
# Declare your table
pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
  <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
  <link rel="stylesheet" type="text/css" href="main.css"/>
  <script src="main.js"></script>
  <body>
    <section class="container">
        <h2>Uni Application Dashboard</h2>
        <input type="search" class="light-table-filter" data-table="order-table" placeholder="Filter">
        {table}
    </section>
  </body>
</html>.
'''

# OUTPUT AN HTML FILE
with open('results.html', 'w') as f:
    f.write(html_string.format(table=dataframe_html))
    webbrowser.open('file://' + os.path.realpath('results.html'))
