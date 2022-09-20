# Initialization procedure

## Part 1
As the cube is limited to 100^3 for part 1, it seems that brute force is a viable option. Cautious about what part 2 will bring, I'll use a dictionary to populate cubes that are on, and depopulate cubes that are off. This means that the dictionary could at most have a million cubes, but with 16GB of RAM we're fine... Though we might have a problem if we have a lot of instructions. Maybe brute force won't work.
If we follow the instructions in reverse order, then we don't have to maintain an array of ons and offs, we can just add/subtract the number of bits switched based on overlap with cubes we've already seen (because, going backwards, we can count on the fact that they would override it anyhow). 

## Part 2