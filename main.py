from utils import get_data
from utils import message
from utils.enum import ColumnName

message.system.start()

program = True

stock_df = get_data.table()

if stock_df.empty:
    program = False
    print('A tabela está vazia.\n')

while program:
    action = message.system.choice_crud()
    match action:

        # Read
        case 1:
            read_action = message.read.options()
            match read_action:
                
                # Full table
                case 1:
                    message.read.full_table(stock_df)

                # Product
                case 2:
                    message.read.specific_rows(stock_df, ColumnName.ITEM.value)

                # Category
                case 3:
                    message.read.specific_rows(stock_df, ColumnName.CATEGORY.value)

                # Price
                case 4:
                    message.read.specific_rows(stock_df, ColumnName.PRICE.value)

                # Quantity
                case 5:
                    message.read.specific_rows(stock_df, ColumnName.QUANTITY.value)

                # More
                case 6:
                    print('More\n')

                # Back
                case 7:
                    print('Voltando...\n')

        # Create
        case 2:
            message.create.row(stock_df)

        # Update
        case 3:
            print('Update\n')

        # Delete
        case 4:
            delete_action = message.delete.options()
            match delete_action:

                # Product
                case 1:
                    stock_df = message.delete.by_item(stock_df)

                # Category
                case 2:
                    stock_df = message.delete.by_category(stock_df)

                # Price
                case 3:
                    stock_df = message.delete.by_price(stock_df)

                # Quantity
                case 4:
                    print('Quantity\n')

                # More
                case 5:
                    print('More\n')

                # Back
                case 6:
                    print('Voltando...\n')

        # Leave
        case 5:
            break

message.system.save_modifications(stock_df)
message.system.close()
