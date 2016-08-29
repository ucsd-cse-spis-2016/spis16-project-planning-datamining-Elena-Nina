import bs4
from lxml import html
import requests
from bs4 import BeautifulSoup

myUrl = "https://cape.ucsd.edu/responses/Results.aspx?Name=kim&CourseNumber="

page = requests.get(myUrl)

htmlStuff = bs4.BeautifulSoup(page.text, "lxml")

ratings = htmlStuff.select("tr.") 


