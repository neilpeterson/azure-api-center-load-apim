from azure.identity import DefaultAzureCredential
import requests
import os

def get_apic_api(subscription_id, api_center_resource_group_name, api_center_name, api_center_workspace_name, api_name, api_center_rest_api_version):

    """
    This function gets an API from Azure API Center.
    """

    credential = DefaultAzureCredential()
    token = credential.get_token('https://management.azure.com/.default')

    url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{api_center_resource_group_name}/providers/Microsoft.ApiCenter/services/{api_center_name}/workspaces/{api_center_workspace_name}/apis/{api_name}?api-version={api_center_rest_api_version}"

    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return response
        