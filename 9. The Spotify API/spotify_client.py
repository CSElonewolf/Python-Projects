#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
import os 
import requests
import datetime 
from urllib.parse import urlencode 
import pprint


# In[ ]:


client_id = "b1f767d933f14dacab7f4062891921bb"
client_secret = "9207250566db44009edf27ca30c1caf3"


# In[ ]:


class SpotifyAPI(object):
    access_token = None;
    access_token_expires = datetime.datetime.now()
    access_token_did_expires = True
    client_id = None
    client_secret = None
    token_url = "https://accounts.spotify.com/api/token"
    
    def __init__(self,client_id,client_secret):
        super().__init__()
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_client_credentials(self):
        """
        Returns A base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception("You must set the client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
        
    def get_token_headers(self):   
        client_creds_b64 = self.get_client_credentials()
        return {
        'Authorization':f"Basic {client_creds_b64}"
        }
    
    
    def get_token_data(self):
        return {
            'grant_type':"client_credentials"
        }
    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_header = self.get_token_headers()
        r = requests.post(token_url,data = token_data,headers = token_header)
        if r.status_code not in range(200,299):
            raise Exception("Could not authenticate client.")
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds = expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expires = expires <  now
        return True
    
    def get_access_token(self):
        token= self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires <now:
            self.perform_auth()
            return self.get_access_token()
        elif token == None:
            self.perform_auth()
            return self.get_access_token()
        return token
    
    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Authorization":f"Bearer {access_token}"
        }
        return headers
    
    def get_resource(self,lookup_id,resource_type='albums',version="v1"):
#         example :-   GET https://api.spotify.com/v1/albums/{id}
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint,headers = headers)
        if r.status_code not in range(200,299):
            return {}
        return r.json()
    
    def get_album(self,_id):
        return self.get_resource(_id,resource_type='albums')
    
    def get_artist(self,_id):
        return self.get_resource(_id,resource_type="artists")
    
    def base_search(self,query_params):
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/search"
        final_endpoint = f"{endpoint}?{query_params}"

        r = requests.get(final_endpoint,headers =headers)
        if r.status_code not in range(200,299):
            return {}
        return r.json()
    
    def search(self,query=None,operator=None,operator_query= None,
                    search_type="track"):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query,dict):
            query = " ".join([f"{k}:{v}" for k,v in query.items()])
        if operator != None and operator_query != None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance(operator_query,str):
                    query = f"{query}{operator}{operator_query}"
        query_params = urlencode({'q':f'{query}','type':f'{search_type.lower()}'})
        print(query_params)
        return self.base_search(query_params)


# In[ ]:


# spotify = SpotifyAPI(client_id,client_secret)
# res = spotify.search(query="Tu Hi Ho"
#                      ,search_type="track")
# res = spotify.search(query={"track":"Tum Ho Ho","artist":"Arijit Singh"})
# print(spotify.access_token_expires)
# res 


# In[ ]:





# In[ ]:





# In[ ]:




