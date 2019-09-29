from django.http import JsonResponse
from django.views import View


class BaseView(View):
    @staticmethod
    def json_result(code=200, msg='OK', data=None):
        res = {
            'code': code,
            'msg': msg,
            'data': data
        }
        return JsonResponse(res)
