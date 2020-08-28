import sql_draft_functions as sdf


def main():
    if sdf.are_we_drafting():
        conn = sdf.create_connection('draft_data.db')
        draft_loop = True

        while draft_loop:
            # if not my turn handle others else handle my pick
            if not sdf.player_turn():
                # get team name of drafter and position to be selected
                picked_by = input('What team is drafting a player?')
                position_table = sdf.position_to_draft()
                if position_table == 'DEF':
                    # get name of defense by City Name (All caps abbreviation)
                    defense = sdf.name_of_defense()
                    sdf.flag_def_as_picked(conn, position_table, defense, picked_by)
                else:
                    # get name of player in LastName format
                    player_last_name = sdf.nfl_player_name()
                    sdf.flag_as_picked(conn, position_table, player_last_name, picked_by)
            else:
                position_table = sdf.position_to_draft()
                sdf.auto_flag(conn, position_table, 'xXxDraftBot69420xXx')

            draft_loop = sdf.are_we_drafting()

        conn.close()

    else:
        print('Thanks for drafting with DraftBot9000.')


if __name__ == '__main__':
    main()
