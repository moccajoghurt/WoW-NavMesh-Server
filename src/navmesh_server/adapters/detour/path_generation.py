# pylint: disable=missing-function-docstring, missing-module-docstring, missing-class-docstring
import abc
import os
import ctypes
from typing import List


class AbstractPathGeneration(abc.ABC):
    @abc.abstractmethod
    def calculate_path_2d(
        self, map_id: int, start: List[float], end: List[float]
    ) -> List[List[float]]:
        pass


class PathGeneration(AbstractPathGeneration):
    def __init__(self):
        nav_dll = ctypes.CDLL(self._get_navigation_lib_path())
        nav_dll.InitializeNavigation()

    def calculate_path_2d(self, map_id: int, start: List[float], end: List[float]):
        nav_dll = ctypes.CDLL(self._get_navigation_lib_path())
        func = nav_dll.CalculatePath
        func.argtypes = [
            ctypes.c_uint,
            XYZ,
            XYZ,
            ctypes.c_bool,
            ctypes.POINTER(ctypes.c_int),
        ]
        func.restype = ctypes.POINTER(XYZ)

        length = ctypes.c_int(0)
        start_xyz = XYZ(x=start[0], y=start[1], z=start[2])
        end_xyz = XYZ(x=end[0], y=end[1], z=end[2])
        results = func(map_id, start_xyz, end_xyz, False, ctypes.byref(length))
        points = []
        for i in range(length.value):
            p = results[i]
            points.append([round(p.x, 2), round(p.y, 2)])
        nav_dll.FreePathArr.restype = None
        nav_dll.FreePathArr.argtypes = [ctypes.POINTER(XYZ)]
        nav_dll.FreePathArr(results)
        return points

    def _get_navigation_lib_path(self):
        this_file_path = os.path.abspath(__file__)
        directory = os.path.dirname(this_file_path)
        return os.path.join(directory, "navigation.so")


class XYZ(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float), ("z", ctypes.c_float)]
