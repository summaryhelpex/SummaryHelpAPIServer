SummaryHelp API Server
=============================================
![Alt text](/.static_root/images/sh_logo.png) 

Introduce
================================================
SummaryHelp API Server is a api server that analyzes english article and returns summary keyword.

You need to send the article in form-data format to the 80 port of/upload in post format

it analyzes english article and returns them by extracting important keywords

model 

SummaryHelp API Server installation
====================================
We also support Windows OS, but we recommend Ubuntu OS.

Set up python
----------------------------------

'''
To set up python: http://www.python.org
$ sudo apt-get install python3
'''

How to install
--------------------------------
**************************

'''
$ git clone https://github.com/summaryhelpex/SummaryHelp_APIServer.git
$ cd SummaryHelp_APIServer
$ pip install -r requirements.txt'''

How to run in local
--------------------------------
***************************

$ cd SummaryHelp_APIServer/summaryhelper
$ python manage.py runserver

SummaryHelp Client
===========================
'''If you want use SummaryHelp Client, then come with https://github.com/summaryhelpex/SummaryChrome_Client.git'''
