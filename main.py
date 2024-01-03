from src.newapi import NewAPI
from src.getapim import GetApimAPI
import os

def main():
    subcription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    api_center_resource_group_name = os.getenv("RESOURCE_GROUP_NAME")
    api_center_name = os.getenv("API_CENTER_NAME")
    api_center_workspace_name = os.getenv("API_CENTER_WORKSPACE_NAME")
    api_center_rest_api_version = os.getenv("API_CENTER_REST_API_VERSION")
    apim_resource_group_name = os.getenv("APIM_RESOURCE_GROUP_NAME")
    apim_name = os.getenv("APIM_NAME")

    apim_apis = GetApimAPI(subcription_id, apim_resource_group_name, apim_name )

    for api in apim_apis:
        NewAPI(subcription_id, api_center_resource_group_name, api_center_name, api_center_workspace_name, api.name, api_center_rest_api_version)

if __name__ == "__main__":
    main()