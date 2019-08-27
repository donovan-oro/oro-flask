
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
    product_list = []
    for i in range(len(products["results"])):
        product_dict = {
            'name': '',
            'description': '',
            'sku': '',
            'prices': [],
            'images': [],
            'seller': '',
            'is-oro-certified': '',
            'benefits': ''}
        print(products["results"][i]['masterData']['current'])
        product_dict['name'] = products["results"][i]['masterData']['current']['name']['en']
        product_dict['description'] = products["results"][i]['masterData']['current']['description']['en']
        product_dict['sku'] = products["results"][i]['masterData']['current']['masterVariant']['sku']
        [product_dict['prices'].append(price['value']['centAmount'])
         for price in products["results"][i]['masterData']['current']['masterVariant']['prices']]

        [product_dict['images'].append(image['url'])
         for image in products["results"][i]['masterData']['current']['masterVariant']['images']]
        print('\n')
        for val in products["results"][i]['masterData']['current']['masterVariant']['attributes']:
            if val['name'] == 'seller':
                product_dict['seller'] = val['value']

            if val['name'] == 'is-oro-certified':
                product_dict['is-oro-certified'] = val['value']

            if val['name'] == 'cbd':
                product_dict['cbd'] = val['value']

            if val['name'] == 'aroused':
                product_dict['aroused'] = val['value']

            if val['name'] == 'rested':
                product_dict['rested'] = val['value']

            if val['name'] == 'calm':
                product_dict['calm'] = val['value']

            if val['name'] == 'happy':
                product_dict['happy'] = val['value']

            if val['name'] == 'pain-relief':
                product_dict['pain-relief'] = val['value']

            if val['name'] == 'beautiful':
                product_dict['beautiful'] = val['value']

            if val['name'] == 'energized':
                product_dict['energized'] = val['value']

            if val['name'] == 'focused':
                product_dict['focused'] = val['value']

            if val['name'] == 'general-wellness':
                product_dict['general-wellness'] = val['value']

            if val['name'] == 'food-beverages':
                product_dict['food-beverages'] = val['value']
        # print('\nFor this product, the schema looks like\n')
        product_list.append(product_dict)
    print(product_list)


# ['name', 'description', 'sku', 'prices', 'images', 'seller', 'is-oro-certified', 'benefits', 'cbd', 'aroused', 'rested', 'calm', 'happy', 'pain-relief', 'beautiful', 'energized', 'focused', 'general-wellness', 'food-beverages']
auth = login(config.CLIENT_ID, config.CLIENT_SECRET, config.PROJECT_KEY)

list_products(auth, config.PROJECT_KEY)
