from view import view_map
from geocode import get_cord, get_ll_span


def main():
    toponym_to_find = input()
    if toponym_to_find:
        lat, lon = get_cord(toponym_to_find)
        ll_spn = f'll={lat},{lon}&spn=0.5,0.5'
        view_map(ll_spn, "map")

        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f'll={ll}&spn={spn}'
        view_map(ll_spn, "map")

        point_param = f'pt={ll}'
        view_map(ll_spn, "map", add_params=point_param)
    else:
        print("No toponym")


if __name__ == '__main__':
    main()