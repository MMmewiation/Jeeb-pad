import os

user_input = input("Type away: ")
done_1 = input("Are you done? (Y/N): ")

if done_1.lower() == "y":
    filename = input("What would you like to save this as: ")
    filepath = input ("where would you like to save it (example C: for your defualt drive)")


    def write_file():
        full_path = os.path.join(filepath, filename)
        with open(filename, "w") as file:
            file.write(user_input)

    write_file()
    print(f"""                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
                                                                             .#*+.                                                
                                                        %++-.      :=      -==+=+=.                                               
                                                      .-%*==++**+.--%*+===+*++=+==+*                                              
                                                    .**+=++==+**++====+++++++++==++==                                             
                                               -*@@%%###+++*+=+++++++++++*+++++*++=+=.-                                           
                                          .-*%%%%@@@%#****+++++=+++++++++==++=+*****+=@+                                          
                                        -*%#####**+++*###*++++++++++****+++++=+++++++==.                                          
                                       .@@%##****+=+*###*+++*******++++***++*++==+++++=+=.                                        
                                        +#@#%%%*#%%#+====++++*+**++***+=+#*++*++==+++++++=                                        
                                          +@@@#*##*++**+++++*******++++++====+++***+++**++-                                       
                                             =++++**********+++==+=+++++++==++=**+++++==++*                                       
                                             +++********###*+=--::-==+****+++++++++++==++=*-                                      
                                            :**++++++++++=+*#%@@@@@%#**#*+++**+++=+**++++===.                                     
                                            :+*****+++****++#%=%%@@@@%****###***++***+**+++***+:                                  
                                           :+**+***++****+++#@@@%%@@@@@#####****+=+**+*++++++++=:                                 
                                          :++++**+++*+++++++*%@@@@@@@@%##*###******+===+**+****##.                                
                                        =:********++++++++**++*#%%##+*#####%%#%@%####+--++***+=++:                                
                                       =@+++*******+*****+===+++*+=+*#**++##**##@@@@@@@+=++*##+=++                                
                                       :*++*********++++*******+++++**++++**+=+#%%@@@@%*====*%%+=*:                               
                                       +++*************+**+****#%%%#****+++**+**#@@@@*+*+*+:-*%@==+:                              
                                      .#***+******+*******++++***+++++++++***+*#@@@#==+*****=%%@@+**+:                            
                                      -*++**#************************####*+**+++%+==+****%@@@@@@@+*+*+                            
                                      +++******##**++**##+++**++++*#####*##*++++++++**+*+==#@%*==+****                            
                                     :***********%#*+*+**+*******++*******###*++==+**++**++=+++*+*****                            
                                     :+++*******+#%%*+*+++++*+*+*##%%####%%%##***##*++++++++**#*******                            
                                    -************%##@%**##++**##*#@@@%##*+#%###*++*****#####*****#****                            
                                   =%*+********#*++==*#*#%#****#%%%#*+*%%#=:=**++****++#####**********                            
                                  :+++*********#**#%@@***%%#=-++*#@%@@@@@@@%##**+***+***##*##***#*#***                            
                                -**+++*#*+*************#+#@@@@%+=+%@@@%%%@@@@%*++*****#%%####*#*****++                            
                              +:++*+**##**#****++*******+#@*:%@@@%#*#@@@@@@@+=+*##**####%#*###%#*###@#                            
                            *#@+**+*+*###**+++****+*##*#+*@#=@@@%%@@@%##*+==+**+*##*######**###%*#- :                             
                          .-*+*++++%#####*+***#*##%#*****+@@++%@@@@*=-===+++***#*%#%%%%##*+*%%%##=                                
                  .=+***++++****##*##*-.     .=*+*****#***+@@@#*=*%#**##**++****#%%##%%%#*##@@*.                                  
               .**+*####+++******##+=:        +###****#*#*+==%@@@@*+******+*+##########%%##*#-                                    
                ==+*#******##*=:...           =+**+**#*******=---=+*#****++**###****#*###%%=                                      
                .::-++++:  ...             ..-*#%****+++**##***********+++=%@%%@@@@@@@@%#%-                                       
                      .                 .:=%%%%@##*++********#**********#@@@@%%%%#%@%%#++-                                        
                                       =+#%%###%@%##**+*+###*********+*++%%@@@@@@@@%###-                                          
                                      +@###%%###*-  +#+*#*+***####****#@@%%%#%%%%%@#*+*.                                          
                                      -**#%@%**+-    @@###***#**##***##%%@%%#####**+**#                                           
                                     .*#*+=#*+:     +#***+*####*****##**++***********-:                                           
                                      +**=:-.      :-***+*#####***@##+*%%######%##=.                                              
                                        :.         ***++**####***=*   ---+#%#%%@*:                                                
                                                  -#*++*##*####*=         ::....                                                  
                                                  -+++#####****=:                                                                 
                                                 :*++*%%###***=                                                                   
                                                :*++*###****=:                                                                    
                                                                                                                                  """)
    print(f"Your input has been saved to {filename}.")
else:
    print("""
                        @                                                                 @@@@@@@@@@@@@@@@%%%%%@@@@                                                              
                                                                                        @@@@@@@@@@@@@@@%%%%%%@%%%%@@                                                             
                                                                                    @@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@@@                                                         
                                                                                   @@@@@@@@@@@@@@@@@@@%%%%%%#######%%%%@@                                                        
                                                                                 @@@@@@@@@@@@@@@@@@%%%%%%%###############%@                                                      
                                                                              @@@@@@@@@@@@%%%@@%%%%%%%%%%%#################%@@                                                   
                                                                         @@@@@@@@@@@@@@%%@%%%%%%%%%%%%%%%#####################%@                                                 
                                                                     @@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%##########################%%@ @                                            
                                                                   @@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%###########################%%@@@                                            
                                                                 @@@@@@@@@@%%@@@%%%%%%%%%%%%%%%%%%%%%############################%%@@                                            
                                                            @  @@@@@@@@@@%%%@@@@@@@%%%%%%%%%%%%%%%%%%############**********#######%%@                                            
                                                            @@@@@@@@@@%%%%%%@@@@@@@@%%%%%%%%%%%%%%%%##############************######%                                            
                                                        @@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@%%%%%%%#%%%%#################**********#####%%                                            
                                              @@@@@@@@@@@@@@@@@@@@@%%@%@@%%%%@@@@@@@@@%%%%%%%%%%%%####################********#*###%@                                            
                                            @@@@@@@@@@@@@@@@@@@@@@@%@%%%@@@@@@@@@@@@@%%%%%%%%%%%%#####################*******######%%                                            
                                           @@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@%@@@%%%%%%%%%%%%#####################***######*##%                                             
                                          @@@@@@@@@@@@@@%%@@@@@@@%%@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%#########################%@                                            
                                          @@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%#######################%                                             
                             @@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%#########################%                                             
                    @@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%########################%@                                             
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%###%%#%%##%%#################%%@                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%##%%%%%%%%%%#######*#########%%@                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%%%%%%%%%%%%%%%%%######***#######%@@                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@%@@@@@%%%@%%%%%%%%%%%%########***#####%@                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@%%@%%%%%%%%%%%%%%#%#**######%%#*###%%                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@##%@%@@%%%%%%%%%%#%##**#########*##%@                                            
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##%%%%%%%%@@@@@@@%#######%%######*#%%                                            
@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%@@@@%%%@@@@@%#####%%%#%%%%%%%@###%@                                           
@@@@@@@@@@@@@@@@@@@                             @     @@@@@@@           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%###%%#####%%%%###%%%%%#%@%#%@                                           
@@@@@@@@@@@@@@@@@@                                                              @@@@@@@@@@@@@@@@@@@@%%#########%%@%%%%#############%%@                                           
@@@@@@@                                                                         @@@@@@@@@@@@@@@@@@%%%%%######@@@@@@@%%%%#######%###%%@@                                          
                                                                                 @@@@@@@@@@@@@@@@%%%%%%%%%%###%@@@@@@@@@%%%######*######                                         
                                                                                      @@@@@@@@@@%%%%%%%%%%####%%%%%@@@@@%%%@%####******##                                        
                                                                                        @@@@@@@%%###############%%##%%@%%@%@@@%*#**##***#                                        
                                                                                         @@@@@%%%%%%###############%%%%%###%###*####****##%                                      
                                                                                        @@@@%%%%%%%%######******########***********###***#%%@%#                                  
                                                                                        @@%%%%%%########********##**************************%@                                   
                                                                                     @@@@@%%%##########**#****###***************************#%                                   
                                                                                    @@%%%%%###############%%@@%#****************************%@                                   
                                                                                   @@%%%%##############%%@@@@@@%#*******************+*******#%@                                  
                                                                                @@@@%%%%%%%###########%@@@@@@@@@#*****************++*********#%@                                 
                                                                                @%%%%####%%%%%#######%@@@@@@@@@@##*****************************#%%                               
                                                                              @@%%%%%##%%%%%%%%%###%%%@@@@@@@@@@##********************************%                              
                                                                              @@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%######*##***********************##@                              
                                                                             @@%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@%##%%####*###**##******************##                               
                                                                           @@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%#########*#########***************#%                                
                                                                           @@@@@@@@@@@%@@%%%%%%%%%%%%%%%%%%%%#######****#######****************#                                 
                                                                          @@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%##############********##*********                                   
                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@%%%%%#############*****************                                    
                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@%%%###########**************#*                                    
                                                                          @@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@%%%%#############***************                                    
                                                                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%#######*************###                                    
                                                                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%###%######****######%                                    
                                                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%#%%%######**####%                                      
                                                                               @@@@@@@@@@@@@           @@@@@@@@@@@@%@@@@%@@@%%%########%%%                                       
                                                                                                                @@@@@ @@@@@@@@%%%%####%                                          
                                                                                                                      @@@@@@@@%%@@@%#%%                                          
                                                                                                                     @@@@@@@@@@@@@@%%%%                                          
                                                                                                                      @@@@@@@@@@@@@#%%                                           
                                                                                                                       @@@@@@@@@@@@%%                                            
                                                                                                                          @@@@@@@@%@%                                            
                                                                                                                           @@@@@@@@                                              
                                                                                                                           @@@@@@                                                
                                                                                                                             @@                                                  
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
                                                                                                                                                                                 
""")
    print("ERROR: the file {filename}.txt failed to save {user_input}, Please try again" )

