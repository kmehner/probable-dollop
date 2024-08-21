import requests 
from bs4 import BeautifulSoup

# Fetching data from a website 
response = requests.get('https://www.codingtemple.com/')

# Check the status of our request response 
print(response.status_code)
# print(response.content) #printing the entire content of the response object - not very pretty 

# Use beautiful soup to organize this information (parse the html)
soup = BeautifulSoup(response.content, 'html.parser')

# Make it prettier 
# print(soup.prettify())

# print response.content.title.text 

print(soup.title.text)
# output 'Coding Bootcamp for High-Growth Tech Careers | Coding Temple' 

print(soup.a)
# <a href="https://partner.ascentfunding.com/codingtemple/" target="_blank">Check your eligibility today</a>

print(soup.h1.text)
# Join the #1 technical pathway for high-growth careers