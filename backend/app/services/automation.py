from typing import Any, Dict, List

class AutomationService:
    def __init__(self):
        self._rules: Dict[str, List[Dict[str, Any]]] = {}

    def save(self, tenant_id: str, rule: Dict[str, Any]):
        print(f"Saving rule for tenant {tenant_id}: {rule}")
        self._rules.setdefault(tenant_id, []).append(rule)
        return rule

    def run_rules(self, tenant_id: str, object_name: str, trigger: str, record: Dict[str, Any]):
        for rule in self._rules.get(tenant_id, []):
            if rule.get("object_name") == object_name and rule.get("trigger") == trigger:
                # Minimal stub action handling
                action = rule.get("action", {})
                record["automation"] = action
# Test cases for the AutomationService
if __name__ == "__main__":
    service = AutomationService()
    
    # Test case 1: Save a rule and run it
    rule = {
        "object_name": "TestObject",
        "trigger": "on_create",
        "action": {"type": "update_field", "field": "status", "value": "processed"}
    }
    service.save("tenant1", rule)
    
    record = {"id": 1, "name": "Test Record"}
    service.run_rules("tenant1", "TestObject", "on_create", record)
    
    assert record.get("automation") == {"type": "update_field", "field": "status", "value": "processed"}, "Test case 1 failed"
    
    print("All test cases passed!")
    print("All test cases passed 2!")
