import uuid

import pytest
from pytest_django.asserts import assertRaisesMessage
from django.db import connection

from core.abstract_models import TimeStampedModel
from core.helpers import is_recent


def test_TimeStampedModel_is_abstract():
    """Test that trying to instantiate abstract model raises exception"""
    with pytest.raises(TypeError):
        assert TimeStampedModel()


@pytest.mark.django_db
def test_TimeStampedModel_fields():
    # Override model to make it not abstract
    class TimeStampModelOverridden(TimeStampedModel):
        class Meta:
            abstract = False

    # Add model to DB schema dynamically
    with connection.schema_editor() as editor:
        editor.create_model(TimeStampModelOverridden)

    m = TimeStampModelOverridden()
    m.save()
    m.refresh_from_db()
    assert isinstance(m.pk, uuid.UUID)
    assert is_recent(m.created_on)
    assert is_recent(m.updated_on)

    inital_update_datetime = m.updated_on
    m.save()
    m.refresh_from_db()
    assert inital_update_datetime != m.updated_on
