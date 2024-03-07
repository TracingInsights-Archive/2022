import fastf1
import os
import json
import utils

YEAR = 2022


events = [
    # 'Pre-Season Test', 

'Bahrain Grand Prix', 'Saudi Arabian Grand Prix', 
     'Australian Grand Prix', 'Emilia Romagna Grand Prix', 'Miami Grand Prix',
    'Spanish Grand Prix', 'Monaco Grand Prix', 'Azerbaijan Grand Prix',
    'Canadian Grand Prix', 'British Grand Prix', 'Austrian Grand Prix',
    'French Grand Prix', 'Hungarian Grand Prix', 'Belgian Grand Prix', 
    'Dutch Grand Prix', 'Italian Grand Prix', 'Singapore Grand Prix', 
    'Japanese Grand Prix', 'United States Grand Prix', 'Mexico City Grand Prix', 
    'São Paulo Grand Prix', 'Abu Dhabi Grand Prix'
]
# sessions = [
#     "Practice 1",
#       "Practice 2",
#       "Practice 3",
#       # "Qualifying",
#       # "Race",
# ]

def sessions_available(year: int, event: str | int) -> any:
    # get sessions available for a given year and event
    event = str(event)
    data = utils.LatestData(year)
    sessions = data.get_sessions(event)
    return sessions

for event in events:
    sessions = sessions_available(YEAR, event)
    for session in sessions:
        f1session = fastf1.get_session(YEAR, event, session)
        f1session.load()
        circuit_info = f1session.get_circuit_info().corners
        corner_info ={
            "CornerNumber": circuit_info['Number'].tolist(),
            "X": circuit_info['X'].tolist(),
            "Y": circuit_info['Y'].tolist(),
            "Angle": circuit_info['Angle'].tolist(),
            "Distance": circuit_info['Distance'].tolist(),
        }

        driver_folder = f"{event}/{session}"
        file_path = f"{event}/{session}/corners.json"
        if not os.path.exists(driver_folder):
            os.makedirs(driver_folder)
        # Save the dictionary to a JSON file
        with open(file_path, "w") as json_file:
            json.dump(corner_info, json_file)
