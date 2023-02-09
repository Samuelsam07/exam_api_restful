from config import db
import enum
from SQLAlchemy import Enum 

class OrederStatus(enum.Enum):

CREATE = 0
SHIPPING = 1
DELIVERED = 2
PAID = 3

t = Table (
    'data',MetaData(),
    Column('value',Enum(OrederStatus))
)
