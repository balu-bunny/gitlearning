from typing import Any, Dict, List

class AutomationService:
    def __init__(self):
        self._rules: Dict[str, List[Dict[str, Any]]] = {}

    def save(self, tenant_id: str, rule: Dict[str, Any]):
        self._rules.setdefault(tenant_id, []).append(rule)
        return rule

    def run_rules(self, tenant_id: str, object_name: str, trigger: str, record: Dict[str, Any]):
        for rule in self._rules.get(tenant_id, []):
            if rule.get("object_name") == object_name and rule.get("trigger") == trigger:
                # Minimal stub action handling
                action = rule.get("action", {})
                record["automation"] = action
