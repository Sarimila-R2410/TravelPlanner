from project import build_travel_map, get_shortest_path, display_travel_info


def test_build_travel_map():
    destinations = ['Loguetown', 'Alabasta']
    travel_info = [
        ('Loguetown', 'Alabasta', {'time': 150, 'mode': 'Ship', 'price': 20}),
    ]
    travel_map = build_travel_map(destinations, travel_info)
    assert 'Loguetown' in travel_map
    assert 'Alabasta' in travel_map
    assert travel_map['Loguetown'] == [('Alabasta', {'time': 150, 'mode': 'Ship', 'price': 20})]


def test_get_shortest_path():
    destinations = ['Loguetown', 'Alabasta', 'Skypiea']
    travel_info = [
        ('Loguetown', 'Alabasta', {'time': 150, 'mode': 'Ship', 'price': 20}),
        ('Alabasta', 'Skypiea', {'time': 200, 'mode': 'Airship', 'price': 50}),
    ]
    travel_map = build_travel_map(destinations, travel_info)
    path, time = get_shortest_path(travel_map, 'Loguetown', 'Skypiea')
    assert path == ['Loguetown', 'Alabasta', 'Skypiea']
    assert time == 350


def test_display_travel_info():
    travel_info = [
        ('Loguetown', 'Alabasta', {'time': 150, 'mode': 'Ship', 'price': 20}),
    ]
    table = display_travel_info(travel_info)
    assert "Loguetown" in table
    assert "Alabasta" in table
    assert "Ship" in table

