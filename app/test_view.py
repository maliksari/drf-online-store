from rest_framework.decorators import api_view
from rest_framework.response import Response
from .demo_task import add, mul, xsum


@api_view(['GET'])
def test_celery(request):
    # Örnek task'ları tetiklemek için kullanılabilir

    # add task'ını çalıştırma
    result_add = add.delay(4, 5)

    # mul task'ını çalıştırma
    result_mul = mul.delay(3, 6)

    # xsum task'ını çalıştırma
    result_xsum = xsum.delay([1, 2, 3, 4, 5])

    return Response({
        'result_add': result_add.id,
        'result_mul': result_mul.id,
        'result_xsum': result_xsum.id
    })