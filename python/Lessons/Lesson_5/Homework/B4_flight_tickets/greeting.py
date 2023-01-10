# from time import sleep

__GREETING = \
    """
         _       __       __                            
        | |     / /___   / /_____ ____   ____ ___   ___ 
        | | /| / // _ \\ / // ___// __ \\ / __ `__ \\ / _ \\
        | |/ |/ //  __// // /__ / /_/ // / / / / //  __/
        |__/|__/ \\___//_/ \\___/ \\____//_/ /_/ /_/ \\___/ 
                         __                             
                        / /_ ____                       
                       / __// __ \\                      
                      / /_ / /_/ /                      
                      \\__/ \\____/
        ___                            _                   
       /   |   ____ ___   ___   _____ (_)_____ ____ _ ____ 
      / /| |  / __ `__ \\ / _ \\ / ___// // ___// __ `// __ \\
     / ___ | / / / / / //  __// /   / // /__ / /_/ // / / /
    /_/  |_|/_/ /_/_/_/ \\___//_/   /_/ \\___/ \\__,_//_/ /_/ 
          /   |   (_)_____ / /(_)____   ___   _____        
         / /| |  / // ___// // // __ \\ / _ \\ / ___/        
        / ___ | / // /   / // // / / //  __/(__  )         
       /_/  |_|/_//_/   /_//_//_/ /_/ \\___//____/                         
"""

__EXPLANATION_MSG = f"This is our automated ticket purchase system!\n" \
                  f"Follow along to ensure the perfect service " \
                  f"that you are accustomed to."


def print_greeting() -> None:
    """
    Prints welcome message.
    :return:
    """
    for char in __GREETING:
        print(char, end="")
        # sleep 0.25ms
        # sleep(0.0020)

    print()
    print(__EXPLANATION_MSG)
    print()

    return
