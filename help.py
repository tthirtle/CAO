"""Dialog messages and help screens"""

splash_msg:str = "Retail Assistant\nBy: Thomas Thirtle"

exit_msg:str = "Do you wish to quit?\nAll changes will be lost\n(Except database and program configuration)"

cancel_msg:str = "Cancel changes?"

empty_msg = "All fields must be complete"

main_menu_help = """Options:

In-store: Options useful for in store. You will need to select your store first.

Program configuration: options for the program

Database Editor: Modify Items and Stores"""

config_help = """
Company Name - name of company you represent

Database file - Location of the database file (MUST BE ABLE TO WRITE)

Report Directory - Where you want reports saved to (MUST BE ABLE TO WRITE)
"""

add_contact_help = """
This screen is just used to add a store contact. I can store up to 3 names and their titles.
To get out of the notes field press TAB.
"""

edit_contact_help = """
This screen is just used to add & change store contacts. I can store up to 3 names and their titles.
To get out of the notes field press TAB.
"""

add_store_help = """
This screem is used to add a new store into the database. Only the store name is required 
"""