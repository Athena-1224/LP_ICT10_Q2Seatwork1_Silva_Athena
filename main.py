from pyscript import document

def candidate_checker(e):
    club_members = ['yna sabulao', 'athena silva', 'divine lipura', 'gabby chua', 'micaiah robles', 'johann magno', 'sophie gamban', 'jacob opilla', 'kate velo', 'luis solis', 'rebecca vinco', 'manila martinez', 'youngeun song', 'keiko santos', 'pio serdena', 'nathan bernaldez']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f'{f_name.strip()} {l_name.strip()}'
    member_checker = candidate.lower() in club_members  

    #fstring (group of words) for messages specifically
    messages = (f'Sorry {candidate}, your name is not on the list. See you next time!', 
                f'Congratulations, {candidate}! You are now part of the Grade 10 Glee Club !!') 

    document.getElementById('result').innerHTML = messages[member_checker]