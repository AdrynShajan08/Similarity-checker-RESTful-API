# Similarity-checker-RESTful-API
RESTful API For Similarity Check Using NLP and Docker

This repo has :
1) *`Dockerfile`*: Configuration file for building the Docker image.
2) *`app.py`*: The main Flask application file.
3) *`utils.py`*: Utility file containing the NLP and similarity check functions.
4) *`requirements.txt`*: File containing the required Python packages.

Steps to follow:
1) pip install the requirements.txt file
2) Build the Docker image:
   *docker build -t similarity-check .*
3) After the build is successful, run the Docker container:
   *docker run -p 5000:5000 similarity-check*
4) Access the API at 'http://localhost:5000/similarity' using any REST client, such as Postman or cURL, with a POST request.
