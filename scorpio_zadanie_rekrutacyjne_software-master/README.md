# Projekt Scorpio - zadanie rekrutacyjne do działu Software

Cześć! 
Miałam pewne wątpliwości co do sposobu obliczania prędkości kątowej w zadaniu 2. Jak sprawdzałam, co jest przesyłane przez topic /virtual_dc_motor/get_position to były to jedynie wartości 1, 0 i 4095, więc te ruchy były małe i kierunek prędkości często się zmieniał.
Swoje rozwiąznia napisałam w pythonie i są umieszczone w folderze scripts.
W zadaniu drugim nie wiedziałam do końca skąd mam wziąć docelową prędkość, skoro nie istniał żaden node przesyłający informacje na topic /virtual_dc_motor_controller/set_velocity_goal, jednak zachowałam dobrą strukturę i subscrybuję oraz publikuję informacje na odpowiednich topicach.
Alicja Bonar
