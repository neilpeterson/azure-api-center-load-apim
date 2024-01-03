from azure.identity import DefaultAzureCredential
import requests
import os

def GetApi(subcription_id, resource_group_name, api_center_name, api_center_workspace_name, api_name, azure_rest_api_version):

    """
    This function gets an API in Azure API Center.
    """

    credential = DefaultAzureCredential()
    token = credential.get_token('https://management.azure.com/.default')
    
    url = f"https://management.azure.com/subscriptions/{subcription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiCenter/services/{api_center_name}/workspaces/{api_center_workspace_name}/apis/{api_name}?api-version={azure_rest_api_version}"

    headers = {
        'Authorization': 'Bearer ' + token.token,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print(response.json())

if __name__ == '__main__':
    GetApi()   