import datajoint as dj

schema = dj.schema('shan_calcium')

@schema
class Mouse(dj.Manual):
    definition = """
    # Experimental animals
    mouse_id             : int                          # Unique animal ID
    ---
    dob=null             : date                         # date of birth
    sex="unknown"        : enum('M','F','unknown')      # sex
    mouse_notes=""       : varchar(4096)                # other comments and distinguishing features
    """

@schema
class Session(dj.Manual):
    definition = """
    -> Mouse
    session_number       : smallint                     # session number
    ---
    session_date         : date                         # date
    person               : varchar(100)                 # researcher name
    data_path            : varchar(255)                 # 
    """

mice = [
    {'dob': '2019-01-05', 'mouse_id': 0, 'sex': 'M'},
    {'dob': '2020-01-06', 'mouse_id': 1, 'sex': 'M'},
    {'dob': "2019-08-23", 'mouse_id': 2, 'sex': 'M'},
    {'dob': "2020-01-22", 'mouse_id': 3, 'sex': 'F'}]

Mouse.insert(mice, skip_duplicates=True)

sessions = [
    {'mouse_id': 0, 
     'session_number': 1, 
     'session_date': "2019-12-03",
     'person': 'Shan', 
     'data_path': 'data'
    },
    {'mouse_id': 1,
     'person': 'Thinh',
     'data_path': 'data',
     'session_number': 1,
     'session_date': "2020-03-02"}]

Session.insert(sessions, skip_duplicates=True)

