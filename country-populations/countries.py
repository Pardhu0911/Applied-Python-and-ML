# %%
import requests
from bs4 import BeautifulSoup

# %%
#use 50 million and 500 million as test
min_population = int(input('Enter the minimum population: '))
max_population = int(input('Enter the maximum population: '))


# %%
address = requests.get('https://www.scrapethissite.com/pages/simple/', timeout=20)
address.raise_for_status()
soup=BeautifulSoup(address.content,
                   'html.parser')

# %%


# %%
#continue with the code

# Successfully extracting elements that meet search criteria
countries_list = soup.find_all(class_="col-md-4 country")


# %%
# Initialize a counter for the "Number" field in the output
count = 0

for item in countries_list:
    # Extract population and convert to int for comparison
    pop_raw = item.find(class_="country-population").get_text(strip=True)
    current_pop = int(pop_raw)
    
    # Check if the country falls within the user's defined range
    if min_population <= current_pop <= max_population:
        count += 1
        
        # Extract the remaining required elements
        name = item.find(class_="country-name").get_text(strip=True)
        cap = item.find(class_="country-capital").get_text(strip=True)
        area = item.find(class_="country-area").get_text(strip=True)
        
        print(f" Number:  {count} ")
        print(f" Country Name:  {name} ")
        print(f" Capital:  {cap} ")
        print(f" Population:  {current_pop} ")
        print(f" Area:  {area} ")
        print(" ********************************* \n")
