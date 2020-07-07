import json
import socket

HOST = 'localhost'
PORT = 8888

with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        # Получаем хедер запроса и сохраняем в переменную
        # декодируя и добавляя в список разбивая на пары значений
        data = conn.recv(1024).decode('utf-8').split('\r\n')
        list_of_lists = []
        # Полученные в запросе заголовки закидываем в список списков
        # разбивая пары по елементам списков
        for el in data:
            list_of_lists.append(el.split(':'))
        # Объявляем словарь, закидываем в него список списков
        # Используя первое значение елемента воженного списка как ключ
        # Втрое значение как значение
        # Первые два элемента словаря не делятся, но статичны
        # Поэтому добавляем их статично руками
        data_dict = {}
        data_dict['Method'] = 'GET / HTTP/1.1'
        data_dict['Host'] = 'localhost:8888'
        for el in list_of_lists[2:-2]:
            data_dict[el[0]] = el[1]
        # Преобразуем словарь в JSОN файл
        json_str = json.dumps(data_dict)
        # Формируем строку для отправки
        # Строка состоит из статичного заголовка и сформированного тела
        send_data = f'HTTP/1.1 200 OK\n Content-Length: 100\n Connection: close\n Content-Type: text/json\n\n {json_str}'.encode(
            "utf-8")
        conn.send(send_data)
