# pylint: disable=missing-function-docstring, missing-module-docstring
from typing import List
from navmesh_server.adapters.detour import path_generation
from navmesh_server.domain import commands


async def calculate_path(
    command: commands.GenerateWaypoints,
    waypoint_generator: path_generation.AbstractPathGeneration,
) -> List[List[float]]:
    waypoints = waypoint_generator.calculate_path_2d(
        command.map_id,
        [command.start_x, command.start_y, command.start_z],
        [command.end_x, command.end_y, command.end_z],
    )
    return waypoints
