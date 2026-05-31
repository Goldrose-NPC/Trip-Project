from utils.serializers import BaseSerializer


def normalize_image_url(field_file):
    if not field_file:
        return ''

    raw_name = getattr(field_file, 'name', '') or ''
    raw_name = raw_name.replace('\\', '/')
    if raw_name.startswith('http://') or raw_name.startswith('https://'):
        return raw_name
    if raw_name.startswith('/static/'):
        return raw_name
    if raw_name.startswith('static/'):
        return '/' + raw_name

    return field_file.url


class BaseImageSerializer(BaseSerializer):
    """ 序列化基础图片： 其他列表需要用到时引用 """

    def to_dict(self):
        image = self.obj
        return {
            'img': normalize_image_url(image.img),
            'summary': image.summary
        }
