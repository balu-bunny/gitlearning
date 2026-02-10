from typing import Any, Dict, List
import uuid

class MetadataService:
    def __init__(self):
        self._objects: Dict[str, Dict[str, Any]] = {}
        self._layouts: Dict[str, Dict[str, Any]] = {}

    def create_object(self, tenant_id: str, obj: Dict[str, Any]):
        print(f"Creating object for tenant {tenant_id}: {obj}")
        key = f"{tenant_id}:{obj['name']}"
        self._objects[key] = obj
        return obj

    def list_objects(self, tenant_id: str) -> List[Dict[str, Any]]:
        return [v for k, v in self._objects.items() if k.startswith(f"{tenant_id}:")]

    def get_object(self, tenant_id: str, name: str):
        return self._objects.get(f"{tenant_id}:{name}")

    def save_layout(self, tenant_id: str, name: str, layout: Dict[str, Any]):
        key = f"{tenant_id}:{name}"
        self._layouts[key] = layout
        return {"object": name, "layout": layout}
