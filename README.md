# azure-api-center-load-apim

Gets a list of APIs from Azure API Management Gateway (APIM) and loads them into Azure API Center. Total proof of concept to 'gen some load' for API Center for service evaluation. Can be extended to add custom metadata, etc..

## Virtual env and pacakges

```
python3 -m venv .venv
pip install -r requirements.txt
```

## Environment Variables

Update with appropriate values for your environment. This assumes a PowerShell environment.

```
$env:AZURE_SUBSCRIPTION_ID = ""
$env:RESOURCE_GROUP_NAME = ""
$env:API_CENTER_NAME = ""
$env:API_CENTER_WORKSPACE_NAME = "default"
$env:API_CENTER_REST_API_VERSION = "2024-03-01"
$env:APIM_RESOURCE_GROUP_NAME = ""
$env:APIM_NAME= ""
```

## Sync APIM with API Center

```
python ./main.py  
```

## Notes

At currnet, an empty REST API is created in API Center with the name of the the API's found in APIM. All APIM API properties are returned for suture consumption.
