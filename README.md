# Introduction
#### The objective of this repo is to simulate a product that has a simple customer catalog (think of it as a simple customer table) and to build a two-way integration with a customer catalog in an external service - Stripe in this case. The two-way sync is real-time so that a customer added/edited on one system propagates to the other system within a few seconds.

---

# Getting Started
### Project Setup
First, to clone this repository to your local machine run the following command in your git Bash
```
https://github.com/sukhmani1303/two-way-integration.git
```
<i>make sure you clone it into an appropriate folder :)</i>


Then, setup a virtual environment using the following command 

```
virtualenv venv
```

use the following command to install the requirements
```
pip install -r requirements.txt
```

___

### Kafka Setup Using Docker
First, install Docker in your machine & execute the following steps

1. open any terminal and cd into the "docker-kafka" folder
2. run the following command in the terminal
```
docker compose -f docker-compose.yml up -d
```
3. Open Docker & start the "docker-kafka" container to enable kafka

___

### Setup Ngrok & Webhook
1. Download Ngrok file from [here](https://ngrok.com/download)
2. Run the following command after running main.py module to get public url for Webhook
```
ngrok http 8080
```
3. Save the url & endpoint _"<public_url>/inward_sync/update"_ as endpoint url for stripe webhook which listens to **customer.updated**

___

### Setup Stripe
1. Login into Stripe
2. Get all the API keys & store them as json in "Keys.json" file
```
{
    
    "STRIPE_SECRET_KEY" : "<your key>",
    "STRIPE_PUBLISHABLE_KEY" : "<your key>",
    "WEBHOOK_SECRET" : "<your key>"

}

```
___

### Setup PostgreSQL
1. Download & install PostgreSQL
2. Insert Data which you entered in stripe's customer catalog
3. Change the "SQLALCHEMY_DATABASE_URL" inside the database.py module to connect to your local DB

___

# Start The Project
1. Start the "docker-kafka" container in Docker Desktop
2. Activate the virtual environment
3. Run the "k_consumer.py" module in a separate terminal
4. Run "main.py" module
5. Use Ngrok to get a public url & update stripe's Webhook endpoint
6. Run app.py by writing the following command in terminal
```
streamlit run app.py
```

___

# Testing the app
using the streamlit's interface one can 
* update the records & trigger outward sync
* view all the record by applying inward sync changes
