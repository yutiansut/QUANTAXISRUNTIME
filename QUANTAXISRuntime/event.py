#coding:utf-8

import datetime
from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import (ALL_COMPLETED, FIRST_COMPLETED,
                                FIRST_EXCEPTION, Future, as_completed, wait)


class EventCenter:
    def __init__(self, *args, **kwargs):
        