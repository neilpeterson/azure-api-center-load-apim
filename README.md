# APIM to API Center Load Generator

Gets a list of APIs from Azure API Management Gateway (APIM) and loads them into Azure API Center. Total proof of concept to 'gen some load' in API Center for service evaluation.

## Environment Variables

Update with appropriate values for your environment, this assumes a PowerShell environment. These can be set as configuration settigns in an Azure Function.

```
$env:AZURE_SUBSCRIPTION_ID = ""
$env:RESOURCE_GROUP_NAME = ""
$env:API_CENTER_NAME = ""
$env:API_CENTER_WORKSPACE_NAME = "default"
$env:API_CENTER_REST_API_VERSION = "2024-03-01"
$env:APIM_RESOURCE_GROUP_NAME = ""
$env:APIM_NAME = ""
$env:DATA_INJECT_DICT_PATH = "./data-injection/data-injection.json"
$env:DOCUMENTATION_URL_STRING_FILTER = ""
```

## Custom metadata injection

### API Center API schema

The API Center API schema must be extended before custom metadata can be injected. This takes place in the `extend_api_schema.py` module. This reads all Kay values from the `data-injection/data-injectin.json` file and created an API property for each one. For example, given the following JSON, an API property (optional / string) would be created with the value of `metadata_key`.

```
{
    "api_name": {
        "metadata_key": "metadata_value"
    }
}
```

This allows for dynamic schema extension which may not be desirable.

### API Center API data injection

Once the schema has been extended, custo data can be added to each API Center API. This is done when the API is cerated and / or updated. Property values are read from the `data-injection/data-injectin.json` file and added to the API Center API. For example, given the following JSON, an API property value is added with the value of `metadata_value`.

```
{
    "api_name": {
        "metadata_key": "metadata_value"
    }
}
```
