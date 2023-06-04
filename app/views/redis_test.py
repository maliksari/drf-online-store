from rest_framework.views import APIView
from django_redis import get_redis_connection
from rest_framework.response import Response


class RedisView(APIView):
    def get(self, request):
        redis_conn = get_redis_connection("default")
        # Redis bağlantısı üzerinde işlemler yapabilirsiniz
        # Örnek:
        redis_conn.set("mykey", "test")
        return Response("Redis bağlantısı başarılı.")