import apic_apim_sync as apic
import json
import os

def main():
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    api_center_resource_group_name = os.getenv("RESOURCE_GROUP_NAME")
    api_center_name = os.getenv("API_CENTER_NAME")
    api_center_workspace_name = os.getenv("API_CENTER_WORKSPACE_NAME")
    api_center_rest_api_version = os.getenv("API_CENTER_REST_API_VERSION")
    apim_resource_group_name = os.getenv("APIM_RESOURCE_GROUP_NAME")
    apim_name = os.getenv("APIM_NAME")
    custom_data_file_path = os.getenv("DATA_INJECT_DICT_PATH")

    # # Custom data key to be used when scaffolding custom data file.
    custom_data_key = ['service_tree_id', 'partner_facing']

    # New instance of an API Center Service
    api_center_instance = apic.apic_service(subscription_id, api_center_resource_group_name, api_center_name, api_center_workspace_name, api_center_rest_api_version)
    
    # Get custom API metadata for API schem and extend schema.
    apic_api_schema_instance = apic.apic_api_schema(api_center_instance, custom_data_key)
    apic_api_schema_instance.extend_schema()
    
    # Get all API's from API Gateway (APIM)
    apim_instance = apic.apim_service(subscription_id, apim_resource_group_name, apim_name)
    apim_apis = apic.apim_api(apim_instance).get_all_apis()

    # Get list of APIS in custom data file, to be used when scafolding file.
    custom_data_api_list = apic.get_custom_data_api_list(custom_data_file_path)

    for api in apim_apis:

        if api.name not in custom_data_api_list:
            # Add API scaffolding to custom data file. Values will then need to be added manually.
            apic.add_api_to_custom_data(custom_data_file_path, api.name, custom_data_key)

        # Generate custom data object for API data i.njection.
        custom_data = apic.gen_custom_data(custom_data_file_path, api.name)
        
        # New instance of an API Center API
        apic_api = apic.apic_api(api_center_instance, api.name, api.description, custom_data)

        # Create API in API Center and print response code
        print(apic_api.new_apic_api().json)

if __name__ == "__main__":
    main()