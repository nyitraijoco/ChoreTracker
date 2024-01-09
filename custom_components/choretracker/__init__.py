"""The Chore Tracker Integration."""

DOMAIN = 'chore_tracker'

async def async_setup(hass, config):
    """Set up the Chore Tracker integration."""
    hass.data.setdefault(DOMAIN, {})

    # Import the ChoresCollection entity
    from chores_entity import ChoresCollection

    # Instantiate the ChoresCollection entity and store it in Home Assistant data
    chores_entity = ChoresCollection()
    hass.data[DOMAIN]['chores_entity'] = chores_entity

    return True
