"""Sneaker Model."""

from masoniteorm.models import Model


class Sneaker(Model):
    __table__="sneakers"