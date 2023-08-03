def wave(people):
    people = people.lower()
    waves = [people[:i] + people[i].upper() + people[i + 1:] for i in range(len(people)) if people[i] != ' ']
    return waves