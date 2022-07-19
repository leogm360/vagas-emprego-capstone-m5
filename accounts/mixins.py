class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(
            self.request.method, self.serializer_class
        )


class SerializerByAccountTypeMixin:
    def get_serializer_class(self, *args, **kwargs):
        is_humam_resources = self.request.data.get("is_human_resources", False)

        if is_humam_resources:
            return self.serializer_map.get("HUMAN_RESOURCES")
        else:
            return self.serializer_map.get("CANDIDATE")
