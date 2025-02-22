from utils import get_data
from utils import message

message.start()

stock_df = get_data.table()

while True:
    action = message.choice_crud()
    match action:

        # Read
        case 1:
            read_action = message.read()
            match read_action:
                
                # Full table
                case 1:
                    message.read_table(stock_df)

                # Product
                case 2:
                    message.read_product(stock_df)

                # Category
                case 3:
                    print('Category\n')

                # Price
                case 4:
                    print('Price\n')

                # Quantity
                case 5:
                    print('Quantity\n')

                # More
                case 6:
                    print('More\n')

                # Back
                case 7:
                    print('\n')
        # Create
        case 2:
            print('Create\n')
        
        # Update
        case 3:
            print('Update\n')
        
        # Delete
        case 4:
            print('Delete\n')
        
        # Leave
        case 5:
            input('Digite ENTER para finalizar o programa...')
            break
