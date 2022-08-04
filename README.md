# Urduify

Urduify is a translator that can translate Roman Urdu to Urdu and vice versa.

[Try it out for yourself!](http://ec2-54-184-174-147.us-west-2.compute.amazonaws.com/)


## Authors

- [Abdul Basit](https://www.github.com/abdul3909)
- [Bilal Ahmed](https://www.github.com/bilalahmed15)
- [Zohaib Adnan](https://www.github.com/zohaibadnan137)

We created this translator during our internship at [Folio3 Software](https://www.linkedin.com/company/folio3/).


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
