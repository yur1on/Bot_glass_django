from aiogram import types

glass_data9 = [
    {"model": "<b>Samsung A30/ Samsung A50/ Samsung A50s/ Samsung M30 2019/ Samsung M30s 2019/ Samsung M21/ Samsung M31</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.7мм \nНижняя часть - 6мм \nБоковая рамка - 1.4мм", "height": 155, "width": 71, "photo_path": "photos/samsung a30.png"},

    # {"model": "Samsung A50", "height": 333, "width": 33, "photo_path": "photos/Samsung_A50.jpg"},
    # {"model": "Samsung A50s", "height": 155, "width": 71, "photo_path": "photos/Samsung_A50s.jpg"},

    {"model": "<b>Samsung A51/ Samsung M31s 2020/ Samsung M71</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 3.4мм \nБоковая рамка - 1.1мм", "height": 155.5, "width": 70.5, "photo_path": "photos/samsung a51.png"},

    {"model": "<b>Samsung A52/ Samsung A52S 5G/ Samsung A53 5G/ Samsung S20FE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 3.6мм \nБоковая рамка - 1.4мм", "height": 156, "width": 71, "photo_path": "photos/samsung a52.png"},

    {"model": "<b>Samsung M52/ Samsung M53/ Samsung A73 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 3.4мм \nБоковая рамка - 1.35мм", "height": 160.5, "width": 73, "photo_path": "photos/samsung a73.png"},

    {"model": "<b>Samsung A33 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 5.7мм \nБоковая рамка - 1.8мм", "height": 156.5, "width": 70.5},

    {"model": "<b>Samsung S21 plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 2.2мм \nБоковая рамка - 1мм", "height": 158.5, "width": 72.5, "photo_path": "photos/samsung s21 plus.png"},

    # {"model": "Samsung A04", "height": 15, "width": 71},
    # {"model": "Samsung F04", "height": 15, "width": 71},
    # {"model": "Samsung M04", "height": 15, "width": 71},

    {"model": "<b>Samsung A05</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.32мм \nНижняя часть - 5.59мм \nБоковая рамка - 1.58мм", "height": 164.5, "width": 74, "photo_path": "photos/samsung a05.png"},

    {"model": "<b>Samsung A05s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.52мм \nНижняя часть - 4.97мм \nБоковая рамка - 1.43мм", "height": 163.5, "width": 73.5, "photo_path": "photos/samsung a05s.png"},

    {"model": "<b>Samsung A71/ Samsung M51 2020/ Samsung Note 10 Lite/ Samsung M62</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 3мм \nБоковая рамка - 1.1мм", "height": 160.5, "width": 73, "photo_path": "photos/samsung a71.png"},

    # {"model": "Samsung S20FE", "height": 15, "width": 71},
    # {"model": "Samsung A52", "height": 15, "width": 71},
    # {"model": "Samsung A52s", "height": 15, "width": 71},
    # {"model": "Samsung A53", "height": 15, "width": 71},

    {"model": "<b>Samsung A31</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 6.2мм \nБоковая рамка - 1.6мм", "height": 155.5, "width": 70, "photo_path": "photos/samsung a31.png"},

    {"model": "<b>Samsung A80 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 3.3мм \nБоковая рамка - 1.3мм", "height": 160.5, "width": 73, "photo_path": "photos/samsung a80.png"},

    {"model": "<b>Samsung A70 2019/ Samsung A70S</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 3.3мм \nБоковая рамка - 1.4мм", "height": 160.5, "width": 73, "photo_path": "photos/samsung a70.png"},

    {"model": "<b>Samsung A41</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.3мм \nНижняя часть - 3.3мм \nБоковая рамка - 1.1мм", "height": 147, "width": 67, "photo_path": "photos/samsung a41.png"},

    {"model": "<b>Samsung A34</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.3мм \nНижняя часть - 3.8мм \nБоковая рамка - 2.3мм", "height": 157.5, "width": 74.5, "photo_path": "photos/samsung a34 5g.png"},

    {"model": "<b>Samsung A14/ Samsung A14 5G/ Samsung M14</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.5мм \nНижняя часть - 6.63мм \nБоковая рамка - 2мм", "height": 162, "width": 72.5, "photo_path": "photos/samsung a14.png"},

    {"model": "<b>Samsung A24</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.4мм \nНижняя часть - 5.7мм \nБоковая рамка - 1.8мм", "height": 157, "width": 73, "photo_path": "photos/samsung a24.png"},

    {"model": "<b>Samsung A10 2019/ Samsung M10 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 6.3мм \nБоковая рамка - 1.6мм", "height": 151.5, "width": 71.5, "photo_path": "photos/samsung a10.png"},

    {"model": "<b>Samsung A10s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.5мм \nНижняя часть - 6.63мм \nБоковая рамка - 2мм", "height": 152.5, "width": 72, "photo_path": "photos/samsung a10s.png"},

    {"model": "<b>Samsung A20/ Samsung A30s/ Samsung M10s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 6.2мм \nБоковая рамка - 1.8мм", "height": 155, "width": 71, "photo_path": "photos/samsung a20.png"},

    {"model": "<b>Samsung A20s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 6.8мм \nБоковая рамка - 1.8мм", "height": 159, "width": 73.5, "photo_path": "photos/samsung a20s.png"},

    {"model": "<b>Samsung A21s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3мм \nНижняя часть - 5.3мм \nБоковая рамка - 1.7мм", "height": 160.5, "width": 72, "photo_path": "photos/samsung a21s.png"},

    # {"model": "Samsung A300", "height": 15, "width": 71},

    {"model": "<b>Samsung A310</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.3мм \nНижняя часть - 12.7мм \nБоковая рамка - 1.4мм", "height": 131.5, "width": 62.5, "photo_path": "photos/samsung a310.png"},

    {"model": "<b>Samsung A320</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.1мм \nНижняя часть - 12.8мм \nБоковая рамка - 1.8мм", "height": 132.5, "width": 63.5},

    {"model": "<b>Samsung A40 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 3.4мм \nБоковая рамка - 1.1мм", "height": 141, "width": 65.5, "photo_path": "photos/samsung a40.png"},

    {"model": "<b>Samsung A40s 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 5.8мм \nБоковая рамка - 1.1мм", "height": 155, "width": 71, "photo_path": "photos/samsung a40s.png"},

    # {"model": "Samsung A500", "height": 15, "width": 71},

    {"model": "<b>Samsung A510</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.1мм \nНижняя часть - 12.8мм \nБоковая рамка - 1.3мм", "height": 141.5, "width": 68, "photo_path": "photos/samsung a510.png"},

    {"model": "<b>Samsung A520</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.9мм \nНижняя часть - 13.1мм \nБоковая рамка - 1.8мм", "height": 144, "width": 69.5, "photo_path": "photos/samsung a520.png"},

    {"model": "<b>Samsung A600</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.8мм \nНижняя часть - 8.9мм \nБоковая рамка - 1.6мм", "height": 146, "width": 67, "photo_path": "photos/samsung a600.png"},

    {"model": "<b>Samsung A605</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.6мм \nНижняя часть - 9.1мм \nБоковая рамка - 1.9мм", "height": 156.5, "width": 72, "photo_path": "photos/samsung a605.png"},

    # {"model": "Samsung A700", "height": 155, "width": 71},

    {"model": "<b>Samsung A710</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.1мм \nНижняя часть - 13.3мм \nБоковая рамка - 1.2мм", "height": 148.5, "width": 71.5, "photo_path": "photos/samsung a710.png"},

    # {"model": "Samsung A720", "height": 155, "width": 71},

    {"model": "<b>Samsung A750</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.9мм \nНижняя часть - 8.8мм \nБоковая рамка - 2.1мм", "height": 155, "width": 72.5, "photo_path": "photos/samsung a750.png"},

    {"model": "<b>Samsung A530</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.2мм \nНижняя часть - 8.2мм \nБоковая рамка - 2мм", "height": 145.5, "width": 67, "photo_path": "photos/samsung a530.png"},

    {"model": "<b>Samsung A730</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.2мм \nНижняя часть - 9мм \nБоковая рамка - 2мм", "height": 156, "width": 72, "photo_path": "photos/samsung a730.png"},

    # {"model": "Samsung A90", "height": 155, "width": 71},

    {"model": "<b>Samsung A920</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 7.8мм \nНижняя часть - 7.1мм \nБоковая рамка - 1.4мм", "height": 159, "width": 73.5, "photo_path": "photos/samsung a920.png"},

    # {"model": "Samsung J120", "height": 155, "width": 71},

    {"model": "<b>Samsung J250</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.3мм \nНижняя часть - 15.2мм \nБоковая рамка - 3.1мм", "height": 140.5, "width": 69},

    # {"model": "Samsung J260", "height": 155, "width": 71},

    {"model": "<b>Samsung J200</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.3мм \nНижняя часть - 13.7мм \nБоковая рамка - 2.8мм", "height": 133, "width": 65, "photo_path": "photos/samsung j200.png"},

    {"model": "<b>Samsung J320</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.3мм \nНижняя часть - 14.2мм \nБоковая рамка - 2.6мм", "height": 138.5, "width": 67.5, "photo_path": "photos/samsung j320.png"},

    {"model": "<b>Samsung J330</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 15.3мм \nНижняя часть - 14.3мм \nБоковая рамка - 2.6мм", "height": 140.5, "width": 67.5},

    {"model": "<b>Samsung J400</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.7мм \nНижняя часть - 12.9мм \nБоковая рамка - 2.6мм", "height": 148.5, "width": 74.5, "photo_path": "photos/samsung j400.png"},

    {"model": "<b>Samsung J610/ Samsung J415</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 9.6мм \nНижняя часть - 9.6мм \nБоковая рамка - 2.5мм", "height": 157, "width": 72.5, "photo_path": "photos/samsung j610.png"},

    {"model": "<b>Samsung J530</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 16.8мм \nНижняя часть - 15.8мм \nБоковая рамка - 2.7мм", "height": 143.5, "width": 68, "photo_path": "photos/samsung j530.png"},

    {"model": "<b>Samsung J500</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.2мм \nНижняя часть - 13.6мм \nБоковая рамка - 2.5мм", "height": 138.5, "width": 67.5},

    # {"model": "Samsung J510", "height": 155, "width": 71},

    {"model": "<b>Samsung G570</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 15мм \nНижняя часть - 15.2мм \nБоковая рамка - 2.6мм", "height": 140, "width": 67, "photo_path": "photos/samsung g570.png"},

    {"model": "<b>Samsung J600</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.5мм \nНижняя часть - 8.7мм \nБоковая рамка - 2.1мм", "height": 146.5, "width": 67, "photo_path": "photos/samsung j600.png"},

    {"model": "<b>Samsung J730</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 15мм \nНижняя часть - 12,7мм \nБоковая рамка - 1.2мм", "height": 149.5, "width": 72, "photo_path": "photos/samsung j730.png"},

    # {"model": "Samsung J710", "height": 155, "width": 71},

    # {"model": "Samsung J701", "height": 155, "width": 71},

    {"model": "<b>Samsung J810</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 9.2мм \nНижняя часть - 9мм \nБоковая рамка - 2.6мм", "height": 156, "width": 72.5},

    # {"model": "Samsung M20 2019", "height": 155, "width": 71},

    {"model": "<b>Samsung M40 2019/ Samsung A60 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 4мм \nБоковая рамка - 1.6мм", "height": 151.5, "width": 70.5, "photo_path": "photos/samsung a60.png"},

    # {"model": "Samsung Note 4", "height": 155, "width": 71},

    {"model": "<b>Samsung Note 5</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.9мм \nНижняя часть - 9.78мм \nБоковая рамка - 1.9мм", "height": 155, "width": 72.5},

    # {"model": "Samsung Note 2", "height": 155, "width": 71},

    {"model": "<b>Samsung Note 8</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3.6мм \nНижняя часть - 6.36мм \nБоковая рамка - 2.15мм", "height": 1, "width": 70.5},

    # {"model": "Samsung Note 9", "height": 155, "width": 71},

    {"model": "<b>Samsung S10e</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.8мм \nНижняя часть - 3.5мм \nБоковая рамка - 1.6мм", "height": 138, "width": 66, "photo_path": "photos/samsung s10e.png"},

    # {"model": "Samsung S20", "height": 155, "width": 71},
    #
    # {"model": "Samsung S20 Plus", "height": 155, "width": 71},
    #
    # {"model": "Samsung S20 Ultra", "height": 155, "width": 71},
    #
    # {"model": "Samsung S3", "height": 155, "width": 71},
    #
    # {"model": "Samsung S4", "height": 155, "width": 71},
    #
    # {"model": "Samsung S4 Mini", "height": 155, "width": 71},
    #
    # {"model": "Samsung S5", "height": 155, "width": 71},
    #
    # {"model": "Samsung S6 Edge", "height": 155, "width": 71},
    #
    # {"model": "Samsung s6", "height": 155, "width": 71},
    #
    # {"model": "Samsung S6 Edge", "height": 155, "width": 71},

    {"model": "<b>Samsung S7</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.3мм \nНижняя часть - 13.2мм \nБоковая рамка - 1.8мм", "height": 140, "width": 67.5},

    # {"model": "Samsung T510", "height": 155, "width": 71},
    # {"model": "Samsung T515", "height": 155, "width": 71},
    #
    # {"model": "Samsung T280", "height": 155, "width": 71},
    # {"model": "Samsung T285", "height": 155, "width": 71},
    #
    # {"model": "Samsung T290", "height": 155, "width": 71},
    # {"model": "Samsung T295", "height": 155, "width": 71},
    #
    # {"model": "Samsung T800", "height": 155, "width": 71},
    # {"model": "Samsung T805", "height": 155, "width": 71},
    #
    # {"model": "Samsung T810", "height": 155, "width": 71},
    # {"model": "Samsung T813", "height": 155, "width": 71},
    # {"model": "Samsung T815", "height": 155, "width": 71},
    # {"model": "Samsung T819", "height": 155, "width": 71},
    # {"model": "Samsung T820", "height": 155, "width": 71},
    # {"model": "Samsung T825", "height": 155, "width": 71},
    #
    # {"model": "Samsung T835", "height": 155, "width": 71},
    #
    # {"model": "Samsung T720", "height": 155, "width": 71},
    # {"model": "Samsung T725", "height": 155, "width": 71},
    #
    # {"model": "Samsung T860", "height": 155, "width": 71},
    # {"model": "Samsung T865", "height": 155, "width": 71},
    #
    # {"model": "Samsung T700", "height": 155, "width": 71},
    # {"model": "Samsung T705", "height": 155, "width": 71},
    #
    # {"model": "Samsung A01", "height": 142.5, "width": 67},
    # {"model": "Samsung M01", "height": 142.5, "width": 67},
    #
    # {"model": "Samsung T321", "height": 155, "width": 71},
    # {"model": "Samsung T325", "height": 155, "width": 71},
    #
    # {"model": "Samsung T580", "height": 155, "width": 71},
    # {"model": "Samsung T585", "height": 155, "width": 71},
    #
    # {"model": "Samsung T590", "height": 155, "width": 71},
    # {"model": "Samsung T595", "height": 155, "width": 71},
    #
    # {"model": "Samsung T385", "height": 155, "width": 71},
    #
    # {"model": "Samsung T561", "height": 155, "width": 71},

    {"model": "<b>Samsung A11/ Samsung M11</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 6.6мм \nБоковая рамка - 1.8мм", "height": 157.5, "width": 72.5, "photo_path": "photos/samsung a11.png"},

    # {"model": "Samsung A20E", "height": 155, "width": 71},
    #
    # {"model": "Samsung P610", "height": 155, "width": 71},
    # {"model": "Samsung P615", "height": 155, "width": 71},
    # {"model": "Samsung P610", "height": 155, "width": 71},
    # {"model": "Samsung P619", "height": 155, "width": 71},

    {"model": "<b>Samsung A71 5G/ Samsung S10 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 2.7мм \nБоковая рамка - 1.3мм", "height": 159, "width": 72.5, "photo_path": "photos/samsung s10 lite.png"},

    {"model": "<b>Samsung Note 20</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.2мм \nНижняя часть - 2.7мм \nБоковая рамка - 1.1мм", "height": 159, "width": 72.5, "photo_path": "photos/samsung note 20.png"},

    # {"model": "Samsung Note 20", "height": 155, "width": 71},

    {"model": "<b>Samsung A02s/ Samsung A03/ Samsung A03S/ Samsung A04e/ Samsung m02s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.48мм \nНижняя часть - 6.6мм \nБоковая рамка - 2мм", "height": 160.5, "width": 72, "photo_path": "photos/samsung a02s.png"},

    {"model": "<b>Samsung S21</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.1мм \nНижняя часть - 2.1мм \nБоковая рамка - 1.2мм", "height": 148.5, "width": 68, "photo_path": "photos/samsung s21.png"},

    {"model": "<b>Samsung S21FE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 3.1мм \nБоковая рамка - 1.5мм", "height": 152.5, "width": 71.5, "photo_path": "photos/samsung s21fe.png"},

    # {"model": "Samsung T395", "height": 155, "width": 71},

    {"model": "<b>Samsung A72</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.4мм \nНижняя часть - 3.8мм \nБоковая рамка - 1.7мм", "height": 161, "width": 73.5, "photo_path": "photos/samsung a72.png"},

    # {"model": "Samsung Z Fold 2", "height": 155, "width": 71},
    #
    # {"model": "Samsung T500", "height": 155, "width": 71},
    # {"model": "Samsung T505", "height": 155, "width": 71},

    {"model": "<b>Samsung A32/ Samsung M22/ Samsung M32</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 5.6мм \nБоковая рамка - 1.4мм", "height": 155, "width": 70, "photo_path": "photos/samsung a32.png"},

    # {"model": "Samsung T220", "height": 155, "width": 71},
    # {"model": "Samsung T225", "height": 155, "width": 71},
    #
    # {"model": "Samsung T733", "height": 155, "width": 71},
    # {"model": "Samsung T735", "height": 155, "width": 71},
    # {"model": "Samsung T736", "height": 155, "width": 71},
    # {"model": "Samsung T970", "height": 155, "width": 71},
    # {"model": "Samsung T975", "height": 155, "width": 71},
    # {"model": "Samsung T976", "height": 155, "width": 71},
    # {"model": "Samsung X800", "height": 155, "width": 71},
    # {"model": "Samsung X806", "height": 155, "width": 71},

    {"model": "<b>Samsung A22s/ Samsung A22 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 6.6мм \nБоковая рамка - 1.6мм", "height": 162, "width": 72, "photo_path": "photos/samsung a22 5g.png"},

    {"model": "<b>Samsung A22 4G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 5.6мм \nБоковая рамка - 1.4мм", "height": 155, "width": 70, "photo_path": "photos/samsung a22.png"},

    # {"model": "Samsung T870", "height": 155, "width": 71},
    # {"model": "Samsung T875", "height": 155, "width": 71},
    # {"model": "Samsung X700", "height": 155, "width": 71},
    # {"model": "Samsung X706", "height": 155, "width": 71},
    #
    # {"model": "Samsung Z Fold 3", "height": 155, "width": 71},
    #
    # {"model": "Samsung S10", "height": 155, "width": 71},
    #
    # {"model": "Samsung S10 Plus", "height": 155, "width": 71},

    {"model": "<b>Samsung A12/ Samsung A02/ Samsung A04s/ Samsung M02/ Samsung M12/ Samsung A13 5G/ Samsung A13 (137f)/ Samsung A32 5g</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.7мм \nНижняя часть - 6мм \nБоковая рамка - 1.8мм", "height": 160.5, "width": 72.5, "photo_path": "photos/samsung a12.png"},

    {"model": "<b>Samsung S22</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 1.5мм \nБоковая рамка - 1.5мм", "height": 143, "width": 68, "photo_path": "photos/samsung s22 5g.png"},

    # {"model": "Samsung S22 Ultra", "height": 155, "width": 71},

    {"model": "<b>Samsung A42</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 5мм \nБоковая рамка - 1.2мм", "height": 160, "width": 72, "photo_path": "photos/samsung a42.png"},

    {"model": "<b>Samsung A13(a135)/ Samsung A23/ Samsung A23 5G/ Samsung M23 5G/ Samsung M33</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 5.4мм \nБоковая рамка - 1.8мм", "height": 160.5, "width": 72, "photo_path": "photos/samsung a13.png"},

    # {"model": "Samsung X200", "height": 155, "width": 71},
    # {"model": "Samsung X205", "height": 155, "width": 71},
    #
    # {"model": "Samsung X900", "height": 155, "width": 71},
    # {"model": "Samsung X906", "height": 155, "width": 71},
    #
    # {"model": "Samsung A22", "height": 155, "width": 71},

    {"model": "<b>Samsung A54 / Samsung S23FE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.5мм \nНижняя часть - 4.1мм \nБоковая рамка - 2.4мм", "height": 154.5, "width": 73, "photo_path": "photos/samsung a54.png"},

    {"model": "<b>Samsung S22 Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.6мм \nНижняя часть - 1.5мм \nБоковая рамка - 1.5мм", "height": 154.5, "width": 73, "photo_path": "photos/samsung s22 plus.png"},

    {"model": "<b>Samsung S23 Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 1.7мм \nБоковая рамка - 1.5мм", "height": 154.5, "width": 73, "photo_path": "photos/samsung s23 plus.png"},

    {"model": "<b>Samsung S23</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.4мм \nНижняя часть - 1.7мм \nБоковая рамка - 1.4мм", "height": 143, "width": 67.5, "photo_path": "photos/samsung s23.png"},

    # {"model": "Samsung Z Fold 5", "height": 155, "width": 71},
    #
    # {"model": "Samsung Z Fold 4", "height": 155, "width": 71},
    #
    # {"model": "Samsung Note 10 plus", "height": 155, "width": 71},

    {"model": "<b>Samsung A21</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3мм \nНижняя часть - 7.1мм \nБоковая рамка - 2.3мм", "height": 161.5, "width": 72.5, "photo_path": "photos/samsung a21.png"},

    {"model": "<b>Samsung A01 Core/ Samsung M01 Core</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8мм \nНижняя часть - 8мм \nБоковая рамка - 2мм", "height": 138, "width": 64, "photo_path": "photos/samsung a01 core.png"},

    # {"model": "Samsung A03 core", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 5", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 5c", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 5 Pro", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 5s Plus", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 6", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Mi 8</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.86мм \nНижняя часть - 7мм \nБоковая рамка - 1.9мм", "height": 152, "width": 72.5, "photo_path": "photos/xiaomi mi8.png"},

    {"model": "<b>Xiaomi Mi 8 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.9мм \nНижняя часть - 6.55мм \nБоковая рамка - 2.1мм", "height": 152.5, "width": 72, "photo_path": "photos/xiaomi mi8 lite.png"},

    # {"model": "Xiaomi Mi 8 Pro", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Mi 8 Se</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 5.68мм \nБоковая рамка - 2мм", "height": 143.5, "width": 69, "photo_path": "photos/xiaomi mi8 se.png"},

    {"model": "<b>Xiaomi Mi 9 Lite/ Xiaomi Mi A3 Lite/ Xiaomi Mi CC9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.64мм \nНижняя часть - 3.8мм \nБоковая рамка - 1.9мм", "height": 153.5, "width": 71.5, "photo_path": "photos/xiaomi mi9 lite.png"},

    {"model": "<b>Xiaomi Mi 9 SE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.95мм \nНижняя часть - 3.6мм \nБоковая рамка - 1.76мм", "height": 143.5, "width": 67, "photo_path": "photos/xiaomi mi9se.png"},

    {"model": "<b>Xiaomi Mi 9T/ Xiaomi Mi 9T Pro/ Xiaomi K20/ Xiaomi K20 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 3.9мм \nБоковая рамка - 1.76мм", "height": 153.5, "width": 71.5, "photo_path": "photos/xiaomi mi9t.png"},

    {"model": "<b>Xiaomi Mi A2</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 9.5мм \nНижняя часть - 9.9мм \nБоковая рамка - 2мм", "height": 156, "width": 72.5, "photo_path": "photos/xiaomi mia2.png"},

    {"model": "<b>Xiaomi Mi A3</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.78мм \nНижняя часть - 6.48мм \nБоковая рамка - 1.6мм", "height": 150, "width": 68.5, "photo_path": "photos/xiaomi mia3.png"},

    # {"model": "Xiaomi Mi Mix 2", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Mi Mix 3</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 4.1мм \nБоковая рамка - 1.8мм", "height": 154.5, "width": 72, "photo_path": "photos/xiaomi mi mix3.png"},

    # {"model": "Xiaomi Mi Mix 3", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Note 10 Lite", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Note 2", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Note 3", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Note", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Note 10", "height": 155, "width": 71},
    # {"model": "Xiaomi Mi Note 10 Pro", "height": 155, "width": 71},
    # {"model": "Xiaomi Mi CC9 Pro", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Pocophone F1</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3.3мм \nНижняя часть - 7.7мм \nБоковая рамка - 2мм", "height": 152.5, "width": 72.5, "photo_path": "photos/xiaomi poco f1.png"},

    {"model": "<b>Xiaomi Redmi 8/ Xiaomi Redmi 8A</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 4.1мм \nБоковая рамка - 1.8мм", "height": 153, "width": 71.5, "photo_path": "photos/redmi 8.png"},

    # {"model": "Xiaomi Redmi Note 5", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi Note 5 Pro", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Redmi 5 Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.8мм \nНижняя часть - 10мм \nБоковая рамка - 2.2мм", "height": 155, "width": 72, "photo_path": "photos/redmi 5plus.png"},

    {"model": "<b>Xiaomi Redmi 5</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.8мм \nНижняя часть - 10.6мм \nБоковая рамка - 2.55мм", "height": 148.5, "width": 69.5, "photo_path": "photos/redmi 5.png"},

    {"model": "<b>Xiaomi Redmi Note 6 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.7мм \nНижняя часть - 1.47мм \nБоковая рамка - 1.9мм", "height": 154, "width": 72.5, "photo_path": "photos/redmi note 6pro.png"},

    {"model": "<b>Xiaomi Redmi Note 7/ Xiaomi Redmi Note 7 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3.6мм \nНижняя часть - 6.36мм \nБоковая рамка - 2.15мм", "height": 155, "width": 71, "photo_path": "photos/redmi note 7.png"},

    {"model": "<b>Xiaomi Redmi Note 8 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 3.8мм \nБоковая рамка - 1.47мм", "height": 156.5, "width": 73, "photo_path": "photos/redmi note 8 pro.png"},

    {"model": "<b>Xiaomi Redmi Note 8T</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3.4мм \nНижняя часть - 8мм \nБоковая рамка - 1.88мм", "height": 156.5, "width": 71, "photo_path": "photos/redmi note 8t.png"},

    {"model": "<b>Xiaomi Redmi Note 9/ Xiaomi Redmi 10X 4G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 4.9мм \nБоковая рамка - 1.68мм", "height": 158, "width": 73, "photo_path": "photos/redmi note 9.png"},

    {"model": "<b>Xiaomi Redmi Note 9s/ Xiaomi Redmi Note 9 Pro 4G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 4.47мм \nБоковая рамка - 1.78мм", "height": 161, "width": 73, "photo_path": "photos/redmi note 9 pro.png"},

    # {"model": "Xiaomi Redmi Pro", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 3", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi 4s", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi A1", "height": 155, "width": 71},
    # {"model": "Xiaomi Mi 5X", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Max 2", "height": 155, "width": 71},
    # {"model": "Xiaomi Mi Max", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Max 3", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Pad 2", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Mi Play", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Redmi 3", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi 3s", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi 3 Pro", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi 3x", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Redmi Redmi 9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.4мм \nНижняя часть - 5.6мм \nБоковая рамка - 1.6мм", "height": 159, "width": 73, "photo_path": "photos/redmi 9.png"},

    {"model": "<b>Xiaomi Redmi 9A/ Xiaomi Redmi 9C/ Xiaomi Redmi 10A/ Xiaomi Poco C3/ Xiaomi Poco C31/ Xiaomi Redmi 9AT/ Xiaomi Redmi 9i</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.78мм \nНижняя часть - 6.4мм \nБоковая рамка - 2.1мм", "height": 160.5, "width": 72.5, "photo_path": "photos/xiaomi redmi 9a.png"},

    {"model": "<b>Xiaomi Redmi Note 9 Pro 5G/ Xiaomi Poco X3/ Xiaomi Poco X3 Pro/ Xiaomi Poco M2 Pro/ Xiaomi Mi 10i/ Xiaomi Mi 10t Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 4.2мм \nБоковая рамка - 1.7мм", "height": 161, "width": 73, "photo_path": "photos/xiaomi poco x3.png"},

    {"model": "Xiaomi Poco X6 Pro/ Xiaomi Poco F6/ Xiaomi Redmi K70e/ Xiaomi Redmi Turbo 3", "height": 158, "width": 72, "photo_path": "photos/poco x6 pro.png"},

    # {"model": "Xiaomi Pocophone F2 Pro", "height": 155, "width": 71},
    # {"model": "Xiaomi K30 Pro", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Redmi K30", "height": 155, "width": 71},
    # {"model": "Xiaomi Poco F2", "height": 155, "width": 71},
    # {"model": "Xiaomi Poco X2", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Mi 10 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.9мм \nНижняя часть - 4.98мм \nБоковая рамка - 1.55мм", "height": 159.5, "width": 72, "photo_path": "photos/xiaomi mi10 lite.png"},

    {"model": "<b>Xiaomi Redmi Note 10 4G/ Xiaomi Redmi Note 11 4G/ Xiaomi Redmi Note 11 NFC/ Xiaomi Redmi Note 11S 4G/ Xiaomi Redmi Note 11SE/ Xiaomi Redmi Note 10S/ Xiaomi Redmi Note 12s/ Xiaomi Poco M4 Pro 4G/ Xiaomi Poco M5s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.34мм \nНижняя часть - 5.15мм \nБоковая рамка - 1.9мм", "height": 156, "width": 70.5, "photo_path": "photos/redmi note 10.png"},

    {"model": "<b>Xiaomi Redmi 9T/ Xiaomi Poco M2/ Xiaomi Poco M3</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.76мм \nНижняя часть - 6мм \nБоковая рамка - 1.8мм", "height": 158, "width": 73, "photo_path": "photos/xiaomi redmi 9t.png"},

    {"model": "<b>Xiaomi Mi 11 Lite/ Xiaomi Mi 11 Lite 5G NE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.6мм \nНижняя часть - 2.8мм \nБоковая рамка - 1.7мм", "height": 156, "width": 72, "photo_path": "photos/xiaomi mi11 lite.png"},

    {"model": "<b>Xiaomi Redmi Note 10 Pro 4G/ Xiaomi Redmi Note 11 Pro 4G/ Xiaomi Redmi Note 11 Pro 5G/ Xiaomi Redmi Note 11 Pro Plus/ Xiaomi Poco X4/ Xiaomi Poco X4 Pro/ Xiaomi Poco X4 Pro 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 3.75мм \nБоковая рамка - 1.76мм", "height": 160, "width": 73, "photo_path": "photos/redmi note 10 pro.png"},

    # {"model": "Xiaomi Redmi Note 9T", "height": 155, "width": 71},
    #
    #
    # {"model": "Xiaomi Mi Mix 4", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Black Shark 3", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Redmi 10/ Xiaomi Redmi Note 10 5G/ Xiaomi Redmi Note 10T/ Xiaomi Redmi Note 11 5G/ Xiaomi Poco M3 Pro/ Xiaomi Poco M3 Pro 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.3мм \nНижняя часть - 4.8мм \nБоковая рамка - 1.45мм", "height": 158, "width": 71.5, "photo_path": "photos/xiaomi redmi 10.png"},

    {"model": "<b>Xiaomi Redmi Note 8/ Xiaomi Redmi Note 8 2022</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 6.36мм \nБоковая рамка - 1.57мм", "height": 153.5, "width": 70.5, "photo_path": "photos/redmi note 8.png"},

    {"model": "<b>Xiaomi Mi 11i/ Xiaomi Mi 11X/ Xiaomi Mi 11X Pro/ Xiaomi Redmi K40/ Xiaomi Redmi K40 Pro/ Xiaomi Redmi K40 Pro Plus/ Xiaomi Poco F3/ Xiaomi Poco F4 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.75мм \nНижняя часть - 3.3мм \nБоковая рамка - 1.5мм", "height": 159.5, "width": 73, "photo_path": "photos/xiaomi poco f3.png"},

    {"model": "<b>Xiaomi Redmi Note 10 Pro 5G/ Xiaomi Redmi Note 11S 5G/ Xiaomi Redmi Note 11T 5G/ Xiaomi Redmi Note 11T Pro 5G/ Xiaomi Poco M4 Pro 5G/ Xiaomi Poco X3 GT/ Xiaomi Poco X3 NFC/ Xiaomi Poco F3 GT</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.15мм \nНижняя часть - 4.36мм \nБоковая рамка - 1.7мм", "height": 159.5, "width": 72.5, "photo_path": "photos/redmi note 10 pro 5g.png"},

    # {"model": "Xiaomi 12 Pro", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Black Shark 2/ Xiaomi Shark 2 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 9.66мм \nНижняя часть - 10.5мм \nБоковая рамка - 2мм", "height": 157, "width": 72.5, "photo_path": "photos/xiaomi black shark 2.png"},

    {"model": "<b>Xiaomi Mi 9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.47мм \nНижняя часть - 3.44мм \nБоковая рамка - 1.7мм", "height": 153.5, "width": 72, "photo_path": "photos/xiaomi mi9.png"},

    {"model": "<b>Xiaomi Redmi 10C/ Xiaomi Redmi 12C/Xiaomi Poco C40/ Xiaomi Poco C55</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.65мм \nНижняя часть - 5.95мм \nБоковая рамка - 2.1мм", "height": 164.5, "width": 72.5, "photo_path": "photos/xiaomi redmi 10c.png"},

    {"model": "<b>Xiaomi Redmi 13C/ Xiaomi Poco C65</b>", "height": 164.5, "width": 74, "photo_path": "photos/redmi 13c.png"},

    {"model": "<b>Xiaomi Redmi 15C</b>", "height": 167.5, "width": 76, "photo_path": "photos/Redmi 15c.png"},

    {"model": "<b>Xiaomi Redmi 14C / Xiaomi Redmi 14C 5G / Xiaomi Redmi A3 Pro / Xiaomi Redmi A5 / Xiaomi Poco C71 / Xiaomi Poco C75 / Xiaomi Poco C75 5G </b>", "height": 168, "width": 74.5, "photo_path": "photos/redmi 14c.png"},

    {"model": "<b>Tecno Spark Go-2024 / Tecno Spark Go / Tecno Spark 20 / Tecno Spark 20C / Tecno Pop 8 / Infinix Smart 8 / Infinix Smart 8 HD / Infinix Smart 8 Pro / Infinix Smart 8 Plus / Infinix Hot 40i / Itel P55 / Itel P55 Plus / Itel P55T / Itel P55 5G / Itel Power 50 / Itel RS4 / Itel 24L / tel A70S / Itel S24</b>", "height": 160, "width": 72, "photo_path": "photos/Infinix hot 40i.png"},

    {"model": "<b>Samsung a15 / Samsung a25 / Samsung M15 </b>", "height": 156, "width": 73, "photo_path": "photos/samsung a15.png"},

    {"model": "<b>Samsung a35 / Samsung a55</b>", "height": 159, "width": 75, "photo_path": "photos/samsung a35.png"},

    {"model": "<b>Vivo T3</b>", "height": 160, "width": 73, "photo_path": "photos/vivo t3.png"},

    {"model": "<b>Vivo V23 5G</b>", "height": 155, "width": 70.5, "photo_path": "photos/vivo v23 5g.png"},

    {"model": "<b>Xiaomi 12 Lite/ Xiaomi Poco F4 Pro/ Xiaomi Poco X4 GT/ Xiaomi Redmi 10X 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 2.8мм \nБоковая рамка - 1.5мм", "height": 157, "width": 72, "photo_path": "photos/xiaomi x4 gt.png"},

    {"model": "<b>Xiaomi Redmi 10 5G/ Xiaomi Redmi 11/ Xiaomi Redmi 11 Prime/ Xiaomi Redmi 11 Prime 5G/ Xiaomi Redmi Note 11E/ Xiaomi Redmi note 11R/ Xiaomi Poco M5/ Xiaomi Poco M4 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.25мм \nНижняя часть - 4.75мм \nБоковая рамка - 1.6мм", "height": 160, "width": 72, "photo_path": "photos/xiaomi poco m5.png"},

    {"model": "<b>Xiaomi Redmi A1/ Xiaomi Redmi A1 Plus/ Xiaomi Redmi A2/ Xiaomi Redmi A2 Plus/ Xiaomi Poco C50 / Xiaomi Poco C51 </b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.5мм \nНижняя часть - 6.4мм \nБоковая рамка - 1.9мм", "height": 160, "width": 72, "photo_path": "photos/redmi a1.png"},

    {"model": "<b>Xiaomi Redmi A3/ Xiaomi Redmi A3x/ Xiaomi Poco C61</b>", "height": 164.5, "width": 72, "photo_path": "photos/redmi a3.png"},

    # {"model": "Xiaomi Pad 5", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi 13 Lite", "height": 155, "width": 71},

    {"model": "<b>Xiaomi 13</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.55мм \nНижняя часть - 1.7мм \nБоковая рамка - 1.45мм", "height": 151, "width": 69.5, "photo_path": "photos/xiaomi 13.png"},

    {"model": "<b>Xiaomi Redmi Note 12 Pro/ Xiaomi Poco X5 Pro 5G/ Xiaomi Redmi Note 12 Pro Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 2.6мм \nБоковая рамка - 1.6мм", "height": 159.5, "width": 73.5, "photo_path": "photos/redmi note 12 pro.png"},

    {"model": "<b>Xiaomi Poco F5/ Xiaomi Poco M6 Pro 4G/ Xiaomi Note 13 5G/ Xiaomi Redmi Note 13 Pro 4g</b> ", "height": 158.5, "width": 72.5, "photo_path": "photos/poco f5.png"},

    # {"model": "Xiaomi Pad 6", "height": 155, "width": 71},

    {"model": "<b>Xiaomi Redmi 12</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.05мм \nНижняя часть - 4.25мм \nБоковая рамка - 1.45мм", "height": 164.5, "width": 73, "photo_path": "photos/xiaomi redmi 12.png"},

    {"model": "<b>Xiaomi Redmi Note 12/ Xiaomi Poco X5</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 5.26мм \nБоковая рамка - 1.58мм", "height": 162, "width": 73, "photo_path": "photos/redmi note 12.png"},

    {"model": "<b>Xiaomi Redmi Note 13 4G/ Xiaomi Redmi Note 14 4G/ Xiaomi Poco M7 Pro 5G</b>", "height": 159.5, "width": 73, "photo_path": "photos/xi_note_13.png"},

    {"model": "<b>Xiaomi Mi 10T 5G/ Xiaomi Mi 10T Pro 5G/ Xiaomi Redmi K30s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.75мм \nНижняя часть - 4мм \nБоковая рамка - 1.6мм", "height": 160.5, "width": 73, "photo_path": "photos/xiaomi mi10t.png"},

    {"model": "<b>Xiaomi 11T/ Xiaomi 11T Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.37мм \nНижняя часть - 4.5мм \nБоковая рамка - 1.83мм", "height": 159.5, "width": 72.5, "photo_path": "photos/xiaomi 11t.png"},

    # {"model": "Xiaomi Black Shark 4", "height": 155, "width": 71},
    # {"model": "Xiaomi Black Shark 4 Pro", "height": 155, "width": 71},
    # {"model": "Xiaomi Black Shark 5", "height": 155, "width": 71},
    # {"model": "Xiaomi Black Shark 5 Pro", "height": 155, "width": 71},
    #
    # {"model": "Xiaomi Poco F4 GT", "height": 155, "width": 71},
    # {"model": "Xiaomi Poco F4 Game", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi K50", "height": 155, "width": 71},
    # {"model": "Xiaomi Redmi K60E", "height": 155, "width": 71},

    {"model": "<b>Xiaomi 12T/ Xiaomi 12T Pro/ Xiaomi Redmi K50 Ultra</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 2.2мм \nБоковая рамка - 1.6мм", "height": 159, "width": 73.5, "photo_path": "photos/xiaomi 12t.png"},

    {"model": "<b>Honor 10 Lite/ Honor 10i/ Honor 20i/ Honor 20e</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.3мм \nНижняя часть - 4.63мм \nБоковая рамка - 1.65мм", "height": 150, "width": 69.5, "photo_path": "photos/honor 10i.png"},

    {"model": "<b>Honor 20/ Honor 20 Pro/ Huawei Nova 5T</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 4.3мм \nБоковая рамка - 1.8мм", "height": 156.5, "width": 73, "photo_path": "photos/honor 20.png"},

    # {"model": "Honor 30", "height": 155, "width": 71},
    #
    # {"model": "Honor 30 Pro Plus", "height": 155, "width": 71},
    #
    # {"model": "Honor 6", "height": 155, "width": 71},
    #
    # {"model": "Honor 6 Plus", "height": 155, "width": 71},
    #
    # {"model": "Honor 7", "height": 155, "width": 71},

    {"model": "<b>Honor 8c/ Asus Zenfone Max 2</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.45мм \nНижняя часть - 7.68мм \nБоковая рамка - 1.8мм", "height": 154.5, "width": 72.5, "photo_path": "photos/honor 8c.png"},

    {"model": "<b>Honor 8</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13мм \nНижняя часть - 14.3мм \nБоковая рамка - 1.36мм", "height": 142, "width": 67.5},

    # {"model": "Honor 8 Pro", "height": 155, "width": 71},

    {"model": "<b>Honor 8x/ Honor 9X Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.95мм \nНижняя часть - 4.18мм \nБоковая рамка - 1.85мм", "height": 156.5, "width": 79, "photo_path": "photos/honor 8x.png"},

    {"model": "<b>Honor 9a/ huawei Y6p</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.25мм \nНижняя часть - 6.36мм \nБоковая рамка - 1.98мм", "height": 155, "width": 70, "photo_path": "photos/huawei y6p.png"},

    # {"model": "Honor 9", "height": 155, "width": 71},

    {"model": "<b>Honor Play</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.7мм \nНижняя часть - 6.7мм \nБоковая рамка - 1.9мм", "height": 154.5, "width": 71, "photo_path": "photos/honor play.png"},

    {"model": "<b>Huawei Y8p/ Honor 30i/ Huawei Enjoy 10s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.58мм \nНижняя часть - 5.4мм \nБоковая рамка - 2.0мм", "height": 153.5, "width": 69, "photo_path": "photos/huawei y8p.png"},

    {"model": "<b>Huawei Y9s/ Huawei P Smart Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 4.12мм \nБоковая рамка - 1.5мм", "height": 158.5, "width": 73.5, "photo_path": "photos/huawei y9s.png"},

    # {"model": "Huawei Mate 10", "height": 155, "width": 71},

    {"model": "<b>Huawei Mate 20</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3мм \nНижняя часть - 3.3мм \nБоковая рамка - 1.6мм", "height": 156, "width": 75.5, "photo_path": "photos/huawei mate 20.png"},

    {"model": "<b>Huawei Mate 20 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.23мм \nНижняя часть - 5.4мм \nБоковая рамка - 1.6мм", "height": 153.5, "width": 71, "photo_path": "photos/huawei mate 20 lite.png"},

    {"model": "<b>Huawei Mate 9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 10.75мм \nНижняя часть - 13.8мм \nБоковая рамка - 1.5мм", "height": 154, "width": 76, "photo_path": "photos/huawei mate 9.png"},

    # {"model": "Huawei MediaPad T3 7.0", "height": 155, "width": 71},
    #
    # {"model": "Huawei MediaPad T5 10.1", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova 2", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova 2 Plus", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova 3", "height": 155, "width": 71},
    # {"model": "Huawei Nova 3i", "height": 155, "width": 71},

    {"model": "<b>Huawei Nova</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.5мм \nНижняя часть - 14.8мм \nБоковая рамка - 2.13мм", "height": 138, "width": 66, "photo_path": "photos/huawei nova.png"},

    # {"model": "Huawei Nova Lite", "height": 155, "width": 71},

    {"model": "<b>Huawei P10</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 14.4мм \nНижняя часть - 15.3мм \nБоковая рамка - 1.55мм", "height": 142, "width": 66, "photo_path": "photos/huawei p10.png"},

    {"model": "<b>Huawei P10 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.2мм \nНижняя часть - 14.8мм \nБоковая рамка - 2мм", "height": 143, "width": 68.5, "photo_path": "photos/huawei p10 lite.png"},

    # {"model": "Huawei P10 Plus", "height": 155, "width": 71},

    {"model": "<b>Huawei P20</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 9.2мм \nБоковая рамка - 1.4мм", "height": 145.5, "width": 67.5, "photo_path": "photos/huawei p20.png"},

    {"model": "<b>Huawei P20 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.9мм \nНижняя часть - 9.3мм \nБоковая рамка - 1.6мм", "height": 152.5, "width": 71},

    {"model": "<b>Huawei P30</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.7мм \nНижняя часть - 3.4мм \nБоковая рамка - 1.8мм", "height": 147, "width": 68.5, "photo_path": "photos/huawei p30.png"},

    {"model": "<b>Huawei P30 Lite/ Honor 20s/ Honor 20 lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.3мм \nНижняя часть - 4.65мм \nБоковая рамка - 1.6мм", "height": 148.5, "width": 69.5, "photo_path": "photos/huawei p30 lite.png"},

    {"model": "<b>Huawei P40</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.93мм \nНижняя часть - 3мм \nБоковая рамка - 1.9мм", "height": 146, "width": 69, "photo_path": "photos/huawei p40.png"},

    {"model": "<b>Huawei P40 Lite 4G/ Huawei Nova 6 SE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.86мм \nНижняя часть - 4.75мм \nБоковая рамка - 1.95мм", "height": 154, "width": 72.5, "photo_path": "photos/huawei p40 lite.png"},

    # {"model": "Huawei P8", "height": 155, "width": 71},

    {"model": "<b>Huawei P9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 12.7мм \nНижняя часть - 14мм \nБоковая рамка - 1.4мм", "height": 141.5, "width": 67, "photo_path": "photos/huawei p9.png"},

    {"model": "<b>Huawei P9 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 13.3мм \nНижняя часть - 15.3мм \nБоковая рамка - 1.88мм", "height": 143, "width": 68.5, "photo_path": "photos/huawei p9 lite.png"},

    # {"model": "Huawei P9 Plus", "height": 155, "width": 71},

    {"model": "<b>Huawei P Smart 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.25мм \nНижняя часть - 5.3мм \nБоковая рамка - 1.8мм", "height": 151, "width": 70, "photo_path": "photos/huawei p smart 2019.png"},

    {"model": "<b>Huawei P Smart Z/ Honor 9X/ Huawei Y9 Prime 2019</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.63мм \nНижняя часть - 4.67мм \nБоковая рамка - 1.8мм", "height": 159, "width": 73.5, "photo_path": "photos/huawei p smart z.png"},

    # {"model": "Huawei View 10", "height": 155, "width": 71},
    #
    # {"model": "Huawei View 20", "height": 155, "width": 71},
    # {"model": "Huawei Nova 4", "height": 155, "width": 71},

    {"model": "<b>Huawei Y7/ Huawei Y7 Prime/ Huawei Y7 2017/ Huawei Nova Lite Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 12.9мм \nНижняя часть - 16мм \nБоковая рамка - 2мм", "height": 150, "width": 72.5, "photo_path": "photos/huawei y7.png"},

    {"model": "<b>Huawei P40 Lite E/ Honor Play 3/ Honor 9C/ Huawei Y7p</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 5.87мм \nБоковая рамка - 2мм", "height": 156, "width": 72, "photo_path": "photos/huawei p40 lite e.png"},

    # {"model": "Huawei MatePad 4 10.4", "height": 155, "width": 71},
    # {"model": "Huawei MatePad 4 10.4 5G", "height": 155, "width": 71},
    #
    # {"model": "Huawei MatePad T10 9.7", "height": 155, "width": 71},
    #
    # {"model": "Huawei MatePad T8 8.0", "height": 155, "width": 71},
    # {"model": "Honor Pad X7", "height": 155, "width": 71},

    {"model": "<b>Honor 10X Lite/ Huawei P Smart 2021/ Huawei Y7a 2020</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.38мм \nНижняя часть - 4.6мм \nБоковая рамка - 2мм", "height": 161.5, "width": 73.5, "photo_path": "photos/huawei p smart 2021.png"},

    {"model": "<b>Honor 30s/ Huawei P40 Lite 5G/ Huawei Nova 7 SE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 4.9мм \nБоковая рамка - 2.0мм", "height": 158, "width": 71.5, "photo_path": "photos/honor 30s.png"},

    # {"model": "Honor X9a", "height": 155, "width": 71},
    # {"model": "Honor X40", "height": 155, "width": 71},
    # {"model": "Honor Magic 5 Lite", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova 6", "height": 155, "width": 71},
    #
    # {"model": "Huawei MediaPad M3 Lite 8.0", "height": 155, "width": 71},
    #
    # {"model": "Huawei MediaPad M5 Lite 8.0", "height": 155, "width": 71},

    {"model": "<b>Honor X8/ Honor x8a/ Honor X30i/ Honor X40i/ Honor X50i/ Huawei Nova 12i/ Huawei Nova 13i/ Huawei Nova Y90/ Honor 90 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.65мм \nНижняя часть - 4.3мм \nБоковая рамка - 1.2мм", "height": 160.5, "width": 72.5, "photo_path": "photos/honor x8.png"},

    {"model": "<b>Huawei Nova Y91</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 7.6мм \nНижняя часть - 11мм \nБоковая рамка - 7.6мм", "height": 173, "width": 82, "photo_path": "photos/huawei nova y91.png"},

    {"model": "<b>Honor X9/ Honor X9 5G/ Honor X30/ Honor Magic 4 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.17мм \nНижняя часть - 4.7мм \nБоковая рамка - 1.24мм", "height": 163, "width": 73.5, "photo_path": "photos/honor x9.png"},

    {"model": "<b>Honor 50 SE/ Huawei Nova 9 SE/ Huawei Nova 10 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 0.7мм \nНижняя часть - 3.14мм \nБоковая рамка - 0.7мм", "height": 161.5, "width": 73, "photo_path": "photos/honor 50se.png"},

    {"model": "<b>Honor X7/ Honor X7a/ Honor X7a Plus/ Huawei Nova Y70/ Huawei Nova Y70 Plus/ Huawei Nova Y71</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 5.3мм \nБоковая рамка - 2.0мм", "height": 164, "width": 74.5, "photo_path": "photos/honor x7.png"},

    # {"model": "Huawei Nova 10 SE", "height": 155, "width": 71},

    {"model": "<b>Honor X6/ Honor X6s/ Honor X6a/ Honor X5 Plus/ Honor X8 5G/ Honor 70 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 160, "width": 72, "photo_path": "photos/honor x6.png"},

    {"model": "<b>Honor X6c</b>", "height": 161, "width": 72.5, "photo_path": "photos/honor x6.png"},

    {"model": "<b>Honor X7b / Honor X7c / Honor 90 Smart / Honor 200 Smart 5G</b>", "height": 164, "width": 74, "photo_path": "photos/honor x7b.png"},

    {"model": "<b>Honor X8b / Honor X8c / Honor 200 lite</b>", "height": 159, "width": 72.5, "photo_path": "photos/honor x8b.png"},

    # {"model": "Huawei MatePad SE", "height": 155, "width": 71},
    #
    # {"model": "Huawei MatePad 11 2021", "height": 155, "width": 71},
    # {"model": "Huawei MatePad 11 2023", "height": 155, "width": 71},
    #
    # {"model": "Huawei MatePad Pro 11 2022", "height": 155, "width": 71},

    {"model": "<b>Honor Pad X8 10.1/ Huawei MatePad T10s 10.1</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.63мм \nНижняя часть - 2.38мм \nБоковая рамка - 1.4мм", "height": 154, "width": 71.5},

    {"model": "<b>Honor Pad 8 12.0</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 7.5мм \nНижняя часть - 7.5мм \nБоковая рамка - 7.5мм", "height": 171, "width": 270.5},

    {"model": "<b>Huawei P50</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.63мм \nНижняя часть - 2.38мм \nБоковая рамка - 1.4мм", "height": 154, "width": 71.5},

    # {"model": "Huawei P60", "height": 155, "width": 71},
    #
    {"model": "Huawei Nova 11 / Huawei Nova 12s / Huawei Nova 13", "height": 159, "width": 73, "photo_path": "photos/honor x6c.png"},
    #
    # {"model": "Huawei Nova 11i", "height": 155, "width": 71},
    #
    # {"model": "Huawei Y9 2019", "height": 155, "width": 71},
    # {"model": "Huawei Y8s", "height": 155, "width": 71},

    {"model": "<b>Huawei Mate 50/ Huawei Mate 50e</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.73мм \nНижняя часть - 2.2мм \nБоковая рамка - 1.6мм", "height": 159.5, "width": 74, "photo_path": "photos/mate 50e.png"},

    # {"model": "Huawei P40", "height": 155, "width": 71},
    # {"model": "Huawei P40 5G", "height": 155, "width": 71},
    #
    # {"model": "Honor Play 4", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova Y60", "height": 155, "width": 71},
    #
    # {"model": "Huawei Nova Y61", "height": 155, "width": 71},
    #
    #
    # {"model": "OPPO A3s", "height": 155, "width": 71},
    # {"model": "OPPO A5", "height": 155, "width": 71},
    # {"model": "OPPO Ax5", "height": 155, "width": 71},
    #
    # {"model": "OPPO A83", "height": 155, "width": 71},
    #
    # {"model": "OPPO F5", "height": 155, "width": 71},
    #
    # {"model": "OPPO R17", "height": 155, "width": 71},
    # {"model": "OPPO R17 Pro", "height": 155, "width": 71},
    # {"model": "OPPO Rx17 Neo", "height": 155, "width": 71},
    # {"model": "OPPO Rx17 Pro", "height": 155, "width": 71},

    {"model": "<b>Realme 6 Pro/ Realme X50</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.36мм \nНижняя часть - 5.2мм \nБоковая рамка - 1.6мм", "height": 160, "width": 72, "photo_path": "photos/realme 6 pro.png"},

    # {"model": "Vivo V17", "height": 155, "width": 71},
    # {"model": "Vivo V17 NEO", "height": 155, "width": 71},
    #
    # {"model": "Oppo A91", "height": 155, "width": 71},
    # {"model": "Oppo Reno 3", "height": 155, "width": 71},
    # {"model": "Oppo a73", "height": 155, "width": 71},
    #
    # {"model": "Oppo Reno 2Z", "height": 155, "width": 71},
    # {"model": "Oppo Reno 2F", "height": 155, "width": 71},
    # {"model": "Oppo K3", "height": 155, "width": 71},
    #
    # {"model": "Realme X3", "height": 155, "width": 71},
    # {"model": "Realme X3 SuperZoom", "height": 155, "width": 71},
    # {"model": "Realme X50 Pro", "height": 155, "width": 71},
    #
    # {"model": "Realme XT", "height": 155, "width": 71},
    # {"model": "Realme X2", "height": 155, "width": 71},
    #
    # {"model": "Realme X2 Pro", "height": 155, "width": 71},
    # {"model": "OnePlus 7T", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 8", "height": 155, "width": 71},
    # {"model": "Oppo Reno 3 Pro", "height": 155, "width": 71},

    {"model": "<b>Oppo A52/A72/A73 5G/A74 5G/  Realme 6/6S/7 4G/7 5G/8 5G/8S 5G/Narzo 20 Pro/Narzo 30/Narzo 30 5G/Narzo 30 Pro/Narzo 50</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.34мм \nНижняя часть - 5.2мм \nБоковая рамка - 1.5мм", "height": 158, "width": 71, "photo_path": "photos/realme 7.png"},

    {"model": "<b>Oppo A5 2020/A9 2020/A11/A11x/A31/A15/A15s/A16/A55 5G/A55s/  Realme 5/5i/6i/C3/C11/C15/C21Y/C25/C25S/C25Y/Narzo 30A/Narzo 10/Narzo 10A/Narzo 20/Narzo 20A/Narzo 50</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 6.35мм \nБоковая рамка - 1.73мм", "height": 160, "width": 72},

    {"model": "<b>Oppo A12/ Oppo A12s/ Oppo A5s/ Oppo A7/ Realme 3/ Realme 3i</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.1мм \nНижняя часть - 6.75мм \nБоковая рамка - 1.68мм", "height": 152, "width": 71.5, "photo_path": "photos/realme 3.png"},

    {"model": "<b>Oppo Reno 5/5 Lite/6/6 Lite/7/ Oppo A74 4G/ Realme 7 pro/8/8pro/X7/GT/GT Neo/GT Neo 2t/Q2 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 3.85мм \nБоковая рамка - 1.4мм", "height": 155, "width": 70, "photo_path": "photos/realme gt.png"},

    # {"model": "Oppo Reno 5 Pro", "height": 155, "width": 71},
    #
    # {"model": "Oppo A32 2020", "height": 155, "width": 71},
    # {"model": "Oppo A33 2020", "height": 155, "width": 71},
    # {"model": "Oppo A53", "height": 155, "width": 71},
    # {"model": "Oppo A54", "height": 155, "width": 71},
    # {"model": "Oppo A55", "height": 155, "width": 71},
    # {"model": "Realme 7i", "height": 155, "width": 71},
    # {"model": "Realme C17", "height": 155, "width": 71},
    # {"model": "OnePlus Nord N100", "height": 155, "width": 71},

    {"model": "<b>Realme 9/ Realme 9 Pro Plus/ Realme 10</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.69мм \nНижняя часть - 5.46мм \nБоковая рамка - 1.26мм", "height": 156, "width": 70},

    # {"model": "Oppo A3", "height": 155, "width": 71},
    # {"model": "Oppo F7", "height": 155, "width": 71},
    #
    # {"model": "Realme GT2", "height": 155, "width": 71},
    # {"model": "Realme GT Neo 2", "height": 155, "width": 71},
    # {"model": "Oppo K10 Pro", "height": 155, "width": 71},
    # {"model": "Oppo Reno 8 Pro", "height": 155, "width": 71},
    # {"model": "OnePlus 9RT", "height": 155, "width": 71},
    #
    # {"model": "Realme 10 Pro Plus", "height": 155, "width": 71},
    #
    # {"model": "Realme Pad 10.4", "height": 155, "width": 71},
    #
    # {"model": "Realme Pad mini", "height": 155, "width": 71},
    #
    # {"model": "Oppo Reno 8T", "height": 155, "width": 71},

    {"model": "<b>Realme C55</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.04мм \nНижняя часть - 4.05мм \nБоковая рамка - 1мм", "height": 161, "width": 72, "photo_path": "photos/realme c55.png"},

    # {"model": "Realme 11 Pro", "height": 155, "width": 71},
    # {"model": "Realme 11 Pro Plus", "height": 155, "width": 71},

    {"model": "<b>Realme C35/ Realme Narzo 50A Prime</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.4мм \nНижняя часть - 6.64мм \nБоковая рамка - 1.6мм", "height": 160.5, "width": 72, "photo_path": "photos/realme c35.png"},

    {"model": "<b>Realme C53</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 5.2мм \nБоковая рамка - 1.5мм", "height": 164, "width": 74, "photo_path": "photos/realme c53.png"},

    # {"model": "Realme C11 2021", "height": 155, "width": 71},
    # {"model": "Realme C20", "height": 155, "width": 71},
    # {"model": "Realme C21", "height": 155, "width": 71},
    # {"model": "Realme Narzo 50i", "height": 155, "width": 71},

    {"model": "<b>Realme 8i/ Realme 9 5G/ Realme 9i/ Realme 9i 5G/ Realme 9 Pro/ Oppo A96</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.68мм \nНижняя часть - 6.84мм \nБоковая рамка - 1.95мм", "height": 160, "width": 72, "photo_path": "photos/realme 9i.png"},

    {"model": "<b>Realme 5 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.9мм \nНижняя часть - 5.11мм \nБоковая рамка - 1.62мм", "height": 152.5, "width": 70.5, "photo_path": "photos/realme 5 pro.png"},

    # {"model": "Realme X4 GT", "height": 155, "width": 71},

    {"model": "Poco X4 GT", "height": 160, "width": 71, "photo_path": "photos/poco x4 gt.png"},

    {"model": "<b>Realme 10 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.0мм \nНижняя часть - 4.0мм \nБоковая рамка - 1.0мм", "height": 161, "width": 72, "photo_path": "photos/realme 10 pro.png"},

    {"model": "Xiaomi 13T", "height": 159.5, "width": 73.5, "photo_path": "photos/xiaomi 13t.png"},

    {"model": "Xiaomi 14", "height": 151, "width": 69.5, "photo_path": "photos/xiaomi 14.png"},

    {"model": "Poco F7", "height": 160.5, "width": 75.5, "photo_path": "photos/poco f7.png"},

    # {"model": "Oppo A17", "height": 155, "width": 71},
    # {"model": "Oppo A17K", "height": 155, "width": 71},
    # {"model": "Oppo A57s", "height": 155, "width": 71},

    {"model": "<b>Realme C30/ Realme C30s/ Realme C31/ Realme C33/ Realme Narzo 50i Prime</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.75мм \nНижняя часть - 6.7мм \nБоковая рамка - 1.8мм", "height": 160.5, "width": 72, "photo_path": "photos/realme c30.png"},

    # {"model": "Asus Zenfone 3 Max (ZC520TL)", "height": 155, "width": 71},
    #
    # {"model": "Asus Zenfone 4 Selfie Pro (ZD552KL)", "height": 155, "width": 71},
    #
    # {"model": "Asus ZenFone 5 (ZE620KL)", "height": 155, "width": 71},
    #
    # {"model": "Asus ZenFone Max Pro (ZB602KL)", "height": 155, "width": 71},
    #
    # {"model": "Asus Zenfone 4 Max Pro (ZC554KL)", "height": 155, "width": 71},
    #
    # {"model": "Asus ROG Phone 5", "height": 155, "width": 71},
    # {"model": "Asus ROG Phone 5s", "height": 155, "width": 71},
    #
    # {"model": "Asus ZenFone 7 (ZS670KS)", "height": 155, "width": 71},
    # {"model": "Asus ZenFone 7 Pro (ZS671KS)", "height": 155, "width": 71},
    #
    # {"model": "Asus ZenFone Max Pro M2 (ZB631KL)", "height": 155, "width": 71},
    #
    # {"model": "Asus ROG Phone 3 (ZS661KS)", "height": 155, "width": 71},
    # {"model": "Asus ROG Phone 11 II (ZS660KL)", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 3", "height": 155, "width": 71},
    # {"model": "OnePlus 3T", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 5", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 5T", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 6", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 6T", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 7 Pro", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 7", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 9 Pro", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 7t", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 8 pro", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 10 pro", "height": 155, "width": 71},
    # {"model": "OnePlus 11", "height": 155, "width": 71},
    # {"model": "Oppo Find X5 Pro", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Ace", "height": 155, "width": 71},
    # {"model": "OnePlus 10T", "height": 155, "width": 71},
    # {"model": "OnePlus 10R", "height": 155, "width": 71},
    # {"model": "OnePlus Ace Pro 10T", "height": 155, "width": 71},
    # {"model": "Realme GT Neo 3", "height": 155, "width": 71},
    # {"model": "Oppo Reno 8 Pro Plus", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Nord 2", "height": 155, "width": 71},
    # {"model": "OnePlus Nord 2T", "height": 155, "width": 71},
    # {"model": "OnePlus Nord CE 5G", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Nord CE 2 Lite", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Nord N10", "height": 155, "width": 71},
    # {"model": "OnePlus Nord N10 5G", "height": 155, "width": 71},
    # {"model": "OnePlus Nord N200", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Nord CE 2 5G", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 8T", "height": 155, "width": 71},
    # {"model": "OnePlus 9", "height": 155, "width": 71},
    # {"model": "OnePlus 9R", "height": 155, "width": 71},
    # {"model": "OnePlus 9T", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Nord CE2 5G", "height": 155, "width": 71},
    #
    # {"model": "OnePlus 10RT", "height": 155, "width": 71},
    #
    # {"model": "OnePlus Ace Pro 12", "height": 155, "width": 71},
    #
    # {"model": "Vivo NEX (1805)", "height": 155, "width": 71},
    #
    # {"model": "Vivo Nex 3 (1912)", "height": 155, "width": 71},
    #
    # {"model": "Vivo V11", "height": 155, "width": 71},
    # {"model": "Vivo V11i", "height": 155, "width": 71},
    # {"model": "Vivo Y97", "height": 155, "width": 71},
    #
    # {"model": "Vivo V15", "height": 155, "width": 71},
    #
    # {"model": "Vivo V15 Pro", "height": 155, "width": 71},
    #
    # {"model": "Vivo Y81", "height": 155, "width": 71},

    {"model": "<b>Vivo Y85/ Vivo V9/ Vivo V9 Youth</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.0мм \nНижняя часть - 5.8мм \nБоковая рамка - 1.8мм", "height": 151.5, "width": 71.5, "photo_path": "photos/vivo y85.png"},

    {"model": "<b>Vivo Y1s/ Vivo Y90/ Vivo Y91/ Vivo Y91C/ Vivo Y91i/ Vivo Y93/ Vivo Y93 lite/ Vivo Y95</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.45мм \nНижняя часть - 6.33мм \nБоковая рамка - 1.8мм", "height": 155.5, "width": 71.5, "photo_path": "photos/vivo y91.png"},

    {"model": "<b>Vivo Y3/ Vivo Y11/ Vivo Y12/ Vivo Y15/ Vivo Y17</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.44мм \nНижняя часть - 6.45мм \nБоковая рамка - 1.78мм", "height": 155.5, "width": 72, "photo_path": "photos/vivo y17.png"},

    # {"model": "Vivo Y30", "height": 155, "width": 71},
    #
    # {"model": "Vivo Y19", "height": 155, "width": 71},
    #
    # {"model": "Vivo X50", "height": 155, "width": 71},

    {"model": "<b>Vivo Y12i/ Vivo Y12a/ Vivo Y20s/ Vivo Y12s/ Vivo Y16/ Vivo Y20i/ Vivo Y20/ Vivo Y30G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.9мм \nНижняя часть - 4.8мм \nБоковая рамка - 1.5мм", "height": 160, "width": 72, "photo_path": "photos/vivo y20.png"},

    # {"model": "Vivo X21", "height": 155, "width": 71},
    # {"model": "Vivo X21UD", "height": 155, "width": 71},

    {"model": "<b>Vivo V21/ Vivo V23e/ Vivo V25/ Vivo V25e</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 3.9мм \nБоковая рамка - 1.65мм", "height": 155.5, "width": 70.5, "photo_path": "photos/vivo v21.png"},

    {"model": "<b>Vivo V20</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 5.3мм \nБоковая рамка - 1.7мм", "height": 156.5, "width": 70.5},

    {"model": "<b>Vivo V21E</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.5мм \nНижняя часть - 5.4мм \nБоковая рамка - 2.0мм", "height": 157, "width": 70.5},

    {"model": "<b>Vivo T2</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.47мм \nНижняя часть - 6.0мм \nБоковая рамка - 1.5мм", "height": 160.5, "width": 73, "photo_path": "photos/vivo t2.png"},

    {"model": "<b>Vivo T1 (Snapdragon 680)/ Vivo V20SE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.47мм \nНижняя часть - 5.1мм \nБоковая рамка - 1.8мм", "height": 156.5, "width": 70.5, "photo_path": "photos/vivo v20se.png"},

    {"model": "<b>Vivo y72 5g/ Vivo y15s/ Vivo y31/ Vivo y31s/ Vivo y33/ Vivo y33s/ Vivo y35/ Vivo y52s/ Vivo y53s/ Vivo t1 5g</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.9мм \nНижняя часть - 4.8мм \nБоковая рамка - 1.5мм", "height": 160, "width": 72, "photo_path": "photos/vivo y53s.png"},

    # {"model": "Vivo V23 5G", "height": 155, "width": 71},

    {"model": "<b>Vivo V17 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.0мм \nНижняя часть - 3.4мм \nБоковая рамка - 1.6мм", "height": 154.5, "width": 71},

    {"model": "<b>Vivo Y22/ Vivo Y22s</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 5мм \nБоковая рамка - 1.5мм", "height": 160, "width": 72},

    # {"model": "Vivo Y02", "height": 155, "width": 71},

    {"model": "<b>Vivo V27e</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.9мм \nНижняя часть - 3.5мм \nБоковая рамка - 1.6мм", "height": 159, "width": 72.5, "photo_path": "photos/vivo v27e.png"},

    {"model": "<b>Tecno Spark 5 Air/ Tecno Spark 6 Air/ Tecno Pouvoir 4/ Tecno Pouvoir 4 Pro/ Tecno Spark Power 2</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.4мм \nНижняя часть - 5.75мм \nБоковая рамка - 1.5мм", "height": 170.5, "width": 75, "photo_path": "photos/tecno spark air 5.png"},

    # {"model": "Tecno Spark 8P", "height": 155, "width": 71},

    {"model": "<b>Tecno Camon 18 Premier/ Infinix Zero X/ Infinix Zero X Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2мм \nНижняя часть - 3.84мм \nБоковая рамка - 1.46мм", "height": 161, "width": 73, "photo_path": "photos/infinix zero x.png"},

    {"model": "<b>Tecno Pova Neo/ Tecno Spark 7P/ Infinix Hot 10s/ Infinix Hot 11/ Infinix Hot 10 Play/ Infinix Hot 11 Play</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.29мм \nНижняя часть - 5.73мм \nБоковая рамка - 1.56мм", "height": 167.5, "width": 73.5, "photo_path": "photos/infinix hot 11.png"},

    {"model": "<b>Tecno Pova 4/ Tecno Pova Neo 2/ Infinix Hot 12 Play/ Infinix Note 12i</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.52мм \nНижняя часть - 5.41мм \nБоковая рамка - 1.81мм", "height": 166.5, "width": 73.5, "photo_path": "photos/infinix hot 12 play.png"},

    {"model": "<b>Tecno Pova 2/ Tecno Pova 3/ Infinix Note 10/ Infinix Note 10 Pro/ Infinix Note 11 Pro/ Infinix Note 11s/ Infinix Note 11i</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.12мм \nНижняя часть - 4.76мм \nБоковая рамка - 1.51мм", "height": 169, "width": 74.5, "photo_path": "photos/infinix note 10.png"},

    {"model": "<b>Tecno Camon 17P/ Tecno Camon 17 Pro/ Tecno Camon 18/ Tecno Camon 18P/ Tecno Camon 18T/ Tecno Pova Neo 5G/ Tecno Spark 8 Pro/ Infinix Hot 11s/ Infinix Zero X Neo/ Infinix Zero 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.0мм \nНижняя часть - 4.0мм \nБоковая рамка - 1.55мм", "height": 161, "width": 73, "photo_path": "photos/infinix hot 11s.png"},

    {"model": "<b>Infinix Note 11/ Infinix Note 12 4G/ Infinix Note 12 5G/ Infinix Note 12 Pro 5G/ Infinix Note 12i 2022/ Infinix Note 12 2023/ Infinix Note 30i 2023/ Infinix Zero 20/ Tecno Pova 4 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.75мм \nНижняя часть - 4.2мм \nБоковая рамка - 1.97мм", "height": 161, "width": 73, "photo_path": "photos/infinix note 11.png"},

    {"model": "<b>Infinix Hot 12i/ Infinix 12 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.52мм \nНижняя часть - 5.31мм \nБоковая рамка - 1.72мм", "height": 166.5, "width": 73.5},

    # {"model": "Tecno Spark 3", "height": 155, "width": 71},
    # {"model": "Tecno Camon 11", "height": 155, "width": 71},

    {"model": "<b>Tecno Camon 15/ Tecno Camon 15 Air/ Tecno Spark 5/ Tecno Spark 5 Pro/ Infinix Note 7 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.95мм \nНижняя часть - 6.25мм \nБоковая рамка - 1.98мм", "height": 160.5, "width": 72.5, "photo_path": "photos/tecno spark 5.png"},

    # {"model": "Tecno Spark 6 Go", "height": 155, "width": 71},
    # {"model": "Tecno Spark Go 2020", "height": 155, "width": 71},
    #
    # {"model": "Tecno Pop 5 LTE", "height": 155, "width": 71},

    {"model": "<b>Tecno Camon 19/ Tecno Camon 19 Pro/ Tecno Camon 19 Pro 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.15мм \nНижняя часть - 4.22мм \nБоковая рамка - 1.1мм", "height": 163, "width": 71.5, "photo_path": "photos/tecno camon 19.png"},

    # {"model": "Tecno Camon 19 Neo", "height": 155, "width": 71},

    {"model": "<b>Infinix Smart 6 Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.65мм \nНижняя часть - 5.87мм \nБоковая рамка - 1.64мм", "height": 167.5, "width": 73.5, "photo_path": "photos/infinix smart 6 plus.png"},

    {"model": "<b>Tecno Spark 7/ Tecno Spark 8C/ Tecno Spark GO 2022/ Tecno Pop 6 Pro/ Infinix Smart 6/ Infinix Smart 6 HD</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.46мм \nНижняя часть - 6.24мм \nБоковая рамка - 1.54мм", "height": 160.5, "width": 72, "photo_path": "photos/tecno spark 8c.png"},

    {"model": "<b>Tecno Spark 4/ Tecno Spark 4 Air/ Infinix Hot 10 lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.82мм \nНижняя часть - 6.63мм \nБоковая рамка - 1.63мм", "height": 161.5, "width": 72, "photo_path": "photos/infinix hot 10 lite.png"},

    # {"model": "Infinix Note 7", "height": 155, "width": 71},

    # {"model": "Tecno Spark 3 Pro", "height": 155, "width": 71},

    {"model": "<b>Tecno Comon 16/ Tecno pova LD7/ Tecno Spark 6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.26мм \nНижняя часть - 6.02мм \nБоковая рамка - 1.6мм", "height": 166.5, "width": 73.5, "photo_path": "photos/tecno pova.png"},

    #
    # {"model": "Tecno Spark 4 Lite (KC8)", "height": 155, "width": 71},
    # {"model": "Tecno Camon 16 Pro", "height": 155, "width": 71},
    #
    # {"model": "Infinix Note 8", "height": 155, "width": 71},
    #
    # {"model": "Tecno Camon 15 Pro", "height": 155, "width": 71},

    {"model": "<b>Tecno Spark 9/ Tecno Spark 9 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.45мм \nНижняя часть - 7.25мм \nБоковая рамка - 1.56мм", "height": 161, "width": 72, "photo_path": "photos/tecno spark 9 pro.png"},

    # {"model": "Infinix Note 8i", "height": 155, "width": 71},
    #
    {"model": "<b>Infinix Hot 12/ Infinix Hot 20</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.52мм \nНижняя часть - 5.31мм \nБоковая рамка - 1.72мм", "height": 166.5, "width": 73.5, "photo_path": "photos/infinix hot 12.png"},

    {"model": "<b>Tecno Spark 10/ Tecno Spark 10C/ Tecno Pop 7</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.42мм \nНижняя часть - 5.66мм \nБоковая рамка - 1.6мм", "height": 161, "width": 72},

    {"model": "<b>Infinix Hot 20i</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.61мм \nНижняя часть - 5.8мм \nБоковая рамка - 2.15мм", "height": 160, "width": 72, "photo_path": "photos/infinix hot 20i.png"},

    # {"model": "Infinix Hot 30i", "height": 155, "width": 71},

    {"model": "<b>Infinix Note 30/ Infinix Hot 30/ Tecno Spark 10 Pro/ Tecno Pova 5</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.44мм \nНижняя часть - 4.9мм \nБоковая рамка - 1.64мм", "height": 165, "width": 73, "photo_path": "photos/infinix hot 30.png"},

    {"model": "<b>Infinix Hot 30 Play NFC</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.37мм \nНижняя часть - 5.9мм \nБоковая рамка - 1.73мм", "height": 166.5, "width": 73.5, "photo_path": "photos/infinix hot 30 play.png"},

    # {"model": "Lenovo K12 Pro", "height": 155, "width": 71},
    #
    # {"model": "Lenovo Tab M10 Plus (X606)", "height": 155, "width": 71},
    #
    # {"model": "Lenovo Tab M10 HD (X306)", "height": 155, "width": 71},
    #
    # {"model": "Lenovo Tab P11 (J606)", "height": 155, "width": 71},
    # {"model": "Lenovo Tab P11 Plus (J616)", "height": 155, "width": 71},
    # {"model": "Lenovo Tab P11 5G (J607)", "height": 155, "width": 71},
    #
    # {"model": "iPhone 11", "height": 155, "width": 71},
    #
    # {"model": "iPhone XR", "height": 155, "width": 71},
    #
    # {"model": "iPad Air 2 (A1566)", "height": 155, "width": 71},
    # {"model": "iPad Air 2 (A1567)", "height": 155, "width": 71},
    #
    # {"model": "iPad mini 4 (A1538)", "height": 155, "width": 71},
    # {"model": "iPad mini 4 (A1550)", "height": 155, "width": 71},
    #
    # {"model": "iPad Pro 10.5 2017 (A1701)", "height": 155, "width": 71},
    # {"model": "iPad Pro 10.5 2017 (A1709)", "height": 155, "width": 71},
    # {"model": "iPad Pro 10.5 2017 (A1852)", "height": 155, "width": 71},
    # {"model": "iPad Air 3 10.5 2019 (A2152)", "height": 155, "width": 71},
    # {"model": "iPad Air 3 10.5 2019 (A2123)", "height": 155, "width": 71},
    # {"model": "iPad Air 3 10.5 2019 (A2153)", "height": 155, "width": 71},
    # {"model": "iPad Air 3 10.5 2019 (A2154)", "height": 155, "width": 71},
    #
    # {"model": "iPad Pro 11 2018 (A1980)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2018 (A2013)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2018 (A1934)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2018 (A1979)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2020 (A2228)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2020 (A2068)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2020 (A2230)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2020 (A2231)", "height": 155, "width": 71},
    #
    # {"model": "iPad mini 5 (A2133)", "height": 155, "width": 71},
    # {"model": "iPad mini 5 (A2124)", "height": 155, "width": 71},
    # {"model": "iPad mini 5 (A2126)", "height": 155, "width": 71},
    # {"model": "iPad mini 5 (A2125)", "height": 155, "width": 71},
    #
    # {"model": "iPad Pro 9.7 (A1673)", "height": 155, "width": 71},
    # {"model": "iPad Pro 9.7 (A1674)", "height": 155, "width": 71},
    # {"model": "iPad Pro 9.7 (A1675)", "height": 155, "width": 71},
    #
    # {"model": "iPad Air 4 10.9 2020 (A2316)", "height": 155, "width": 71},
    # {"model": "iPad Air 4 10.9 2020 (A2324)", "height": 155, "width": 71},
    # {"model": "iPad Air 4 10.9 2020 (A2325)", "height": 155, "width": 71},
    # {"model": "iPad Air 4 10.9 2020 (A2072)", "height": 155, "width": 71},
    # {"model": "iPad Air 5 2022 (A2588)", "height": 155, "width": 71},
    # {"model": "iPad Air 5 2022 (A2589)", "height": 155, "width": 71},
    # {"model": "iPad Air 5 2022 (A2591)", "height": 155, "width": 71},
    #
    # {"model": "iPhone 13 Mini", "height": 155, "width": 71},
    #
    # {"model": "iPhone 13", "height": 155, "width": 71},
    # {"model": "iPhone 13 Pro", "height": 155, "width": 71},
    #
    # {"model": "iPhone 13 Pro Max", "height": 155, "width": 71},
    #
    # {"model": "iPhone 11 Pro", "height": 155, "width": 71},
    #
    # {"model": "iPhone 12 mini", "height": 155, "width": 71},
    #
    # {"model": "iPhone X", "height": 155, "width": 71},
    # {"model": "iPhone Xs", "height": 155, "width": 71},
    #
    # {"model": "iPhone Xs Max", "height": 155, "width": 71},
    #
    # {"model": "iPhone 6 Plus", "height": 155, "width": 71},
    #
    # {"model": "iPhone 6", "height": 155, "width": 71},
    #
    # {"model": "iPhone 6s Plus", "height": 155, "width": 71},
    #
    # {"model": "iPhone 6s", "height": 155, "width": 71},
    #
    # {"model": "iPhone 7", "height": 155, "width": 71},
    #
    # {"model": "iPhone 7 Plus", "height": 155, "width": 71},
    #
    # {"model": "iPhone 8 Plus", "height": 155, "width": 71},
    #
    # {"model": "iPhone 8", "height": 155, "width": 71},
    # {"model": "iPhone SE 2020", "height": 155, "width": 71},
    #
    # {"model": "iPhone 12", "height": 155, "width": 71},
    # {"model": "iPhone 12 Pro", "height": 155, "width": 71},
    #
    # {"model": "iPhone 11 Pro Max", "height": 155, "width": 71},
    #
    # {"model": "iPad Pro 11 2021 (A2301)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2021 (A2377)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2021 (A2459)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2021 (A2460)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2022 (A2435)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2022 (A2759)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2022 (A2761)", "height": 155, "width": 71},
    # {"model": "iPad Pro 11 2022 (A2762)", "height": 155, "width": 71},
    #
    # {"model": "iPhone 14", "height": 155, "width": 71},
    #
    # {"model": "iPhone 14 Pro", "height": 155, "width": 71},
    #
    # {"model": "iPhone 14 Pro Max", "height": 155, "width": 71},
    #
    # {"model": "iPhone 14 Plus", "height": 155, "width": 71},
    #
    # {"model": "iPad Pro 12.9 2021 (A2378)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2021 (A2379)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2021 (A2461)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2021 (A2462)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2022 (A2436)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2022 (A2437)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2022 (A2764)", "height": 155, "width": 71},
    # {"model": "iPad Pro 12.9 2022 (A2766)", "height": 155, "width": 71},
    #
    # {"model": "iPad mini 6 2021 (A2567)", "height": 155, "width": 71},
    # {"model": "iPad mini 6 2021 (A2568)", "height": 155, "width": 71},
    # {"model": "iPad mini 6 2021 (A2569)", "height": 155, "width": 71},
    #
    # {"model": "Phone 12 Pro Max", "height": 155, "width": 71},

    # {"model": "<b>Google Pixel 2</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel 2 XL</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel 3a</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel 3</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel 3 XL</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel XL</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>Google Pixel 4a 4g</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.8мм \nНижняя часть - 4.1мм \nБоковая рамка - 2.2мм", "height": 141, "width": 66.5, "photo_path": "photos/pixil 4a.png"},

    {"model": "<b>Google Pixel 5</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 1.5мм \nНижняя часть - 1.9мм \nБоковая рамка - 1.6мм", "height": 141.5, "width": 67.5, "photo_path": "photos/pixel 5.png"},

    {"model": "<b>Google Pixel 4</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.7мм \nНижняя часть - 3.6мм \nБоковая рамка - 1.3мм", "height": 143, "width": 65, "photo_path": "photos/pixel 4.png"},

    {"model": "<b>Google Pixel 4 XL</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 8.7мм \nНижняя часть - 1.2мм \nБоковая рамка - 3.6мм", "height": 156.5, "width": 71, "photo_path": "photos/pixel 4xl.png"},

    # {"model": "<b>Google Pixel 3a XL</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Google Pixel 5a</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>Google Pixel 6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.2мм \nНижняя часть - 3.5мм \nБоковая рамка - 2.0мм", "height": 154.5, "width": 71, "photo_path": "photos/pixel 6.png"},

    # {"model": "<b>Google Pixel 4a 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>Google Pixel 6a</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.45мм \nНижняя часть - 3.85мм \nБоковая рамка - 2.0мм", "height": 148.5, "width": 68.5, "photo_path": "photos/pixel 6a.png"},

    # {"model": "<b>Google Pixel 7 pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>Google Pixel 7</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 152.5, "width": 70, "photo_path": "photos/pixel 7.png"},

    # {"model": "<b>ZTE Blade A610</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade A6 Max</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade A910</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade V7 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade V9</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Nubia Z11</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Nubia Z11 max</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Nubia Z17 mini</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE V9 Vita</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>ZTE Blade A5 2020/ ZTE Blade A7 2020/ ZTE Blade A51 Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 3.33мм \nНижняя часть - 7.1мм \nБоковая рамка - 1.9мм", "height": 151, "width": 69, "photo_path": "photos/zte a7.png"},

    # {"model": "<b>ZTE Blade A7s 2020/ ZTE Blade 20 smart</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade A51/ ZTE Blade A71</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade V2020 Smart/ ZTE Blade V30 Vita</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade A31</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade V2020 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Blade V10</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>ZTE Nubia Red Magic 5G/ ZTE Nubia Red Magic 5S/ ZTE Nubia Red Magic 5G Lite</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    # {"model": "<b>ZTE Nubia Red Magic 6/ ZTE Nubia Red Magic 6s/ ZTE Nubia Red Magic 6 Pro/ ZTE Nubia Red Magic 6s Pro/ ZTE Nubia Red Magic 7</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>VSMART Joy 3/ VSMART Joy 3 plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>VSMART Joy 4</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    # {"model": "<b>Nokia 2.1 (TA-1080)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 2.3 (TA-1206)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 2 (TA-1029)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 3.1 Plus (TA-1104)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 3.1 (TA-1063)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 3 (TA-1032)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 5.1 Plus (TA-1105)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 5.1 (TA-1075)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 6.1 (TA-1043)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 6 (TA-1021)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 7 Plus (TA-1046)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 8.1 (TA-1119)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 3.4 (TA-1283)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia C20 (TA-1352)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia X20 (TA-1341)/ Nokia X10 (TA-1332)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 8.3 (TA-1243)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 6.2 TA-1198/ Nokia 7.2 (TA-1196)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 9 (TA-1087)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 2.4 (TA-1270)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia 1.4 (TA-1322)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia C1 Plus (TA-1312)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia G10 (TA-1334)/ Nokia G20 (TA-1336)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia XR20 (TA-1362)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia G50 (TA-1361)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia G21 (TA-1418)/ Nokia G11 (TA-1401)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia T20 (TA-1397)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Nokia T20 (TA-1397)</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    {"model": "<b>TCL 20Y/ TCL 20E</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 162, "width": 72, "photo_path": "photos/tcl 20y.png"},

    {"model": "<b>TCL 30XE/ TCL 30E/ TCL 20B/ TCL 20R 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.75мм \nНижняя часть - 6.8мм \nБоковая рамка - 1.67мм", "height": 161, "width": 72, "photo_path": "photos/tcl 20b.png"},

    {"model": "<b>TCL 30 Plus/ TCL 30 4G/ TCL 30 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.3мм \nНижняя часть - 3.7мм \nБоковая рамка - 1.55мм", "height": 161, "width": 73},

    # {"model": "<b>TCL 10L/ TCL Plex</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 10 Plus/ TCL 10 Pro</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 20S/ TCL 20 Pro 5G</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 20L/ TCL 20L Plus</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 20SE</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 205</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL 305/ TCL 306</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>TCL T610K/ TCL 40SE/ ZTE A1 Alpha Eco</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    #
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},
    # {"model": "<b>Honor X6</b> \nШирина закрашенной рамки стекла: \nВерхняя часть - 2.6мм \nНижняя часть - 6.7мм \nБоковая рамка - 2.0мм", "height": 100, "width": 10},

    # Другие элементы данных
]
