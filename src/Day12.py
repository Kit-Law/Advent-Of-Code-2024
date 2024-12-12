

def gen_garden(filepath):
    garden = []

    with open(filepath) as file:
        for line in file:
            garden.append(list(line.rstrip()))
    
    return garden


def get_region(garden, plant, type, seen, region):
    if garden[plant[0]][plant[1]] != type or plant in seen:
        return

    region.append(plant)
    seen.add(plant)

    if plant[1] > 0:
        get_region(garden, (plant[0], plant[1] - 1), type, seen, region)
    if plant[1] + 1 < len(garden[0]):
        get_region(garden, (plant[0], plant[1] + 1), type, seen, region)
    if plant[0] > 0:
        get_region(garden, (plant[0] - 1, plant[1]), type, seen, region)
    if plant[0] + 1 < len(garden):
        get_region(garden, (plant[0] + 1, plant[1]), type, seen, region)


def get_regions(garden):
    regions = []
    seen = set()

    for j in range(len(garden)):
        for i in range(len(garden[0])):
            if (j, i) in seen:
                continue
            region = []
            get_region(garden, (j, i), garden[j][i], seen, region)
            regions.append(region)
    
    return regions


def get_perimeter(xs):
    body = set()
    perimeter = 0

    for x in xs:
        body.add(x)
    for x in xs:
        if (x[0] - 1, x[1]) not in body:
            perimeter += 1
        if (x[0], x[1] - 1) not in body:
            perimeter += 1
        if (x[0], x[1] + 1) not in body:
            perimeter += 1
        if (x[0] + 1, x[1]) not in body:
            perimeter += 1
    
    return perimeter


def get_sides(xs):
    body = set()
    number_of_sides = 0

    for x in xs:
        body.add(x)

    for x in xs:
        if (x[0] - 1, x[1]) not in body and (x[0], x[1] - 1) not in body:
            number_of_sides += 1
        if (x[0] - 1, x[1]) not in body and (x[0], x[1] + 1) not in body:
            number_of_sides += 1
        if (x[0] + 1, x[1]) not in body and (x[0], x[1] - 1) not in body:
            number_of_sides += 1
        if (x[0] + 1, x[1]) not in body and (x[0], x[1] + 1) not in body:
            number_of_sides += 1

        if (x[0] + 1, x[1]) in body and (x[0], x[1] + 1) in body and (x[0] + 1, x[1] + 1) not in body:
            number_of_sides += 1
        if (x[0] + 1, x[1]) in body and (x[0], x[1] - 1) in body and (x[0] + 1, x[1] - 1) not in body:
            number_of_sides += 1
        if (x[0] - 1, x[1]) in body and (x[0], x[1] + 1) in body and (x[0] - 1, x[1] + 1) not in body:
            number_of_sides += 1
        if (x[0] - 1, x[1]) in body and (x[0], x[1] - 1) in body and (x[0] - 1, x[1] - 1) not in body:
            number_of_sides += 1

    return number_of_sides


def star_one(filepath):
    garden = gen_garden(filepath)
    regions = get_regions(garden)

    total_price = 0
    for plants in regions:
        perimeter = get_perimeter(plants)
        total_price += len(plants) * perimeter

    return total_price


def star_two(filepath):
    garden = gen_garden(filepath)
    regions = get_regions(garden)

    total_price = 0
    for plants in regions:
        perimeter = get_sides(plants)
        total_price += len(plants) * perimeter

    return total_price


if __name__=="__main__":
    print(star_one("inputs/Day12.txt"))
    print(star_two("inputs/Day12.txt")) 
