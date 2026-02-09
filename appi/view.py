import requests
import sys
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QPixmap


def view_map(ll_spn=None, map_type="map", add_params=None):
    if ll_spn:
        map_requests = f'https://static-maps.yandex.ru/1.x/?{ll_spn}&l={map_type}'
    else:
        map_requests = f'https://static-maps.yandex.ru/1.x/?l={map_type}'

    if add_params:
        map_requests += f'&{add_params}'

    r = requests.get(map_requests)

    if not r:
        print("Ошибка выполнения запроса:")
        print("Http статус:", r.status_code, "(", r.reason, ")")
        sys.exit()

    file = "map.png"
    with open(file, "wb") as f:
        f.write(r.content)

    app = QApplication(sys.argv)
    label = QLabel()
    pixmap = QPixmap(file)
    label.setPixmap(pixmap)
    label.show()
    sys.exit(app.exec())