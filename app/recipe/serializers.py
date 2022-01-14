from rest_framework import serializers


from core.models import Tag,Ingredient,Recipe


class TagSerializer(serializers.ModelSerializer):
    #Serialize the tag object

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    #serialize the ingredient objects
    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    #serialize the Recipe objects
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset = Tag.objects.all()
    )
    class Meta:
        model = Recipe
        fields = ('id','title','ingredients','tags','time_minutes','price','link')
        read_only = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    #serialize the recipe details
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags        = TagSerializer(many=True,read_only=True)

