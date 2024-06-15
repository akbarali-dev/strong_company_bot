from typing import Union

import asyncpg

from asyncpg.pool import Pool
from asyncpg import Connection
from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
            port=5432
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def select_user_info(self, **kwargs):
        sql = """
        select *
        from bot_api_botuser
        where
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_FILES(self, **kwargs):
        sql = """
        select * from bot_api_file
        where 
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_questions(self, **kwargs):
        sql = """
        select question
        from bot_api_answerquestions
        where 
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_answer(self, **kwargs):
        sql = """
        select answer
        from bot_api_answerquestions
        where 
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_file(self, **kwargs):
        sql = """
        select file_link
        from bot_api_file
        where
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_contacts(self, **kwargs):
        sql = """
        select name, link
        from bot_api_contact
        where
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_portfolio(self, **kwargs):
        sql = """
        select id, title
        from bot_api_portfolio
        where
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetch=True)

    async def select_portfolio_by_id(self, **kwargs):
        sql = """
        select id, title, description, link
        from bot_api_portfolio
        where
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)



