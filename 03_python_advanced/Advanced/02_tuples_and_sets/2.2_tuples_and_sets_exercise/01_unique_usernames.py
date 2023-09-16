usernames_count = int(input())

unique_usernames = set()

for _ in range(usernames_count):
    username = input()
    unique_usernames.add(username)

for user in unique_usernames:
    print(user)