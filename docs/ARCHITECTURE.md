# Architecture

## High-level

- **Identity**: Amazon Cognito User Pool (multi-tenant users)
- **API**: Amazon API Gateway -> AWS Lambda (FastAPI)
- **Data**: Amazon DynamoDB tables
  - `PlatformMetadata` (objects, fields, layouts, UI pages)
  - `PlatformRecords` (object records by tenant)
  - `PlatformPermissions` (RBAC)
  - `PlatformAutomations` (workflow/trigger rules)
- **Frontend**: S3 + CloudFront (React)

## Multi-tenancy
- Every record includes `tenant_id`.
- Partition keys are `(tenant_id, entity)` where possible.

## Metadata-driven platform
- Objects are defined by `ObjectDefinition`.
- Fields are stored in metadata and validated at runtime.
- Layouts and UI pages render metadata.

## Automation
- Simple rule engine triggered on CRUD events.
- Rules can create/update records, or post notifications.

## UI Builder
- Page metadata stores component tree JSON.
- Frontend renders components based on this JSON.

## Next Steps
- Add audit logs and field history
- Add search indexing (OpenSearch)
- Add approval workflows
- Add formula fields
