RANDOM_SEED = 42
NEW_CUSTOMERS = 80             # Total number of customers
INTERVAL_CUSTOMERS = 3.0        # Generate new customers roughly every x seconds
MIN_PATIENCE = 1                # Min. gen_customer patience
MAX_PATIENCE = 5                # Max. gen_customer patience
CAPACITY = 2                    # The capacity of our resource  2 bank tellers
TIME_IN_BANK = 10.0             # The max time an operation can take
REPORT_STEP_BY_STEP = False     # Flag to report step by step events
REPORT_QUEUE = True            # Flag to report step by step the state of the queue
CREATE_SIM_GRAPHS = False        # Flag to create the graphs of the collected data

#With more data we can describe more things
#Identify or learn the reason why they dont have more people to work for you
#porque es mejor no tener tantos empleados para que la empresa se beneficie
#Si la seed es la misma todos tendremos el mismo resultado
