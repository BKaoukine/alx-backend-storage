#!/usr/bin/env python3
"""Exercise.py."""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorate a method to count the number of calls.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call count and call the original method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorate a method to store the history of inputs and outputs.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    inputs = method.__qualname__ + ':inputs'
    outputs = method.__qualname__ + ':outputs'

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store input and output history and call the original method."""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    Display the call history of a method.

    Args:
        method (Callable): The method whose history is to be displayed.
    """
    inputs = f'{method.__qualname__}:inputs'
    outputs = f'{method.__qualname__}:outputs'

    in_el = method.__self__._redis.lrange(inputs, 0, -1)
    out_el = method.__self__._redis.lrange(outputs, 0, -1)

    print("{} was called {} times:".format(method.__qualname__, len(in_el)))
    for i, o in zip(in_el, out_el):
        print(
            f"{method.__qualname__}\
                (*{i.decode('utf-8')}) \
                    -> {o.decode('utf-8')}"
            )


class Cache:
    """Cache class to store data in a Redis database."""

    def __init__(self) -> None:
        """Initialize the Cache with a Redis connection.

        and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis database.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from the Redis database.

        Args:
            key: The key under which the data is stored.
            fn: Optional function to apply to the data.

        Returns:
            Union[str, bytes, int, float]: The retrieved data.
        """
        if fn is None:
            return self._redis.get(key)
        return fn(self._redis.get(key))

    def get_str(self, key) -> str:
        """
        Retrieve data as a string from the Redis database.

        Args:
            key: The key under which the data is stored.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(key, str)

    def get_int(self, key) -> int:
        """
        Retrieve data as an integer from the Redis database.

        Args:
            key: The key under which the data is stored.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(key, int)
