from sqlalchemy.exc import IntegrityError

from database.base import get_session
from models.dbmodel import AssetDBModel, SignalDBModel
from pydanticmodels.signalmodel import SignalModel

session = next(get_session())


def write_data_in_db(data: SignalModel) -> bool:
    ticker = get_or_create_ticker_from_db(data.asset_name)
    signal = SignalDBModel(**data.dict(exclude={'asset_name'}))
    signal.asset_id = ticker.id
    session.add(signal)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


def get_or_create_ticker_from_db(ticker_name):
    ticker = session.query(AssetDBModel).filter(AssetDBModel.asset_name == ticker_name).one_or_none()
    if not ticker:
        ticker = AssetDBModel(ticker_name)
        session.add(ticker)
        session.flush((ticker, ))
    return ticker
