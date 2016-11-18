# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)

            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")
    return objects


def parse_star_parameters(line, star):

    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000  2 5 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    linestar=line.split( )
    star.R=float(linestar[1])
    star.color=linestar[2]
    star.m=float(linestar[3])
    star.x=float(linestar[4])
    star.y=float(linestar[5])
    star.Vx=float(linestar[6])
    star.Vy=float(linestar[7])






def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """


    linepl=line.split( )
    planet.R=float(linepl[1])
    planet.color=linepl[2]
    planet.m=float(linepl[3])
    planet.x=float(linepl[4])
    planet.y=float(linepl[5])
    planet.Vx=float(linepl[6])
    planet.Vy=float(linepl[7])




def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, '%s %d %s %f' % (obj.type, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy))

def save_statistic_to_file (output_filename,space_objects, dt):
     """Сохраняет сатистические данные о космических объектах в файл.
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
     for obj in space_objects:
        modul_Vx = obj.Vx
        modul_Vy = obj.Vy
        modul_s =((obj.Vx*dt)**2 +(obj.Vy*dt)**2)**0.5
     with open(output_filename, 'w') as out_file:
             print('%s %d %s %f' % (modul_Vx, modul_Vy, modul_s))



if __name__ == "__main__":
    print("This module is not for direct call!")
