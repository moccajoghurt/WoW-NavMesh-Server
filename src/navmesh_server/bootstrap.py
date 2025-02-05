# pylint: disable=missing-function-docstring,unnecessary-lambda
import inspect
from navmesh_server.adapters.detour import path_generation
from navmesh_server.services import messagebus
from navmesh_server.domain import commands
from navmesh_server.usecases import (
    waypoint_generation,
)


def bootstrap(
    waypoint_generator: path_generation.AbstractPathGeneration = path_generation.PathGeneration(),
) -> messagebus.MessageBus:
    bus = messagebus.MessageBus()
    dependencies = {
        "waypoint_generator": waypoint_generator,
    }
    injected_command_handlers = {
        commands.GenerateWaypoints: inject_dependencies(
            waypoint_generation.calculate_path, dependencies
        ),
    }

    for command_type, command_handler in injected_command_handlers.items():
        bus.register_command_handler(command_type, command_handler)
    return bus


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda command: handler(command, **deps)
