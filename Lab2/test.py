if name == "main":
    # Пример работы с JSON
    json_rep = MyEntity_rep_json("data.json")
    json_rep.write_all([{"ID": None, "Field1": "value1", "Field2": "value2"}])
    print(json_rep.get_all())

    # Пример работы с YAML
    yaml_rep = MyEntity_rep_yaml("data.yaml")
    yaml_rep.write_all([{"ID": None, "Field1": "value1", "Field2": "value2"}])
    print(yaml_rep.get_all())

    # Пример работы с БД
    db_rep = MyEntity_rep_DB()
    db_rep.write_all([{"ID": None, "Field1": "value1", "Field2": "value2"}])
    print(db_rep.get_all())

    # Пример использования адаптера
    db_adapter = DBAdapter(db_rep)
    print(db_adapter.get_all())

    # Пример использования декоратора с фильтрацией
    decorator = FilterSortDecorator(db_adapter, filter_func=lambda x: x["Field1"] == "value1",
                                    sort_func=lambda x: x["Field2"])
    print(decorator.get_k_n_short_list(0, 1))