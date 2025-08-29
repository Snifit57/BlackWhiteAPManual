# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class Async(DefaultOnToggle):
    """Adds all location checks that are only accessable after Route 7 (including areas you backtrack to).
    This does NOT include post-game location checks.
    """
    display_name = "Async"

class PostGame(DefaultOnToggle):
    """Adds all location checks that are only accessable after defeating the Elite Four and Ghetsis.
    """
    display_name = "PostGame"

class NPC(DefaultOnToggle):
    """Shuffles optional items given to you by NPCs into the pool.
    """
    display_name = "NPC Items"

class HiddenItems(DefaultOnToggle):
    """Shuffles hidden items into the pool.
    """
    display_name = "Hidden Items"

class DowsingMCHN(Toggle):
    """Hidden items require the Dowsing MCHN in logic.
    """
    display_name = "Dowsing MCHN Logic"

class Cobalion(DefaultOnToggle):
    """Shuffles Mistralton Cave items into the pool (Does not Impact the "Defeat Cobalion" Goal)
    """
    display_name = "Mistralton Cave Items"

class AbyssalRuins(DefaultOnToggle):
    """Shuffles Abyssal items into the pool (Only works with the "Defeat Cynthia" or "Become Champion" goals.)
    """
    display_name = "Abyssal Ruins Items"

class Flash(DefaultOnToggle):
    """Items in or through dark areas require TM70 Flash in logic.
    """
    display_name = "Flash Logic"

class ResortPass(DefaultOnToggle):
    """Access to Desert Resort and Relic Castle logically requires the "Resort Pass".
    """
    display_name = "Resort Pass"

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options


def after_options_defined(options: dict) -> dict:
    options.update({
        'include_npc_items': NPC,
        'randomize_hidden_items': HiddenItems,
        'require_dowsing_mchn': DowsingMCHN,
        'include_mistralton_cave_items': Cobalion,
        'include_abyssal_ruins_items': AbyssalRuins,
        'require_flash': Flash,
        'add_resort_pass': ResortPass
    })
    return options





