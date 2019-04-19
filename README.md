# DrfBootcamp
Code for DRF bootcamp conducted on Apr 2019 with Django and DRF

### Installation instruction
1. Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
2. Clone this repo and `cd DrfBootcamp`
3. Run `virtualenv venv -p python3.6`
4. Run `pip install -r requirements.txt`
5. Run `python manage.py migrate`
6. Go to `localhost:8000` in your browser. 


### Deployment to Heroku:
1. Download heroku cli
2. Heroku login
3. go to project root
4. Run: `heroku:apps create <app_name>`
5. Run: `git push heroku master`
6. Go to `<app_name>.herokuapp.com/api/v1` in your browser
