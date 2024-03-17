iterations = 8

death_speed = 4

def get_rabbit_pop(iterations, death_speed):
    mature_pop = 0
    teen_pop = 0
    youth_pop = 1
    deletions = []    
    for i in range(death_speed):
        deletions.append(0)
    
    for i in range(iterations - 1):
        for j in range(death_speed - 1):
            index = death_speed - 2 - j
            deletions[index + 1] = deletions[index]
            deletions[index] = 0
        mature_pop += teen_pop
        teen_pop = 0

        deletions[0] += youth_pop

        teen_pop += youth_pop
        youth_pop = 0

        youth_pop += mature_pop
        
        mature_pop -= deletions[-1]
        deletions[-1] = 0
    return mature_pop + youth_pop + teen_pop

print(get_rabbit_pop(iterations, death_speed))