import json

events_description = {
    'stimulus_pair': {
        'LongName': 'Stimulus pair',
        'Description': ''
    },
    'correct_response': {
        'LongName': 'Correct response',
        'Description': '',
    },
    'stim_file_left': {
        'LongName': 'Left-hand stimulus file',
        'Description': '',
    },
    'stim_file_right': {
        'LongName': 'Right-hand stimulus file',
        'Description': '',
    },
    'stim_type_left': {
        'LongName': 'Left-hand stimulus type',
        'Description': '',
    },
    'stim_type_right': {
        'LongName': 'Right-hand stimulus type',
        'Description': '',
    },
    'feedback': {
        'LongName': 'Participant feedback',
        'Description': '',
    },
    'feedback_onset': {
        'LongName': 'Onset of feedback screen',
        'Description': '',
    },
    'feedback_duration': {
        'LongName': 'Duration of feedback screen',
        'Description': '',
    }
}

bold_description = {
    'CogAtlasID': 'trm_5667483dcc371',
    'TaskName': 'Probabilistic Selection Task'
}

with open('task-PST_events.json', 'w') as fo:
    json.dump(events_description, fo, sort_keys=True, indent=4)

with open('task-PST_bold.json', 'w') as fo:
    json.dump(bold_description, fo, sort_keys=True, indent=4)
