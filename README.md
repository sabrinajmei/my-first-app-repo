# sabrinas-first-app-repo
Repo creation in-class practice 

# Setup
Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10
conda activate my-first-env
```
Create requirements.txt file for packages:
- Right click left sidebar, create a new file outside of the app folder
- Name it "requirements.txt"
- In that file, type out all the packages you need: requests, plotly, pandas, python-dotenv, etc.

Install packages:
```sh
pip install -r requirements.txt
```
Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:
```sh
# this is the ".env" file...
ALPHAVANTAGE_API_KEY="_________"

SENDGRID_API_KEY="__________"
SENDER_ADDRESS="example@gmail.com"
 
```
# Usage
Run the example script:
```sh
python app/my_script.py 
OR
python -m app.my_script
```
Run the unemployment report:
```sh
python app/unemployment.py
```
Send an example email:

```sh
python app/email_service.py
```
