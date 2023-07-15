easter_breads_count = int(input())
eggs_count = int(input())
cookies_kg = int(input())

final_sum = easter_breads_count * 3.20 + eggs_count * 4.35 + eggs_count * 12 * 0.15 + cookies_kg * 5.40

print(f'{final_sum:.2f}')