from azure.identity import DefaultAzureCredential
import json
import requests

class apic_api():
    def __init__(self, api_center, api_name, api_description, custom_data):
        self.api_center = api_center
        self.api_name = api_name
        self.api_description = api_description
        self.custom_data = custom_data

    def new_apic_api(self):
        
        """
        This function creates a new API in Azure API Center.
        API Center REST Reference - https://learn.microsoft.com/en-us/rest/api/apicenter/
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')
        
        url = f"https://management.azure.com/subscriptions/{self.api_center.subscription_id}/resourceGroups/{self.api_center.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.api_center.name}/workspaces/{self.api_center.api_center_workspace_name}/apis/{self.api_name}?api-version={self.api_center.api_center_rest_api_version}"

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        body = {
            'properties': {
                'title': self.api_name,
                'kind': 'rest',
                'description': self.api_description,
                'customProperties': self.custom_data
            }
        }

        # TODO - This should return instance of API Center API class
        return requests.put(url, headers=headers, data=json.dumps(body))
    
    def get_apic_api(self):
        
        """
        This function gets an API in Azure API Center.
        API Center REST Reference - https://learn.microsoft.com/en-us/rest/api/apicenter/
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')
        
        url = f"https://management.azure.com/subscriptions/{self.subcription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.name}/workspaces/{self.api_center_workspace_name}/apis/{self.api_name}?api-version={self.azure_rest_api_version}"

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        # TODO - This should return instance of API Center API class
        return requests.get(url, headers=headers)
