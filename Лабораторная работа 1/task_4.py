users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_inuq = set(users)
users_info = {"Общее количество": 0, "Уникальные посещения": 0}
users_info["Общее количество"] = len(users)
users_info["Уникальные посещения"] = len(users_inuq)
print(users_info)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
