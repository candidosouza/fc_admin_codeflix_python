
from typing import TYPE_CHECKING
from core.__seedwork.domain.exceptions import EntityValidationException, LoadEntityException
from core.__seedwork.domain.value_objects import UniqueEntityId
from core.category.domain.entities import Category

if TYPE_CHECKING:
    from core.category.infra.django_app.models import CategoryModel


class CategoryModelMapper:
    @staticmethod
    def to_entity(model: 'CategoryModel') -> Category:
        try:
            return Category(
                unique_entity_id=UniqueEntityId(str(model.id)),
                name=model.name,
                description=model.description,
                is_active=model.is_active,
                created_at=model.created_at,
            )
        except EntityValidationException as exception:
            raise LoadEntityException(exception.error) from exception

    @staticmethod
    def to_model(category: Category) -> 'CategoryModel':
        from core.category.infra.django_app.models import CategoryModel # pylint: disable=import-outside-toplevel
        return CategoryModel(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
            created_at=category.created_at
        )
