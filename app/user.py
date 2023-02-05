from dataclasses import dataclass

@dataclass
class User:
    """
    CREATE TABLE IF NOT EXISTS user_logins(
    user_id             varchar(128),
    device_type         varchar(32),
    masked_ip           varchar(256),
    masked_device_id    varchar(256),
    locale              varchar(32),
    app_version         integer,

);
    """
    user_id: str
    device_type: str
    masked_ip: str
    masked_device_id: str
    locale: str
    app_version: str
