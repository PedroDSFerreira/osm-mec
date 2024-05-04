class AppPkgView:
    @staticmethod
    def _list(data):
        return {
            "id": str(data["_id"]),
            "name": data.get("name"),
            "provider": data.get("provider"),
            "version": data.get("version"),
            "info-name": data.get("info-name"),
            "description": data.get("description"),
        }

    @staticmethod
    def _get(data):
        return {
            "id": str(data["_id"]),
            "appd_id": data.get("appd_id"),
            "name": data.get("name"),
            "provider": data.get("provider"),
            "version": data.get("version"),
            "mec-version": data.get("mec-version"),
            "info-name": data.get("info-name"),
            "description": data.get("description"),
        }

    @staticmethod
    def _save(data, appd):
        return {
            "appd_id": data.get("id"),
            "name": data.get("name"),
            "provider": data.get("provider"),
            "version": data.get("version"),
            "mec-version": data.get("mec-version"),
            "info-name": data.get("info-name"),
            "description": data.get("description"),
            "appd": appd,
        }
