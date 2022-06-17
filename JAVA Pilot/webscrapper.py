import requests
import bs4
import lxml
var = input("Enter programming language:")
url = "https://www.udacity.com/courses/all?field=school-of-programming&search="+var
result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,"lxml") 
soup.select('div catalog-v2_results__1FjDi')