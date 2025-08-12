import kiyotaka
import kiyotaka.api

def main():
    enums = [kiyotaka.api.PointExchange, kiyotaka.api.PointType]

    for enum in enums:
        print(enum)
        for e in enum:
            print(e.name, '=', e.value)

if __name__ == '__main__':
    main()
