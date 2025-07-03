from system.serializer import BaseImageSerializer
from utils.serializers import BaseListPageSerializer, BaseSerializer


class UserSerializer(BaseSerializer):
    """ 用户基础信息 """
    def to_dict(self):
        user = self.obj
        return {
            'nickname': user.nickname,
            'avatar': user.avatar.url
        }

class UserProfileSerializer(BaseSerializer):
    """ 用户详细信息 """
    def to_dict(self):
        profile = self.obj
        return {
            'real_name': profile.real_name,
            'sex': profile.sex,
            'sex_display': profile.get_sex_display(),
        }
