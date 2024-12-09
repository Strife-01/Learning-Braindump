total_fr = 16000000
sec = 1000

# in ms
notes_pauses = [2, 4, 8]
notes_dur_list = [534.6534653465346, 267.3267326732673, 133.66336633663366]
notes_pause_list = [59.40594059405941, 29.702970297029704, 14.851485148514852]

dict_of_cycles = {}

# in sec
for i in range(len(notes_dur_list)):
    note_sec = notes_dur_list[i] / sec
    note_pause_sec = notes_pause_list[i] / sec
    print(f'for notes with a {notes_pauses[i]} pause number we need:')
    print(f'Total time of note in sec = {note_sec}')
    print(f'Total time of the pause in sec = {note_pause_sec}')
    note_clock_cycles = note_sec * total_fr
    note_pause_clock_cycle = note_pause_sec * total_fr   
    print(f'Total clock wasted cycles we need per note are {note_clock_cycles}')
    print(f'Total clock wasted cycles we need per pause are {note_pause_clock_cycle}')

    print(end='\n\n')

    dict_of_cycles[f'pause_{i}_note_cycles'] = note_clock_cycles
    dict_of_cycles[f'pause_{i}_note_pause_cycles'] = note_pause_clock_cycle

print(dict_of_cycles)

