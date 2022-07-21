import logging
from tda import auth
from tda.auth import Client as tda_Client
from coinbase.wallet.client import Client as cb_Client
from configparser import ConfigParser
from typing import Union

def client_connect(api, cfg, log=False) -> Union[cb_Client, tda_Client]:
    '''
        Returns a client connection to Coinbase API or TD Ameritrade API and 
        authenticates the connection with the given keys accordingly. 

        Args:
            api (string) : the api to connect to (either 'TDA' or 'COINBASE')
            log (bool) : enable/disable logging for debugging authentication
            config (string) : path to the config file with auth keys 
        
        Returns:
            A Client object from either the TDA API or the Coinbase API

        Raises:
            AnyError : if connection was unable to be established/authenticated
    '''
    logging.getLogger('').addHandler(logging.StreamHandler())
    config = ConfigParser()
    config.read(cfg)
    API_KEY = config.get(f'{api}_AUTH', 'API_KEY')
    if api == 'TDA':
        REDIRECT = config.get(f'{api}_AUTH', 'REDIRECT')
        TOKEN_PATH = config.get(f'{api}_AUTH', 'TOKEN_PATH')
        try:
            client = auth.client_from_token_file(TOKEN_PATH, API_KEY)
        except FileNotFoundError:
            from selenium import webdriver
            with webdriver.Chrome() as driver:
                client = auth.client_from_login_flow(
                    driver, API_KEY, REDIRECT, TOKEN_PATH)
        return client
    elif api == 'CB':
        API_SECRET = config.get(f'{api}_AUTH', 'API_SECRET')
        client = cb_Client(API_KEY, API_SECRET)
        return client