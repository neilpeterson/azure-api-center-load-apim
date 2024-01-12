from azure.identity import DefaultAzureCredential
import json
import requests

class apic_api():
    def __init__(self, api_center, api_name, api_diaplay_name, api_description, custom_data, documentation_url):
        self.api_center = api_center
        self.api_name = api_name
        self.api_display_name = api_diaplay_name
        self.api_description = api_description
        self.custom_data = custom_data
        self.documentation_url = documentation_url

    def new_apic_api(self):
        
        """
        This function creates a new API in Azure API Center.
        API Center REST Reference - https://learn.microsoft.com/en-us/rest/api/apicenter/
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')
        
        url = f"https://management.azure.com/subscriptions/{self.api_center.subscription_id}/resourceGroups/{self.api_center.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.api_center.name}/workspaces/{self.api_center.api_center_workspace_name}/apis/{self.api_display_name}?api-version={self.api_center.api_center_rest_api_version}"

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        body = {
            'properties': {
                'title': self.api_display_name,
                'kind': 'rest',
                # 'description': self.api_description, # Removing for now while we sort description parsing.
                'customProperties': self.custom_data,
                # 'lifecycle': 'Production', # Need to make dynamic once we know what we want to do with this.
                'externalDocumentation': [
                    {
                        'title': 'API Documentation',
                        'url': self.documentation_url
                    }
                ]
            }
        }

        return requests.put(url, headers=headers, data=json.dumps(body))
    
    def new_apic_api_version(self):
        
        """
        This function creates a new API version for a given API in Azure API Center.
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')
        
        url = f"https://management.azure.com/subscriptions/{self.api_center.subscription_id}/resourceGroups/{self.api_center.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.api_center.name}/workspaces/{self.api_center.api_center_workspace_name}/apis/{self.api_display_name}/versions/{self.api_name}?api-version={self.api_center.api_center_rest_api_version}"

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        body = {
            'properties': {
                'title': self.api_name,
                'lifecycleStage': 'Production' # Need to make dynamic once we know what we want to do with this.
            }
        }

        response = requests.put(url, headers=headers, data=json.dumps(body))
        return response

    def get_apic_api(self):
        
        """
        This function gets an API in Azure API Center.
        API Center REST Reference - https://learn.microsoft.com/en-us/rest/api/apicenter/
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')
        
        url = f"https://management.azure.com/subscriptions/{self.api_center.subscription_id}/resourceGroups/{self.api_center.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.api_center.name}/workspaces/{self.api_center.api_center_workspace_name}/apis/{self.api_display_name}?api-version={self.api_center.api_center_rest_api_version}"

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        return requests.get(url, headers=headers)
