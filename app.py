
import config
import requests


def login(client_id, client_secret, project_key):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = "grant_type=client_credentials&scope=manage_project:%s" % project_key
    url = "https://auth.commercetools.co/oauth/token"
    auth = (client_id, client_secret)
    r = requests.post(url, data=body, headers=headers, auth=auth)
    if r.status_code is 200:
        return r.json()
    else:
        print(r.json())
        raise Exception(
            "Failed to get an access token. Are you sure you have added them to config.py?")


# Keys for possible tables in big query
['id',  'createdAt', 'lastModifiedAt', 'lastModifiedBy', 'productType',
    'catalogs', 'masterData', 'catalogData', 'lastVariantId']


def list_products(auth, project_key):
    headers = {"Authorization": "Bearer %s" % auth["access_token"]}
    url = "https://api.commercetools.co/%s/products" % project_key
    r = requests.get(url, headers=headers)
    products = r.json()
    product_dict = {
        'name': '',
        'description': '',
        'sku': '',

    }
    print(products["results"][0]['masterData']['current'])
    product_dict['name'] =


auth = login(config.CLIENT_ID, config.CLIENT_SECRET, config.PROJECT_KEY)

list_products(auth, config.PROJECT_KEY)
