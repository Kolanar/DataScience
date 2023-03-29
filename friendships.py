from collections import Counter

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klien'}
]

friendships0 = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

"""
Инициализировать словарь пустым списком для идентификатора каждого пользователя
"""
friendships1 = {user["id"]: [] for user in users}

for i, j in friendships0:
    friendships1[i].append(j)
    friendships1[j].append(i)


# Число всех друзей
def number_of_friends(user):
    """Сколь друзей есть у пользователя user"""
    user_id = user['id']
    frined_ids = friendships1[user_id]
    return len(frined_ids)


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

# Создать список в формате (id пользователя, число друзей)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)


def friends_of_friends(user):
    user_id = user['id']
    return Counter(foaf_id for friend_id in friendships1[user_id] for foaf_id in friendships1[friend_id] if
                   foaf_id != user_id and foaf_id not in friendships1[user_id])

print(friends_of_friends(users[3]))