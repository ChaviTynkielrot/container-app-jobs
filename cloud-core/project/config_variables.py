# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv
import os

load_dotenv()

tenant_id = os.getenv("TENANT_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
application_id = os.getenv("APPLICATION_ID")
keyvault_uri = os.getenv("KEYVAULT_URI")



# keyvault_uri=os.getenv("KEYVAULT_URI")
# secret_name = os.getenv("SECRET")
# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=keyvault_uri, credential=credential)
# secret = client.get_secret(secret_name)
# connection_string = secret.value