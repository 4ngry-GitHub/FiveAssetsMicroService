from database.base import get_session
from models.dbmodel import AssetDBModel


def create_model(*, data):
    session = next(get_session())
    model = AssetDBModel(**data)
    session.add(model)
    session.commit()
