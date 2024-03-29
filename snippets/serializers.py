from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100, allow_blank=True, default='')
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # MEMO:
    # > Note: Make sure you also add 'owner', to the list of fields in the inner Meta class.
    # Meta class を使う形式のときは……という話だと思う。
    # ex.
    # class Meta:
    #     model = Snippet
    #     fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
    #     owner = serializers.ReadOnlyField(source='owner.username')
    # OR
    #     owner = serializers.CharField(readonly=True, source='owner.username')

    def create(self, validation_data):
        """
        Create and return a new `Snippent` instance, given the validation data
        """
        return Snippet.objects.create(**validation_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
