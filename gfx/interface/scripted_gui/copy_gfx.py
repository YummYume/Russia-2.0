# Created by Yam for the Russia Reworked mod. Free to use. Requires Python 3.10
import traceback
import shutil
import os.path

if __name__ == "__main__":

    try:
        national_obligations = [
            "industrial_awakening",
            "tsar_bomba",
            "unfailing_army",
            "grand_fleet",
            "proletarian_union",
            "neverending_story",
            "continental_system",
            "treaty_moscow",
            "golden_age",
            "imperial_obligations",
            "carry_on_legacy",
            "russian_realm",
            "rebirth"
        ]
        national_obligations_options = [
            3,
            2,
            2,
            2,
            3,
            3,
            2,
            2,
            2,
            3,
            2,
            3,
            3,
        ]

        print("Creating GFX...")

        if os.path.isfile("GFX_national_obligations_golden.dds"):
            national_obligations_with_options = zip(national_obligations, national_obligations_options)

            for national_obligation, national_obligation_options in national_obligations_with_options:
                title = national_obligation.replace("_", " ").title()

                match national_obligation_options:
                    case 1:
                        if not os.path.isfile(f"GFX_{ national_obligation }_first_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_first_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                    case 2:
                        if not os.path.isfile(f"GFX_{ national_obligation }_first_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_first_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                        if not os.path.isfile(f"GFX_{ national_obligation }_second_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_second_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                    case 3:
                        if not os.path.isfile(f"GFX_{ national_obligation }_first_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_first_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                        if not os.path.isfile(f"GFX_{ national_obligation }_second_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_second_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                        if not os.path.isfile(f"GFX_{ national_obligation }_third_option_button.dds"):
                            shutil.copy(f"GFX_national_obligations_golden.dds", f"GFX_{ national_obligation }_third_option_button.dds")
                        else:
                            print("Warning : file GFX_%s_second_option_button.dds already exists, skipping..." % national_obligation)

                    case _:
                        print("Error for national obligation %s" % title)

            print("Success")
        else:
            print("Warning : file GFX_national_obligations_golden.dds cannot be found")
            print("Cancelling...")

    except Exception:
        print("Something went wrong...")
        print(traceback.format_exc())
