clans = {
    'crab': 0,
    'crane': 1,
    'dragon': 2,
    'lion': 3,
    'phoenix': 4,
    'scorpion': 5,
    'unicorn': 6,
}

def get_clans_list():
    clan_list = []
    for clan, clan_id in clans.iteritems():
        clan_list.append((clan_id, clan.title()))
    clan_list.append((None, '---'))
    return sorted(clan_list, key=lambda tup: tup[1])
