# Uni-Application-Dashboard

Using Python Beautiful Soup to scrap all these university application dashboard so we don't have to open them one by one everyday!
----------
**How to Download this:**

- Click Clone or Download on the right top corner,
- Click Download Zip and unzip it to your desired location
----------

**Prerequisites:**
- python 3 -> download here https://www.python.org/downloads/
- python 3 packages: `requests, beautifulsoup4, pandas, lxml`

After installing python run `pip install requests beautifulsoup pandas lxml` in command prompt (If you are running on Mac run `easy_install pip` then run the command above), or if you are really lazy you can run the `install.bat`, **remember to replace the email and password in the scrap.py!!!**

- Run the python script by typing `cd `where you store the folder e.g. `cd C:/Users/mark/Downloads/Uni-Application-Dashboard` then type `python scrap.py` and click enter, or just run the `run.bat` file

If you want to try if any college admission portal dashboard works with this, just add the url to the json list with double quote and **a comma at the 2nd last item (look at the format of the lines above you will see the pattern - VERY IMPORTANT TO ADD A COMMA WHEN YOU ADD A NEW ITEM**

And please tell me by adding the results to the google sheets below! 

https://docs.google.com/spreadsheets/d/1BNUvivym9dXqMVmSzSrRztvMlR-yOpbyk9WJ5T2uwvI/edit?usp=sharing

----------
Possible Error:

**AttributeError: 'NoneType' object has no attribute 'find_all'**

that means either you forget to set the email and password, or the url you added cannot collect the information so it throws the error!
