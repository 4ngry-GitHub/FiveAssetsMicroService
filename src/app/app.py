from fastapi import FastAPI, Body, HTTPException, status

from database.crud import write_data_in_db
from pydanticmodels.signalmodel import SignalModel

app = FastAPI()


@app.post(
    '/post-asset',
    tags=['Assets'],
    description='Post asset in database',
    status_code=201
)
async def post_asset(asset_data: SignalModel = Body(...)) -> dict:
    response_result: bool = write_data_in_db(asset_data)
    if response_result:
        return {"Result": "Success"}
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail='Error! You did something wrong.')