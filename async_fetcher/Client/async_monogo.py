# coding=utf-8

import asyncio
import motor
import pymongo
from motor import motor_asyncio
from motor.motor_asyncio import (AsyncIOMotorCollection, AsyncIOMotorClient, AsyncIOMotorDatabase,
                                 AsyncIOMotorCommandCursor)


def database(ip='127.0.0.1', port=27017):
    return AsyncIOMotorClient(ip, port)


