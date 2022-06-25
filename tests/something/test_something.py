import pytest
from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses

import tables


@pytest.mark.parametrize('status', [
    # "ACTIVE",
    # "BANNED",
    # "DELETED",
    # "INACTIVE"
    *Statuses.list()

])
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance_value', [
    '100',
    '0',
    '-10',
    'asdd'

])
def test_something_balance(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'

])
def test_something_delete(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


def test_something_excange_localize(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        'localize', PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


def test_something_excange_localize_deep_into(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'state', 'country'],
        PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


@pytest.mark.parametrize('localizations, loc', [
    ('fr', 'fr_FR')
])
def test_something_excange_localizations(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_get_data_fields(get_db_session):
    data = get_db_session.query(tables.Films).first()
    print(data.title)


def test_try_to_delete_something(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.ItemType, (tables.ItemType.item_id == 3))


def test_try_to_add_testdata(get_db_session, get_add_method):
    new_item_type = {'item_type': 'new_type'}
    item = tables.ItemType(**new_item_type)
    get_add_method(get_db_session, item)
    print(item.item_id)


def test_try_to_add_testdata2(get_db_session, get_add_method, get_item_type_generator):
    item = tables.ItemType(**get_item_type_generator.build())
    get_add_method(get_db_session, item)
    print(item.item_id)

def test_finally(generate_item_type):
    print(generate_item_type.item_id)
