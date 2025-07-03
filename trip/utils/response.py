from django.http import JsonResponse


class NotFoundJsonResponse(JsonResponse):
    """ 400 对应的JSON响应 """
    status_code = 400
    def __init__(self, *args, **kwargs):

        data = {
            "error_code": "40400",
            "error_msg": "您访问的内容不存在或已被删除",
            }
        super().__init__(data, *args, **kwargs)


class BadRequestJsonResponse(JsonResponse):
    """ 500 """
    status_code = 400

    def __init__(self, err_list=[], *args, **kwargs):
        data = {
            "error_code": "40000",
            "error_msg": "参数格式不正确",
            "err_list": err_list
        }
        super().__init__(data, *args, **kwargs)


class MethodNotAllowedJsonResponse(JsonResponse):
    """ 请求方式不被允许 """
    status_code = 405

    def __init__(self, *args, **kwargs):
        data = {
            "error_code": "405000",
            "error_msg": "请求方式不被允许",
        }
        super().__init__(data, *args, **kwargs)


class UnauthenticatedJsonResponse(JsonResponse):
    """ 未登录，请登录 """
    status_code = 401

    def __init__(self, *args, **kwargs):
        data = {
            "error_code": "401000",
            "error_msg": "请登录",
        }
        super().__init__(data, *args, **kwargs)


class ServerErrorJsonResponse(JsonResponse):
    """ 表单未通过验证 """
    status_code = 500

    def __init__(self, *args, **kwargs):
        data = {
            "error_code": "500000",
            "error_msg": "服务器正忙，请稍后重试",
        }
        super().__init__(data, *args, **kwargs)