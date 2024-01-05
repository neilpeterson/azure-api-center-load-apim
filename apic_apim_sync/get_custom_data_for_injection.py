import json

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def return_custom_data_object(obj, api_name, is_property=False, current_api=None):
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

def gen_custom_data(custom_data_file_path, api_name):

    """
    This function generates a JSON object with custom data for the given API.
    """

    custom_data = read_json_file(custom_data_file_path)
    custom_data_object = return_custom_data_object(custom_data, api_name)
    return custom_data_object