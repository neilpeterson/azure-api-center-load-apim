import apic_apim_sync as apic
import os
import json

def main():
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    api_center_resource_group_name = os.getenv("RESOURCE_GROUP_NAME")
    api_center_name = os.getenv("API_CENTER_NAME")
    api_center_workspace_name = os.getenv("API_CENTER_WORKSPACE_NAME")
    api_center_rest_api_version = os.getenv("API_CENTER_REST_API_VERSION")
    apim_resource_group_name = os.getenv("APIM_RESOURCE_GROUP_NAME")
    apim_name = os.getenv("APIM_NAME")
    custom_data_file_path = os.getenv("DATA_INJECT_DICT_PATH")

    apic.extend_apic_api_schema(subscription_id, api_center_resource_group_name, api_center_name, custom_data_file_path, api_center_rest_api_version)
    
    apim_apis = apic.get_apim_api(subscription_id, apim_resource_group_name, apim_name)

    for api in apim_apis:

        custom_data = apic.gen_custom_data(custom_data_file_path, api.name)
        new_api = apic.new_apic_api(subscription_id, api_center_resource_group_name, api_center_name, api_center_workspace_name, api.name, api.description, custom_data, api_center_rest_api_version)
        print(new_api)

if __name__ == "__main__":
    main()