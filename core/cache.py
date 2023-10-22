from django.core.cache import cache


class CachedData:
    def __init__(self, cache_name, model, time):
        self.cache_name = cache_name
        self.model = model
        self.time = time

    def cache_model(self):
        cached_data = cache.get(self.cache_name)

        if cached_data is None:
            cached_data = list(self.model.objects.all())
            cache.set(self.cache_name, cached_data, self.time)
        return cached_data
