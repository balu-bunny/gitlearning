from typing import Any, Dict, List
import uuid

class RecordsService:
    def __init__(self, metadata_service):
        self._records: Dict[str, List[Dict[str, Any]]] = {}
        self.metadata = metadata_service

    def create_record(self, tenant_id: str, object_name: str, data: Dict[str, Any]):
        obj = self.metadata.get_object(tenant_id, object_name)
        if not obj:
            raise ValueError("Object not defined")
        record = {"id": str(uuid.uuid4()), "data": data}
        key = f"{tenant_id}:{object_name}"
        self._records.setdefault(key, []).append(record)
        return record

    def list_records(self, tenant_id: str, object_name: str):
        key = f"{tenant_id}:{object_name}"
        return self._records.get(key, [])
