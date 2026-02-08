from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from .services.metadata import MetadataService
from .services.records import RecordsService
from .services.permissions import PermissionsService
from .services.automation import AutomationService
from .services.ui_builder import UiBuilderService

app = FastAPI(title="Platform MVP")

metadata = MetadataService()
records = RecordsService(metadata)
permissions = PermissionsService()
automation = AutomationService()
ui_builder = UiBuilderService()

class ObjectDefinition(BaseModel):
    name: str
    label: str
    fields: List[Dict[str, Any]] = Field(default_factory=list)

class LayoutDefinition(BaseModel):
    object_name: str
    layout: Dict[str, Any]

class RecordPayload(BaseModel):
    data: Dict[str, Any]

class PermissionDefinition(BaseModel):
    role: str
    object_name: str
    can_create: bool = True
    can_read: bool = True
    can_update: bool = True
    can_delete: bool = True

class AutomationRule(BaseModel):
    object_name: str
    trigger: str
    condition: Dict[str, Any] = Field(default_factory=dict)
    action: Dict[str, Any] = Field(default_factory=dict)

class PageDefinition(BaseModel):
    name: str
    page: Dict[str, Any]

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/objects")
def create_object(obj: ObjectDefinition, tenant_id: str = "default"):
    return metadata.create_object(tenant_id, obj.dict())

@app.get("/objects")
def list_objects(tenant_id: str = "default"):
    return metadata.list_objects(tenant_id)

@app.get("/objects/{name}")
def get_object(name: str, tenant_id: str = "default"):
    obj = metadata.get_object(tenant_id, name)
    if not obj:
        raise HTTPException(status_code=404, detail="Object not found")
    return obj

@app.post("/objects/{name}/layouts")
def create_layout(name: str, layout: LayoutDefinition, tenant_id: str = "default"):
    return metadata.save_layout(tenant_id, name, layout.layout)

@app.post("/objects/{name}/records")
def create_record(name: str, payload: RecordPayload, tenant_id: str = "default"):
    record = records.create_record(tenant_id, name, payload.data)
    automation.run_rules(tenant_id, name, "create", record)
    return record

@app.get("/objects/{name}/records")
def list_records(name: str, tenant_id: str = "default"):
    return records.list_records(tenant_id, name)

@app.post("/permissions")
def add_permission(p: PermissionDefinition, tenant_id: str = "default"):
    return permissions.save(tenant_id, p.dict())

@app.post("/automations")
def add_automation(a: AutomationRule, tenant_id: str = "default"):
    return automation.save(tenant_id, a.dict())

@app.post("/pages")
def add_page(p: PageDefinition, tenant_id: str = "default"):
    return ui_builder.save_page(tenant_id, p.dict())

@app.get("/pages")
def list_pages(tenant_id: str = "default"):
    return ui_builder.list_pages(tenant_id)

# AWS Lambda adapter
try:
    from mangum import Mangum
    handler = Mangum(app)
except Exception:
    handler = None
