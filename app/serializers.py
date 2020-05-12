from app.models import Article, Author, Category
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source="author.id")
    author_name = serializers.CharField(read_only=True, source="author.name")
    def create(self, validated_data):
        author_id = validated_data.pop("author", {}).pop("id", None)
        if not author_id:
            raise Exception("Incorrect author id")
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            raise Exception("Author Does Not Exist")
        return Article.objects.create(author=author, **validated_data)

    class Meta:
        model = Article
        fields = ['title', 'content', 'author_id', 'author_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class AuthorDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'id', 'articles']
