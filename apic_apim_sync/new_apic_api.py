from azure.identity import DefaultAzureCredential
import requests
import os
import json

def new_apic_api(subcription_id, resource_group_name, api_center_name, api_center_workspace_name, api_name, api_description, custom_data, azure_rest_api_version):
    
    """
    This function creates a new API in Azure API Center.
    API Center REST Reference - https://learn.microsoft.com/en-us/rest/api/apicenter/
    """
    
    credential = DefaultAzureCredential()
    token = credential.get_token('https://management.azure.com/.default')
    
    url = f"https://management.azure.com/subscriptions/{subcription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiCenter/services/{api_center_name}/workspaces/{api_center_workspace_name}/apis/{api_name}?api-version={azure_rest_api_version}"

    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-Type': 'application/json'
    }

    body = {
        'properties': {
            'title': api_name,
            'kind': 'rest',
            'description': api_description,
            'customProperties': custom_data
        }
    }

    return requests.put(url, headers=headers, data=json.dumps(body))