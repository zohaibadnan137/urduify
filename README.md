# Urduify

Urduify is a translator that can translate Roman Urdu to Urdu and vice versa.

[Try it out for yourself!](http://ec2-54-184-174-147.us-west-2.compute.amazonaws.com/)


## Authors

- [Abdul Basit](https://www.github.com/abdul3909)
- [Bilal Ahmed](https://www.github.com/bilalahmed15)
- [Zohaib Adnan](https://www.github.com/zohaibadnan137)

We created this translator during our internship at [Folio3 Software](https://www.linkedin.com/company/folio3/).


## Technologies

<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Screenshots

![Screenshot](https://user-images.githubusercontent.com/82387424/182638323-ff6ce03c-3415-4d3b-af0a-ff9814ec9e5d.png)


## How It Works

Urduify does not use a learning model. 

For translation from Roman Urdu to Urdu, Urduify uses a dictionary which consists of Roman Urdu and Urdu word pairs. This dictionary has more than 16,000 word pairs, and was assembled using a total of six datasets. 

For translation from Urdu to Roman Urdu, Urduify uses another dictionary which maps Urdu characters to their corresponding English letters. Hence, translation is done character by character.


## Run Locally

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server
```bash
  cd application
  python api.py
```

Run the application
```bash
  cd ../user_interface
  index.html
```
