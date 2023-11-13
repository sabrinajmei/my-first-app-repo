# my-first-app-repo
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
- In that file, type out all the packages you need: requests, plotly, pandas

Install packages:
```sh
pip install -r requirements.txt
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
