import json
import re

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def get_api_names(data):
    api_names = [item['api'] for item in data]
    return api_names

def return_custom_data_object(obj, api_name, is_property=False, current_api=None):

    """
    This function returns a JSON object with custom data properties for the given API.
    This will be used to add custo data on the API Center API.
    """
    
    properties = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'api':
                current_api = value
            if is_property and (api_name is None or current_api == api_name):
                properties[key] = value
            properties.update(return_custom_data_object(value, api_name, key == 'properties', current_api))
    elif isinstance(obj, list):
        for item in obj:
            properties.update(return_custom_data_object(item, api_name, is_property, current_api))
    return properties

def get_custom_data_api_list(custom_data_file_path):

    """
    This function returns a list of API names found in the custom data file.
    This list will be used to determine if an API needs to be added to the custom data file.
    """

    custom_data = read_json_file(custom_data_file_path)
    api_list = get_api_names(custom_data)
    return api_list

def add_api_to_custom_data(custom_data_file_path, api_name, api_display_name, documentation_url, custom_data_key):

    """
    This function adds a new API to the custom data file.
    """

    properties_dict = {i: None for i in custom_data_key}
    custom_data = read_json_file(custom_data_file_path)
    custom_data.append({'api': api_name, 'api_display_name': api_display_name, 'documentation_url': documentation_url, 'properties': properties_dict})
    with open(custom_data_file_path, 'w') as f:
        json.dump(custom_data, f, indent=4)

def gen_custom_data(custom_data_file_path, api_name):

    """
    This function generates a JSON object with custom data for the given API.
    """

    custom_data = read_json_file(custom_data_file_path)
    custom_data_object = return_custom_data_object(custom_data, api_name)
    return custom_data_object

def get_documentation_url(api_description, documentation_url_string_filter):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', api_description)

    for url in urls:
        if documentation_url_string_filter in url:
            return url