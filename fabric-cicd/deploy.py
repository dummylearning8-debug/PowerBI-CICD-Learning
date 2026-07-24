import os

from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items


# Authenticate using Service Principal
credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"],
)


# Configure target workspace
workspace = FabricWorkspace(
    workspace_id=os.environ["DEPLOYMENT_WORKSPACE_ID"],
    environment="dev",
    repository_directory="..",
    item_type_in_scope=[
        "SemanticModel",
        "Report",
    ],
    token_credential=credential,
)


# Deploy Power BI items
publish_all_items(workspace)