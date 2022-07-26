import logging
from tda import auth
from tda.auth import Client as TDA_Client
from coinbase.wallet.client import Client as CB_Client
from configparser import ConfigParser
from typing import Union
from pykrakenapi import KrakenAPI
import krakenex

def client_connect(api, cfg, log=False) -> Union[CB_Client, TDA_Client]:
    '''
        Returns a client connection to the given api and 
        authenticates the connection with the given keys accordingly. 

        Args:
            api (str) : the api to connect to (e.g. 'TDA' or 'CB')
            log (bool) : enable/disable logging for debugging authentication
            cfg (str) : path to the config file with api keys 
        
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
        client = CB_Client(API_KEY, API_SECRET)
        return client