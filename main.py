import datetime
import os
import time

import psutil
import psutil._exceptions as ps_exceptions
from discoIPC import ipc


def main():
    # generated by 'map list generator.py'
    map_gamemodes = {'ctf_2fort': ('ctf', 'Capture the Flag'), 'ctf_2fort_invasion': ('ctf', 'Capture the Flag'), 'ctf_doublecross': ('ctf', 'Capture the Flag'), 'ctf_landfall': ('ctf', 'Capture the Flag'), 'ctf_sawmill': ('ctf', 'Capture the Flag'), 'ctf_turbine': ('ctf', 'Capture the Flag'), 'ctf_well': ('ctf', 'Capture the Flag'), 'cp_5gorge': ('control-point', 'Control Point'), 'cp_badlands': ('control-point', 'Control Point'), 'cp_coldfront': ('control-point', 'Control Point'), 'cp_fastlane': ('control-point', 'Control Point'), 'cp_foundry': ('control-point', 'Control Point'), 'cp_freight_final1': ('control-point', 'Control Point'), 'cp_granary': ('control-point', 'Control Point'), 'cp_gullywash_final1': ('control-point', 'Control Point'), 'cp_metalworks': ('control-point', 'Control Point'), 'cp_powerhouse': ('control-point', 'Control Point'), 'cp_process_final': ('control-point', 'Control Point'), 'cp_sunshine_event': ('control-point', 'Control Point'), 'cp_snakewater_final1': ('control-point', 'Control Point'), 'cp_sunshine': ('control-point', 'Control Point'), 'cp_vanguard': ('control-point', 'Control Point'), 'cp_well': ('control-point', 'Control Point'), 'cp_yukon_final': ('control-point', 'Control Point'), 'cp_dustbowl': ('attack-defend', 'Attack/Defend'), 'cp_egypt_final': ('attack-defend', 'Attack/Defend'), 'cp_gorge': ('attack-defend', 'Attack/Defend'), 'cp_gorge_event': ('attack-defend', 'Attack/Defend'), 'cp_gravelpit': ('attack-defend', 'Attack/Defend'), 'cp_junction_final': ('attack-defend', 'Attack/Defend'), 'cp_manor_event': ('attack-defend', 'Attack/Defend'), 'cp_mercenarypark': ('attack-defend', 'Attack/Defend'), 'cp_mossrock': ('attack-defend', 'Attack/Defend'), 'cp_mountainlab': ('attack-defend', 'Attack/Defend'), 'cp_snowplow': ('attack-defend', 'Attack/Defend'), 'cp_steel': ('attack-defend', 'Attack/Defend'), 'tc_hydro': ('territorial-control', 'Territorial Control'), 'pl_badwater': ('payload', 'Payload'), 'pl_barnblitz': ('payload', 'Payload'), 'pl_borneo': ('payload', 'Payload'), 'pl_fifthcurve_event': ('payload', 'Payload'), 'pl_cactuscanyon ': ('payload', 'Payload'), 'pl_enclosure_final': ('payload', 'Payload'), 'pl_frontier_final': ('payload', 'Payload'), 'pl_goldrush': ('payload', 'Payload'), 'pl_millstone_event': ('payload', 'Payload'), 'pl_hoodoo_final': ('payload', 'Payload'), 'pl_snowycoast': ('payload', 'Payload'), 'pl_swiftwater_final1': ('payload', 'Payload'), 'pl_thundermountain': ('payload', 'Payload'), 'pl_upward': ('payload', 'Payload'), 'plr_bananabay': ('payload-race', 'Payload Race'), 'plr_hightower_event': ('payload-race', 'Payload Race'), 'plr_hightower': ('payload-race', 'Payload Race'), 'plr_nightfall_final': ('payload-race', 'Payload Race'), 'plr_pipeline': ('payload-race', 'Payload Race'), 'koth_badlands': ('koth', 'King of the Hill'), 'koth_brazil': ('koth', 'King of the Hill'), 'koth_viaduct_event': ('koth', 'King of the Hill'), 'koth_lakeside_event': ('koth', 'King of the Hill'), 'koth_harvest_final': ('koth', 'King of the Hill'), 'koth_harvest_event': ('koth', 'King of the Hill'), 'koth_highpass': ('koth', 'King of the Hill'), 'koth_king': ('koth', 'King of the Hill'), 'koth_lakeside_final': ('koth', 'King of the Hill'), 'koth_lazarus': ('koth', 'King of the Hill'), 'koth_maple_ridge_event': ('koth', 'King of the Hill'), 'koth_moonshine_event': ('koth', 'King of the Hill'), 'koth_nucleus': ('koth', 'King of the Hill'), 'koth_probed': ('koth', 'King of the Hill'), 'koth_sawmill': ('koth', 'King of the Hill'), 'koth_suijin': ('koth', 'King of the Hill'), 'koth_viaduct': ('koth', 'King of the Hill'), 'sd_doomsday_event': ('special-delivery', 'Special Delivery'), 'sd_doomsday': ('special-delivery', 'Special Delivery'), 'mvm_bigrock': ('mvm', 'Mann vs. Machine'), 'mvm_coaltown': ('mvm', 'Mann vs. Machine'), 'mvm_decoy': ('mvm', 'Mann vs. Machine'), 'mvm_example': ('mvm', 'Mann vs. Machine'), 'mvm_ghost_town': ('mvm', 'Mann vs. Machine'), 'mvm_mannhattan': ('mvm', 'Mann vs. Machine'), 'mvm_mannworks': ('mvm', 'Mann vs. Machine'), 'mvm_rottenburg': ('mvm', 'Mann vs. Machine'), 'rd_asteroid': ('beta-map', 'Robot Destruction'), 'ctf_foundry': ('mannpower', 'Mannpower'), 'ctf_gorge': ('mannpower', 'Mannpower'), 'ctf_hellfire': ('mannpower', 'Mannpower'), 'ctf_thundermountain': ('mannpower', 'Mannpower'), 'pass_brickyard': ('passtime', 'PASS Time'), 'pass_district': ('passtime', 'PASS Time'), 'pass_timbertown': ('passtime', 'PASS Time'), 'pd_pit_of_death_event': ('player-destruction', 'Player Destruction'), 'pd_watergate': ('player-destruction', 'Player Destruction')}
    start_time = int(time.time())
    activity = {'details': 'In menus',  # this is what gets modified and sent to Discord via discoIPC
                'timestamps': {'start': start_time},
                'assets': {'small_image': 'tf2_icon_small', 'small_text': 'Team Fortress 2', 'large_image': 'main_menu', 'large_text': 'In menus'},
                'state': ''}
    client_connected = False

    while True:
        tf2_is_running = False
        steam_is_running = False

        # looks through all running processes to determine if tf2 is running and to find the paths of tf2 and steam
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)

                if p.name() == "hl2.exe" and 'Team Fortress 2' in p.cmdline()[0]:
                    tf2_location = p.cmdline()[0][:-7]
                    tf2_is_running = True

                if p.name() == "Steam.exe":
                    steam_location = p.cmdline()[0][:-9]
                    steam_is_running = True
            except ps_exceptions.NoSuchProcess:
                pass
            except ps_exceptions.AccessDenied:
                pass

        if steam_is_running:
            # reads a steam config file
            config_files('settings', steam_location)

        # used for display only
        current_time = datetime.datetime.now()
        current_time_formatted = current_time.strftime('%#I:%#M:%S %p')

        if tf2_is_running:
            if not client_connected:
                # connects to Discord
                client = ipc.DiscordIPC('429389143756374017')
                client.connect()

                # sends first status, starts on main menu
                start_time = int(time.time())
                activity['timestamps']['start'] = start_time
                client.update_activity(activity)
                client_connected = True

            # defaults
            current_map = ''
            current_class = ''
            party_state = 'Not in a party'

            # modifies a few tf2 config files
            config_files('classes', tf2_location)

            # console.log is a log of tf2's console (duh), only exists if tf2 has -condebug (see the bottom of config_files)
            consolelog_filename = '{}tf\\console.log'.format(tf2_location)
            with open(consolelog_filename, 'r', errors='replace') as consolelog_file:
                line = consolelog_file.readline()

                # iterates though every line in the log (I KNOW) and learns everything from it
                while line != '':
                    if '[PartyClient] Joining party ' in line and not line.endswith('0\n'):
                        party_state = 'In a party'

                    if 'Map: ' in line:
                        current_map = line[5:-1]
                        current_class = 'unselected'  # this variable is poorly named
                        party_state = 'Not in a party'

                    if ' selected' in line:
                        current_class = line[:-11]

                    if 'Lobby destroyed' in line or 'Steam config directory:' in line or 'Dropped ' in line:
                        current_map = 'In menus'  # so is this one
                        current_class = 'unselected'

                    if '[PartyClient] Entering queue' in line:
                        current_map = 'In queue'
                        current_class = 'unselected'

                    line = consolelog_file.readline()

            if current_map != 'In menus' and current_map != 'In queue':
                # not in menus = in a game
                try:
                    current_gamemode, gamemode_fancy = map_gamemodes[current_map]
                    activity['assets']['large_image'] = current_gamemode
                    activity['assets']['large_text'] = gamemode_fancy
                except KeyError:
                    activity['assets']['large_image'] = 'unknown_map'

                activity['details'] = 'Map: {}'.format(current_map)
                activity['state'] = 'Class: {}'.format(current_class)
            else:
                # in menus displays the main menu
                activity['details'] = current_map
                activity['state'] = party_state
                activity['assets']['large_image'] = 'main_menu'
                activity['assets']['large_text'] = 'Main menu'

            # output to terminal, just for monitoring
            print(current_time_formatted)
            print("{} ({})".format(activity['details'], activity['assets']['large_text']))
            print(activity['state'])
            time_elapsed = time.time() - start_time
            print("{:02}:{:02} elapsed".format(int(time_elapsed / 60), round(time_elapsed % 60)))
            print()

            # send everything to discord
            client.update_activity(activity)
        else:
            if client_connected:
                try:
                    client.disconnect()  # doesn't work...
                except:
                    pass

                print('{}: TF2 closed, exiting'.format(current_time_formatted))
                raise SystemExit  # ...but this does
            else:
                print("{}: Not running TF2".format(current_time_formatted))

            # to prevent connecting when already connected
            client_connected = False

        # rich presence only updates every 15 seconds, but it listens constantly so sending every 5 seconds is fine
        time.sleep(5)


def config_files(mode, exe_location):
    if mode == 'classes':  # allows the console to output 'class selected' on class choose
        tf2_classes = ['Scout', 'Soldier', 'Pyro', 'Demoman', 'Heavy', 'Engineer', 'Medic', 'Sniper', 'Spy']

        for tf2_class in tf2_classes:
            # 'echo' means 'output to console' in source-speak
            selected_line = 'echo "{} selected"'.format(tf2_class)

            config_filename = tf2_class.lower().replace('heavy', 'heavyweapons')  # valve why

            # config files are at 'Steam\steamapps\common\Team Fortress 2\tf\cfg'
            try:
                # reads each existing class.cfg
                class_config_file = open('{}tf\\cfg\\{}.cfg'.format(exe_location, config_filename), 'r+', errors='replace')
                if selected_line not in class_config_file.read():
                    # if it doesn't already have the echo line, add it
                    class_config_file.write('\n\n' + selected_line)
            except FileNotFoundError:
                # the config file doesn't exist, so create it and add the echo line
                class_config_file = open('{}tf\\cfg\\{}.cfg'.format(exe_location, config_filename), 'w')
                class_config_file.write('\n\n' + selected_line)

            # I know a 'with open()' is better but eh
            class_config_file.close()
    elif mode == 'settings':  # reads steams launch options save file to find -condebug
        found_condebug = False

        for user_id_folder in next(os.walk(exe_location + 'userdata'))[1]:  # possibly multiple users for the same steam install
            try:
                # 'C:\Program Files (x86)\Steam\userdata\*user id number*\config\localconfig.vdf'
                with open('{}userdata\\{}\\config\\localconfig.vdf'.format(exe_location, user_id_folder), 'r+', errors='replace') as global_config_file:
                    lines = global_config_file.readlines()
                    tf2_line_num = 0

                    for line in enumerate(lines):
                        if line[1] == '\t\t\t\t\t"440"\n':  # looks for the tf2's number and finds the line number
                            tf2_line_num = line[0]

                    launchoptions_line = lines[tf2_line_num + 14]  # the launch options line should be the 14th line in the tf2 options, might not be though
                    if '-condebug' in launchoptions_line:
                        # oh also this might be slow to update
                        found_condebug = True
            except FileNotFoundError:
                pass

        if not found_condebug:
            # yell at the user to fix their settings
            print('Your TF2 installation doesn\'t seem to be set up properly. To fix:'
                  '\n1. Right click on Team Fortress 2 in your Steam library'
                  '\n2. Open properties (very bottom)'
                  '\n3. Click "Set launch options..."'
                  '\n4. Add -condebug'
                  '\n5. OK and Close\n')
            # -condebug is kinda necessary so just exit if it's not there
            raise SystemExit


if __name__ == '__main__':
    main()
