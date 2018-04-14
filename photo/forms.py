# 폼셋이란 동일한 폼 여러개로 구성된 폼을 말합니다. 인라인 폼셋이란 메인 폼에 딸려 있는 하위 폼셋을 말하는 것으로,
# 테이블간의 관계가 1:N 인경우, N 테이블의 레코드 여러개를 한꺼번에 입력박기 위한 폼으로 사용됩니다.
from photo.models import Album,Photo
from django.forms.models import inlineformset_factory

PhotoInlineFormSet = inlineformset_factory(Album,Photo,fields=['image','title','description'],extra=2)
