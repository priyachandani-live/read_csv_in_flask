This Flask application is about reading static csv files.

## static folder
This is the folder, where all your static files files will be included. In our case the static file is a csv file.
Therefore, whichever file you have to make the app read, needs to be resided in the static folder.

## templates folder
This folder is as important as the one static one. Since, the app.py file is using render_template(), which specifically looks
for the templates folder. Hence, to make sure your file is read in the browser, put your html files within the templates folder.

## steps
1. Create a static folder and put the csv file within it.
2. Run the flask app, at /csv route your csv file will be read.
3. To run, use `python app.py` and at port 5000 your application shall be up.
4. At route `localhost:5000/csv` you shall be able to view your csv data.


# Steps for containerisation
1. Create a Dockerfile in the root directory.
2. Add the required lines in the Dockerfile.
* Note: It is important to have the requirements.txt file.
3. To run the dockerfile and create a docker image use `docker build -t flask-app .` where 'flask-app' is the tag name and '.' indicates to use th current directory's dockerfile.
4. Once image is created, run the docker container using `docker run -p 5000:5000 flask-app` command.
