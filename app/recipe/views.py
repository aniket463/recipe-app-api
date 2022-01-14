from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



from core.models import Tag,Ingredient,Recipe
from recipe import serializers


class BaseRecipeArrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):
    #Base viewset for user own recipe attributes
    authentication_classes = (TokenAuthentication,)
    permission_classes   =   (IsAuthenticated,)

    def get_queryset(self):
        #Return object for current authenticated user only
        return self.queryset.filter(user=self.request.user).order_by('-name')
    def perform_create(self, serializer):
        #Create a new tag
        serializer.save(user=self.request.user)

class TagViewSet(BaseRecipeArrViewSet):
    #Manage tag in the database
    queryset             =   Tag.objects.all()
    serializer_class     =   serializers.TagSerializer

class IngredientViewSet(BaseRecipeArrViewSet):
    #Manage Ingredient in the database
    queryset             =   Ingredient.objects.all()
    serializer_class     =   serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class     =   serializers.RecipeSerializer
    queryset             =   Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes   =   (IsAuthenticated,)

    def get_queryset(self):
        #Return object for current authenticated user only
        return self.queryset.filter(user=self.request.user)
