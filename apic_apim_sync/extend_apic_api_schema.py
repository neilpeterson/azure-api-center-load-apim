from azure.identity import DefaultAzureCredential
import requests
import os
import json

def extend_apic_api_schema(subscription_id, resource_group_name, api_center_name, custom_data_file_path, azure_rest_api_version):
    
    """
    This function creates a new API Center API metadata schema property.
    """
    
    credential = DefaultAzureCredential()
    token = credential.get_token('https://management.azure.com/.default')

    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-Type': 'application/json'
    }

    with open(custom_data_file_path) as f:
        data = json.load(f)

    # Get a list of all property keys, flattten, remove duplicates
    property_keys = [list(item['properties'][0].keys()) for item in data]
    property_keys = [key for sublist in property_keys for key in sublist]
    property_keys = list(set(property_keys))

    for key in property_keys:
        url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiCenter/services/{api_center_name}/metadataSchemas/{key}?api-version={azure_rest_api_version}"

        body = {
            'properties': {
                "assignedTo": [
                    {
                        "entity": "api",
                        "deprecated": False,
                    }
                ],
                "schema": f'{{\"type\":\"string\", \"title\":\"{key}\"}}'
            }
        }

        # TODO - package these up into a list and return to caller
        requests.put(url, headers=headers, data=json.dumps(body))
