from rest_framework import serializers

from book_shop.models import Author, Book, Review, Rating, Order


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    genre = serializers.ReadOnlyField(source='genre.name')
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'rating_user', 'middle_star')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'image')


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    genre = serializers.ReadOnlyField(source='genre.name')
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        exclude = ('draft', 'url')


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("star", "book")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            book=validated_data.get('book', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating
