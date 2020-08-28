import sqlite3 as sq


# Takes sqlite3 database file as input and returns a connection to DB
def create_connection(db_file):
    conn = None
    try:
        conn = sq.connect(db_file)
    except ConnectionRefusedError as e:
        print(e)

    return conn


# INPUTS: DB connection, name of position table, Name of team who picket player
# No return
def flag_as_picked(conn, position_table, player_last_name, picked_by):
    # create cursor to execute sql commands on DB
    c = conn.cursor()
    c.execute('UPDATE {} SET Selected = ? WHERE LastName = ?'.format(position_table), (picked_by, player_last_name))
    conn.commit()


# Nearly identical function for Defense, different Column indexes for this table in sql database
# Thought it would be cleaner to make two separate functions
def flag_def_as_picked(conn, position_table, defense, picked_by):
    c = conn.cursor()
    c.execute('UPDATE {} SET Selected = ? WHERE State_Name = ?'.format(position_table), (picked_by, defense))
    conn.commit()


# Auto draft picks for yours truly, this sql command + subquery works for players and defense
def auto_flag(conn, position_table, picked_by):
    c = conn.cursor()
    c.execute('UPDATE {} SET Selected = ? '
              'WHERE Rank = (SELECT min(Rank) FROM {} '
              'WHERE Selected IS NULL)'.format(position_table, position_table), (picked_by,))
    conn.commit()


# start draft and game loop control
def are_we_drafting() -> bool:
    answer = input('Do you wish to start the draft or continue drafting? Please answer yes or no.')
    return True if answer == 'yes' else False


# Input string from player mine == True any other == false
def player_turn() -> bool:
    answer = input('Is it your turn or someone else? Please respond with mine or other.'
                   'Note this is case sensitive.')
    return True if answer == 'mine' else False


def position_to_draft() -> str:
    return input('What position do you want to draft? Please select either of these options'
                 'QB, RB, WR, TE, K or DEF please note that this is case sensitive.')


def nfl_player_name() -> str:
    return input('Please enter the player last name with first'
                 ' letter capitalized or McCafferey etc.')


def name_of_defense() -> str:
    return input('In this format please enter your defense, San Francisco (SF).')
