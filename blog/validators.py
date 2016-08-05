import re
import requests
from django.conf import settings
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
import xmltodict

@deconstructible
class ZipCodeValidator(object):
    '우편번호 체계안내: http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'

    def __init__(self, is_check_exist=False):
        self.is_check_exist=is_check_exist

    def __call__ (self, zip_code):
        if not re.match(r'^\d{5}$', zip_code):
            raise ValidationError('5자리 숫자로 입력해주세요.')

        if self.is_check_exist:
            self.check_exist(zip_code)

    def check_exist(self, zip_code):
        '우체국 open api: http://biz.epost.go.kr/customCenter/custom/custom_10.jsp'

        params={
            'regkey': settings.EPOST_API_KEY,
            'target': 'postNew',
            'query': zip_code,
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response=xmltodict.parse(xml)
        try:
            error=response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))