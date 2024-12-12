import Helpers.Grids as Grids


def get_region(garden, plant, type, seen, region):
    if garden[plant] != type or plant in seen:
        return

    region.append(plant)
    seen.add(plant)

    for neighbor in Grids.get_cardinal_neighbors(plant, garden):
        get_region(garden, neighbor, type, seen, region)


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
        for surrounding in Grids.get_adjacent_points(x):
            if surrounding not in body:
                perimeter += 1
    
    return perimeter


def get_sides(xs):
    body = set()
    number_of_sides = 0

    for x in xs:
        body.add(x)

    for x in xs:
        surroundings = Grids.get_adjacent_points(x, True)

        if surroundings["N"] not in body and surroundings["W"] not in body:
            number_of_sides += 1
        if surroundings["N"] not in body and surroundings["E"] not in body:
            number_of_sides += 1
        if surroundings["S"] not in body and surroundings["W"] not in body:
            number_of_sides += 1
        if surroundings["S"] not in body and surroundings["E"] not in body:
            number_of_sides += 1

        if surroundings["S"] in body and surroundings["E"] in body and surroundings["SE"] not in body:
            number_of_sides += 1
        if surroundings["S"] in body and surroundings["W"] in body and surroundings["SW"] not in body:
            number_of_sides += 1
        if surroundings["N"] in body and surroundings["E"] in body and surroundings["NE"] not in body:
            number_of_sides += 1
        if surroundings["N"] in body and surroundings["W"] in body and surroundings["NW"] not in body:
            number_of_sides += 1

    return number_of_sides


def star_one(filepath):
    garden = Grids.read_grid_from_file(filepath)
    regions = get_regions(garden)

    total_price = 0
    for plants in regions:
        perimeter = get_perimeter(plants)
        total_price += len(plants) * perimeter

    return total_price


def star_two(filepath):
    garden = Grids.read_grid_from_file(filepath)
    regions = get_regions(garden)

    total_price = 0
    for plants in regions:
        perimeter = get_sides(plants)
        total_price += len(plants) * perimeter

    return total_price


if __name__=="__main__":
    print(star_one("inputs/Day12.txt"))
    print(star_two("inputs/Day12.txt")) 
