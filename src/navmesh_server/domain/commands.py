# pylint: disable=missing-class-docstring, too-few-public-methods
from dataclasses import dataclass


class Command:
    pass


@dataclass
class GenerateWaypoints:
    map_id: int
    start_x: float
    start_y: float
    start_z: float
    end_x: float
    end_y: float
    end_z: float
