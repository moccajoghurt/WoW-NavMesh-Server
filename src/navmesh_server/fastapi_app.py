from pydantic import BaseModel
from fastapi import APIRouter, Depends, FastAPI, Header
from fastapi import HTTPException
from navmesh_server import bootstrap
from navmesh_server.domain import commands

API_KEY = "bb44363a-2a05-4c49-bed3-DEV-ONLY-28913930e6ee"


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")


app = FastAPI()
bus = bootstrap.bootstrap()

router = APIRouter()


class PathRequest(BaseModel):
    map_id: int
    start_x: float
    start_y: float
    start_z: float
    end_x: float
    end_y: float
    end_z: float


@app.post("/fetch-route", dependencies=[Depends(verify_api_key)])
async def fetch_route(model: PathRequest):
    cmd = commands.GenerateWaypoints(
        map_id=model.map_id,
        start_x=model.start_x,
        start_y=model.start_y,
        start_z=model.start_z,
        end_x=model.end_x,
        end_y=model.end_y,
        end_z=model.end_z,
    )
    waypoints = await bus.execute_command(cmd)
    return {"Waypoints": waypoints}
