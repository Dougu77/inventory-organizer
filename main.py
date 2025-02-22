from utils import get_data
from utils import message

message.start()

stock_df = get_data.table()

action = message.choice_crud()

match action:
    case 1:
        print('Read')
    case 2:
        print('Create')
    case 3:
        print('Update')
    case 4:
        print('Delete')
    case 5:
        print('Leave')
