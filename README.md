# Uni-Application-Dashboard

Using Python Beautiful Soup to scrap all these university application dashboard so we don't have to open them one by one everyday!
----------
**How to Download this:**

- Click Clone or Download on the right top corner,
- Click Download Zip and unzip it to your desired location
----------

**Prerequisites:**
- python 3 -> download here https://www.python.org/downloads/
- python 3 packages: `requests, beautifulsoup, pandas`

  After installing python run `pip install requests beautifulsoup pandas` in command prompt, or if you are really lazy you can run the `install.bat`, **remember to replace the email and password in the scrap.py!!!**

- Run the python script by typing `cd `where you store the folder e.g. `cd C:/Users/mark/Downloads/Uni-Application-Dashboard'` then type `python scrap.py` and click enter, or just run the `run.bat` file

If you want to try if any college admission portal dashboard works with this, just add the url to the json list with double quote and a comma if its not at the end of the list!

And please tell me by adding the results to the google sheets below! 

https://docs.google.com/spreadsheets/d/1BNUvivym9dXqMVmSzSrRztvMlR-yOpbyk9WJ5T2uwvI/edit?usp=sharing

----------
Possible Error:

**AttributeError: 'NoneType' object has no attribute 'find_all'**

that means either you forget to set the email and password, or the url you added cannot collect the information so it throws the error!
