# azure-container-app

Azure Container Apps is a serverless platform that allows you to maintain less infrastructure and save costs while running containerized apps.
The Azure Container application contains containers deployed from various repositories such as: ACR, GHCR, Docker Hub, etc., these containers can be scheduled by calling azure container app jobs

Azure Container Apps tasks allow you to run container tasks that run for a limited time and port. You can use jobs to perform tasks such as data processing, machine learning, or any scenario where on-demand processing is required.

With Azure Container Apps, you can:

- Run multiple container revisions and manage the container app's application lifecycle.

- Run containers from any registry, public or private, including Docker Hub and Azure Container Registry (ACR).

- Securely manage secrets directly in your application.

- Provide an existing virtual network when creating an environment for your container apps.

## advantages:
- Optimized for running general purpose containers, especially for applications that span many microservices deployed in containers.

- Supports running on demand, scheduled, and event-driven jobs.

-  each container app is linked to a container app environment related to a Log Analytics workspace.

- It differs from other container services in that it includes both Dapr (Distributed Application Runtime) and KEDA (Kubernetes Event-Driven Auto-Sizing)

## Disadvantages:
- Privileged containers: Azure Container Apps doesn't allow privileged containers mode with host-level access. 

- The level of isolation between container applications sharing the same environment is almost non-existent
Therefore it is recommended to host only applications that belong to the same line of business and are likely to interact with each other.

## Limitations:

- Operating system: Linux-based ( linux/amd64 ) container images are required.
