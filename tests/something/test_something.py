import pytest
from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize('status', [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"

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
    'fr', 'fr_FR'
])
def test_something_excange_localizations(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)
