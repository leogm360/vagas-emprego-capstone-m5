class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(
            self.request.method, self.serializer_class
        )


class SerializerByAccountTypeMixin:
    def get_serializer_class(self, *args, **kwargs):
        recruiter_request = self.request.data.get("is_human_resources", False)
        recruiter_token = getattr(
            self.request.user, "is_human_resources", False
        )

        if recruiter_request or recruiter_token:
            return self.serializer_map.get("HUMAN_RESOURCES")
        else:
            return self.serializer_map.get("CANDIDATE")
