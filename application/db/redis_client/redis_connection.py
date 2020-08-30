import redis
from .redis_client_config import client_config

redis_client = redis.Redis(
    host = client_config["HOST"], 
    port = client_config["PORT"], 
    db = client_config["DB"]
)