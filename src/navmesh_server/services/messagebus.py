# pylint: disable=missing-function-docstring,missing-class-docstring
from typing import Callable, Dict, List, Type, Any


class MessageBus:
    def __init__(self):
        self.event_handlers: Dict[Type, List[Callable]] = {}
        self.command_handlers: Dict[Type, Callable] = {}

    def register_event_handler(self, event_type: Type, handler: Callable):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def register_command_handler(self, command_type: Type, handler: Callable):
        self.command_handlers[command_type] = handler

    async def publish_event(self, event):
        event_type = type(event)
        if event_type in self.event_handlers:
            for handler in self.event_handlers[event_type]:
                await handler(event)

    async def execute_command(self, command) -> Any:
        command_type = type(command)
        if command_type in self.command_handlers:
            return await self.command_handlers[command_type](command)
        raise ValueError(f"No handler registered for command type: {command_type}")
