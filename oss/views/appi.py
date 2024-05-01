class AppiView:
    @staticmethod
    def _list(data):
        return {
            "id": str(data["_id"]),
            "name": data.get("name"),
            "description": data.get("description"),
            "operational-status": data.get("operational-status"),
            "config-status": data.get("config-status"),
            "details": data.get("detailed-status"),
            "created-at": data.get("create-time"),
        }

    @staticmethod
    def _get(data):
        return AppiView._list(data)
