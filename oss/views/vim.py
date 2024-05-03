class VimView:
    @staticmethod
    def _list(data):
        return {
            "id": data["_id"],
            "name": data.get("name"),
        }
