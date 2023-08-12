def groups_per_user(groups_dictionary):
    user_groups = {}
    # Recorre el diccionario de grupos
    for group in groups_dictionary:
        # Ahora recorre los usuarios en el grupo
        for user in groups_dictionary[group]:
            # Si el usuario ya está en user_groups, agrega el grupo a su lista de grupos
            if user in user_groups.keys():
                user_groups[user].append(group)
            # Si no está en user_groups, crea una nueva entrada con el grupo como primer elemento
            else:
                user_groups[user] = [group]
    # Retorna el diccionario de usuarios y sus grupos correspondientes
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
