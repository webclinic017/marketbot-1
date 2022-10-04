# MarketBot

## API SUPPORT

* [ ] Coinbase
* [x] TD Ameritrade
* [x] polygon.io
* [x] FRED

## API CREDS

In order for the package to work and connect to the APIs on
your system, you must put add the file 'creds.ini' to the directory
'/private/'. The final path of the file will look like '/private/creds.ini'. This file should be formatted as follows:
```
[TDA_AUTH]
API_KEY = <Insert TD Ameritrade API key here>
REDIRECT = <Insert redirect url here (for the corresponding TDA API key's application)
TOKEN_PATH = <insert token file path here (probably root of project)>
ACCOUNT_ID = <Insert TD Ameritrade account id here>

[CB_AUTH]
API_KEY = <Insert Coinbase API key here>
API_SECRET = <Insert Coinbase API secret key here>

[POLY_AUTH]
API_KEY = <Insert polygon.io API key here>
```

## HOW TO INSTALL WITH DOCKER

In order to install and run this project to a container follow these steps:

1. Using a terminal, clone this repository to a directory on your system of choice: \
```git clone https://github.com/jacksteussie/market-bot.git```

2. In the cloned directory build the docker image: \
```docker build -t market-bot -f Dockerfile .```

3. Do the same thing with the API credentials and ```creds.ini``` as described above but in the docker container running the built image.
   
4. Keep in mind, if developing/running tests in the container, you will have to initialize the conda environment inside bash. So when you get into the container and execute a bash shell, type ```conda activate marketbot```.