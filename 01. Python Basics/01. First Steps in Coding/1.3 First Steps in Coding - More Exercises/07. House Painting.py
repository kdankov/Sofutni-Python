house_height = float(input())
length_of_side_wall = float(input())
length_of_triangle_roof_wall = float(input())

side_wall_area = house_height * length_of_side_wall
window_area = 1.5 * 1.5
both_sides_area = 2 * side_wall_area - 2 * window_area

back_wall_area = house_height * house_height
door_area = 1.2 * 2
both_faces_area = 2 * back_wall_area - door_area

total_walls_area = both_sides_area + both_faces_area
green_paint_needed = total_walls_area / 3.4

both_roof_rectangles_area = 2 * (house_height * length_of_side_wall)
both_roof_triangles_area = 2 * (house_height * length_of_triangle_roof_wall / 2)

totalRoofArea = both_roof_rectangles_area + both_roof_triangles_area
redPaintNeeded = totalRoofArea / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{redPaintNeeded:.2f}')
