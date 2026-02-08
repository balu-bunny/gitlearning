from typing import Any, Dict, List

class PermissionsService:
    def __init__(self):
        self._permissions: Dict[str, List[Dict[str, Any]]] = {}

    def save(self, tenant_id: str, permission: Dict[str, Any]):
        self._permissions.setdefault(tenant_id, []).append(permission)
        return permission
