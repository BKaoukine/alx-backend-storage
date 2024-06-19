#!/usr/bin/env python3
"""Cach Class."""

import redis
from typing import AnyStr
import uuid


class Cache:
    """Cache class to store data in a Redis database."""

    def __init__(self) -> None:
        """Initialize the Cache with a Redis.
        
        connection and flush the database.
        """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: AnyStr) -> str:
        """
        Store data in the Redis database.

        Args:
            data (AnyStr): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        datainput = str(data)
        self.__redis.set(key, datainput)
        return key