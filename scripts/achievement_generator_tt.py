# Created by Yam for the Russia Reworked mod. Free to use.
import traceback

if __name__ == "__main__":

    try:
        achievements = [
            "cleaning_red_carpet",
            "revolution_completed",
            "speedrun_urals",
            "not_sus",
            "new_world_order",
            "red_army",
            "world_without_borders",
            "rush_b",
            "fourth_rome",
            "gotcha",
            "drunkard_wheel",
            "copyright",
            "running_90",
            "quick_revolution",
            "great_deeds",
            "rome_tsarigrad_moscow",
            "1905_avenged",
            "lacplesis",
            "third_friend",
            "national_priority",
            "click_me",
            "big_tower"
        ]

        gui = ""
        sub_gui = ""
        scripted_gui_dynamic_list = ""
        scripted_gui_trigger = ""
        localisation = ""
        gfx = ""
        y = 5

        print("Generating %s achievement..." % (len(achievements)))

        for achievement in achievements:
            title = achievement.replace("_", " ").title()

            print("Generating achievement %s" % title)

            gui += f"""
            #{ title }
            containerWindowType = {{
                name = "russia_reworked_{ achievement }_achievement"
                position = {{ x = 15 y = { y } }}
                size = {{ width = 600 height = 83 }}
                
                iconType = {{
                    name = "achievement_entry_bg"
                    spriteType = "GFX_russia2_achievement_entry_bg"
                    position = {{ x = -2 y = -4 }}
                    Orientation = "UPPER_LEFT"
                }}
                
                iconType = {{
                    name = "russia_reworked_{ achievement }_achievement_icon_unlocked"
                    spriteType = "GFX_{ achievement }_unlocked"
                    position = {{ x = 17 y = 12 }}
                    Orientation = "UPPER_LEFT"
                }}

                iconType = {{
                    name = "russia_reworked_{ achievement }_achievement_icon_locked"
                    spriteType = "GFX_{ achievement }_locked"
                    position = {{ x = 17 y = 12 }}
                    Orientation = "UPPER_LEFT"
                }}

                iconType = {{
                    name = "russia_reworked_{ achievement }_achievement_status_yes"
                    spriteType = "GFX_russia2_achivevement_status_yes"
                    position = {{ x = @ACHIEVEMENT_ICON_POSITION_X y = @ACHIEVEMENT_ICON_POSITION_Y }}
                    Orientation = "UPPER_LEFT"
                }}

                iconType = {{
                    name = "russia_reworked_{ achievement }_achievement_status_no"
                    spriteType = "GFX_russia2_achivevement_status_no"
                    position = {{ x = @ACHIEVEMENT_ICON_POSITION_X y = @ACHIEVEMENT_ICON_POSITION_Y }}
                    Orientation = "UPPER_LEFT"
                }}

                instantTextBoxType = {{
                    name = "achievement_name"
                    position = {{ x = @ACHIEVEMENT_TITLE_POSITION_X y = @ACHIEVEMENT_TITLE_POSITION_Y }}
                    font = "hoi_20b"
                    borderSize = {{ x = 0 y = 0 }}
                    text = russia_reworked_{ achievement }_achievement_title
                    maxWidth = 280
                    maxHeight = 32
                    fixedsize = yes
                    format = left
                }}
                
                instantTextBoxType = {{
                    name = "achievement_desc"
                    position = {{ x = 112 y = 30 }}
                    font = "hoi_18mbs"
                    borderSize = {{ x = 0 y = 0 }}
                    text = russia_reworked_{ achievement }_achievement_desc
                    maxWidth = 450
                    maxHeight = 100
                    format = left			
                }}
                
                ## stuff to the right
                
                instantTextBoxType = {{
                    name = "achievement_obtained_by"
                    position = {{ x = -8 y = 3 }}
                    font = "hoi_16mbs"
                    borderSize = {{ x = 0 y = 0 }}
                    text = russia_reworked_achievements_obtained_by
                    orientation = upper_right
                    maxWidth = 100
                    maxHeight = 32
                    format = centre
                }}

                containerWindowType = {{
                    name = "achievement_obtained_by_container"
                    position = {{ x = 135 y = 15 }}
                    size = {{ width = 175 height = 65 }}
                    orientation = upper_right
                    origo = upper_right
                    verticalScrollbar = "right_vertical_slider"

                    background = {{
                        name = "Background"
                        spriteType = "GFX_russia2_empty_grid_bg"
                    }}

                    gridboxtype = {{
                        name = "russia_reworked_{ achievement }_achievement_grid"
                        position = {{ x = 5 y = 2 }}
                        size = {{ width = 100%% height = 100%% }}
                        slotsize = {{ width = 30%% height = 35 }}
                        max_slots_horizontal = 3
                        add_horizontal = yes
                        format = "UPPER_LEFT"
                    }}
                }}
            }}
            """

            y += 100

            sub_gui += f"""
    #Linked to gridboxtype (russia_reworked_{ achievement }_achievement_grid)
    containerWindowType = {{
        name = "russia_reworked_{ achievement }_entry"
        position = {{ x = 0 y = 5 }}
        size = {{ width = 50 height = 25 }}
        
        iconType = {{
            name = "flag"
            quadTextureSprite = "GFX_flag_small2"
            position = {{ x = 12 y = 0 }}
            alwaystransparent = no
            Orientation = "UPPER_LEFT"
            pdx_tooltip = LOC_russia_reworked_{ achievement }_entry_tt
            pdx_tooltip_delayed = LOC_russia_reworked_{ achievement }_entry_tt_desc
        }}
    }}
            """

            scripted_gui_dynamic_list += f"""
            russia_reworked_{ achievement }_achievement_grid = {{
				array = global.{ achievement }_achievement
				change_scope = yes
				entry_container = russia_reworked_{ achievement }_entry
			}}
            """

            scripted_gui_trigger += f"""
            russia_reworked_{ achievement }_achievement_icon_unlocked_visible = {{
				is_in_array = {{ global.{ achievement }_achievement = THIS }}
			}}

			russia_reworked_{ achievement }_achievement_icon_locked_visible = {{
				NOT = {{
					is_in_array = {{ global.{ achievement }_achievement = THIS }}
				}}
			}}

			russia_reworked_{ achievement }_achievement_status_yes_visible = {{
				is_in_array = {{ global.{ achievement }_achievement = THIS }}
			}}

			russia_reworked_{ achievement }_achievement_status_no_visible = {{
				NOT = {{
					is_in_array = {{ global.{ achievement }_achievement = THIS }}
				}}
			}}
            """

            localisation += f"""
 russia_reworked_{ achievement }_achievement_title:0 "§Y{ title }§!"
 russia_reworked_{ achievement }_achievement_desc:0 ""
 LOC_russia_reworked_{ achievement }_entry_tt:0 "§Y[THIS.GetNameDefCap]§!"
 LOC_russia_reworked_{ achievement }_entry_tt_desc:0 "§Y[THIS.GetNameDefCap]§! obtained this achievement at§Y[?global.{ achievement }_achievement_date@THIS.GetDateString]§!."
            """

            gfx += f"""
    spriteType = {{
        name = "GFX_{ achievement }_locked"
        texturefile = "gfx/interface/scripted_gui/GFX_{ achievement }_locked.dds"
    }}

    spriteType = {{
        name = "GFX_{ achievement }_unlocked"
        texturefile = "gfx/interface/scripted_gui/GFX_{ achievement }_unlocked.dds"
    }}
            """

        gui += f"""
            #Don't touch that
            containerWindowType = {{
                name = "russia_reworked_bottom_space_achievement"
                position = {{ x = 15 y = { y } }}
                size = {{ width = 600 height = 0 }}
            }}
        """

        f = open("achievements_save.txt", "w", encoding='utf-8-sig')
        f.write(gui)
        f.write(sub_gui)
        f.write(scripted_gui_dynamic_list)
        f.write(scripted_gui_trigger)
        f.write(localisation)
        f.write(gfx)
        f.close()
        print("Success")

    except Exception:
        print("Something went wrong...")
        print(traceback.format_exc())