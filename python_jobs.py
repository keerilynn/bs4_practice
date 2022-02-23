import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

#Now we're using keywords to find only Python related jobs.

print("Here are all the jobs with 'Python' in the title:\n")
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#text.lower ensures capitalization does not interfere with our search.
#Not sure about lambda? Here's a helpful link: https://www.programiz.com/python-programming/anonymous-function

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
#Above a list comprehension is used. Here's info on list comprehensions:https://realpython.com/list-comprehension-python/

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print("\n")
    
#Job titles, companies, and locations are printed with a line break between each job posting. Only jobs that contain 'python' in the title are included.
