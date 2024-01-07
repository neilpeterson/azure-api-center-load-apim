from azure.identity import DefaultAzureCredential
import json
import requests

class apic_api_schema():
    def __init__(self, api_center, custom_data_file_path):
        self.api_center = api_center
        self.custom_data_file_path = custom_data_file_path

    def extend_schema(self):
        
        """
        This function creates a new API Center API metadata schema property.
        This class needs work, currently is just holding the extenstion function.
        Expand to define a schema property class.
        """
        
        credential = DefaultAzureCredential()
        token = credential.get_token('https://management.azure.com/.default')

        headers = {
            'Authorization': 'Bearer ' + token.token,
            'Content-Type': 'application/json'
        }

        with open(self.custom_data_file_path) as f:
            data = json.load(f)

        # Get a list of all property keys, flattten, remove duplicates
        property_keys = [list(item['properties'][0].keys()) for item in data]
        property_keys = [key for sublist in property_keys for key in sublist]
        property_keys = list(set(property_keys))

        for key in property_keys:
            url = f"https://management.azure.com/subscriptions/{self.api_center.subscription_id}/resourceGroups/{self.api_center.resource_group_name}/providers/Microsoft.ApiCenter/services/{self.api_center.name}/metadataSchemas/{key}?api-version={self.api_center.api_center_rest_api_version}"

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

            response = requests.put(url, headers=headers, data=json.dumps(body))
            # ADD some error handling here
