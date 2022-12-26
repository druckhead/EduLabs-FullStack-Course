# from time import perf_counter
# from nationalizeexceptions import *
#
# from E1 import Nationalize
#
# if __name__ == '__main__':
#     # NAMES = ["Kenyon", "Deshawn", "Michaela", "Molly", "Barrett", "Steven", "Brisa", "Zackery", "Kamora", "Sara",
#     #          "Jaycee",
#     #          "Leland", "Danny", "Ashlee", "Royce", "Bryce", "Anabel", "Skyler", "Cristian", "Shannon", "Aditya",
#     #          "Asher",
#     #          "Quintin", "Hunter", "Rose", "Ronin", "Zion", "Rayne", "Nyasia", "Sanaa", "Dominic", "Tyshawn", "Gillian",
#     #          "Clayton", "Easton", "Julio", "Coby", "Melany", "Bradyn", "Jazlene", "Myah", "Zayden", "Noemi", "Brooks",
#     #          "Mckenzie", "Khalil", "Ruben", "Kristina", "Dixie", "Sawyer", "Ali", "Nasir", "Kaylynn", "Messiah",
#     #          "Kevin",
#     #          "Will", "Cordell", "Dereon", "Jamari", "Adrien", "Ashtyn", "Santos", "Isabela", "Lucas", "Harley",
#     #          "Esteban",
#     #          "Zain", "Alma", "Elliot", "Collin", "Alexa", "Magdalena", "Kristopher", "Kaya", "Jaydin", "Aimee", "June",
#     #          "Ryland", "Belinda", "Kennedy", "Mohammed", "Kenna", "Kaia", "Ada", "Frida", "Valeria", "Noe", "Savannah",
#     #          "Jorge", "Claire", "Abdullah", "Hillary", "Drake", "Kristen", "Amelia", "Marcus", "Liana", "Saniya",
#     #          "Karissa",
#     #          "Jasper"]
#
#     NAMES = ["daniel", "kaia", "ziv", "noa", "yuval"]
#
#     n = Nationalize()
#     start = perf_counter()
#     try:
#         countries = n.info(NAMES)
#     except TooManyRedirects as redirect_err:
#         print(redirect_err)
#     except Timeout as timeout_err:
#         print(timeout_err)
#     except NameNotFound as name_err:
#         print(name_err)
#     except CountryIdNotFound as country_id_err:
#         print(country_id_err)
#     else:
#         print("DONE")
#     finally:
#         end = perf_counter()
#         print(f"[Runtime: {end - start}s]")
