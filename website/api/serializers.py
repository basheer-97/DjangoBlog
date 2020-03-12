from rest_framework import serializers
from website1.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','cover','cover2','title','slug','author','text','text_2','quote','quote_name','l_heading','l_heading_text','s_heading','s_heading_text','category','created_date','tag_1','tag_2','tag_3')

