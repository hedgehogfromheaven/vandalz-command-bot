# handlers/__init__.py

from aiogram import Dispatcher
from .basic import register_basic_handlers


def setup_handlers(dp: Dispatcher):
    register_basic_handlers(dp)