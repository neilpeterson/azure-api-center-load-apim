class apic_service():
    def __init__(self, subscription_id, resource_group_name, name, api_center_workspace_name, api_center_rest_api_version):
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.name = name
        self.api_center_workspace_name = api_center_workspace_name
        self.api_center_rest_api_version = api_center_rest_api_version