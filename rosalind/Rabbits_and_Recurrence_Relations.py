iterations = 6

reproduction_factor = 1

mature_pop = 0
teen_pop = 0
youth_pop = 1

for i in range(iterations - 1):
    mature_pop += teen_pop
    teen_pop = 0

    teen_pop += youth_pop
    youth_pop = 0

    youth_pop += mature_pop * reproduction_factor

print(mature_pop + youth_pop + teen_pop)