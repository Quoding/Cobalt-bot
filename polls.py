YESNO_EMOJIS = ["✅", "❌"]
DAYS_EMOJIS = ["⚽", "⚾", "🏀", "🎾", "🏈", "🥏", "🏓"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def make_poll(preset):
    """Make the poll based on the given preset

    Args:
        preset (string): Value in ['days', 'yesno']

    Returns:
        tuple: emojis and message for the poll creation
    """

    if preset == "days":
        message = "Please vote with the reacts below !\n\n"
        for day, emoji in zip(DAYS, DAYS_EMOJIS):
            message += "{} = {}\n".format(day, emoji)

        return DAYS_EMOJIS, message

    elif preset == "yesno":
        message = "Please vote with the reacts below!"

        return YESNO_EMOJIS, message

    else:
        return "Bad usage, check the usage with !help"
