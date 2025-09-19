__all__ = [
    "owner_fields",
    "base_model_fields",
]

owner_fields = {"owner__id": ["exact"]}

base_model_fields = {
    "id": ["exact"],
    "created": ["exact", "gt", "lt", "gte", "lte"],
    "modified": ["exact", "gt", "lt", "gte", "lte"],
}
