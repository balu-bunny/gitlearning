from typing import Any, Dict, List

class UiBuilderService:
    def __init__(self):
        self._pages: Dict[str, List[Dict[str, Any]]] = {}

    def save_page(self, tenant_id: str, page: Dict[str, Any]):
        self._pages.setdefault(tenant_id, []).append(page)
        return page

    def list_pages(self, tenant_id: str):
        return self._pages.get(tenant_id, [])
