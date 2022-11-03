from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime

from database.base import Base, engine


class AssetDBModel(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    asset_name = Column(String, nullable=False)
    
    def __init__(self, asset_name):
        self.asset_name = asset_name
    
    def __repr__(self) -> str:
        return f"asset_name={self.asset_name}"
    
    
class SignalDBModel(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey(AssetDBModel.id), nullable=False)
    signal = Column(Integer, nullable=False)
    close = Column(Numeric, nullable=False)
    open = Column(Numeric, nullable=False)
    high = Column(Numeric, nullable=False)
    low = Column(Numeric, nullable=False)
    time = Column(DateTime, nullable=False)
    timenow = Column(DateTime, nullable=False)
    interval = Column(Integer, nullable=False)
    plot_0 = Column(Numeric, nullable=True)
    plot_1 = Column(Numeric, nullable=True)
    plot_2 = Column(Numeric, nullable=True)
    plot_3 = Column(Numeric, nullable=True)
    plot_4 = Column(Numeric, nullable=True)
    plot_5 = Column(Numeric, nullable=True)
    plot_6 = Column(Numeric, nullable=True)
    plot_7 = Column(Numeric, nullable=True)
    plot_8 = Column(Numeric, nullable=True)
    plot_9 = Column(Numeric, nullable=True)
    plot_10 = Column(Numeric, nullable=True)
    plot_11 = Column(Numeric, nullable=True)
    plot_12 = Column(Numeric, nullable=True)
    plot_13 = Column(Numeric, nullable=True)
    plot_14 = Column(Numeric, nullable=True)
    plot_15 = Column(Numeric, nullable=True)
    plot_16 = Column(Numeric, nullable=True)
    plot_17 = Column(Numeric, nullable=True)
    plot_18 = Column(Numeric, nullable=True)
    plot_19 = Column(Numeric, nullable=True)


Base.metadata.create_all(engine)