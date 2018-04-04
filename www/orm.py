#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

__author__ = 'Micheal'

import asyncio, logging

import  aiomysql

def log(sql, args=()):
    logging.ingo('SQL: %s' % sql)

async def create_pool(loop, **kw):
    logging.info('creat datebase connection pool...')
    globals __pool
    __pool =await aiomysql.creat_pool(
        host=
    )