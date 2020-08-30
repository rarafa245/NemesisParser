from .redis_client import redis_client

def redis_insert_localization(tag_id: int, message: str, expire_time=1800) -> bool:
    ''' insert json string in Redis DB
        :parram - tag_id: Identification of the Tag
                - message: json string
                - expire_time: seconds to message to expire (default 1800 - 30 min)
        :return - Boolean with the sucess/faluir of the process
    '''

    key = 'tags:{}'.format(tag_id)
    insert = redis_client.set(key, message, ex=expire_time)

    return insert