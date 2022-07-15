class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        # if self.request.method == 'POST':
        #     return DetailParkingLotSerializer
        # elif self.request.method == 'GET':
        #     return ListParkingLotSerializer
        return self.serializer_map.get(self.request.method, self.serializer_class)
        # return self.serializer_map.get("POST")