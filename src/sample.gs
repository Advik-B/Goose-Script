# This is a comment
# This is an example file of goose script
# --------------------------------------------------

#* 
    This
    is
    a
    multiline
    comment
#*

WAIT 5s #  wait 5 seconds 

#*
    Valid timers are:

        s - seconds
        m - minutes
        h - hours
        d - days
#*

#*
    Valid commands are:

        Functions:
            OPEN - opens a file
            WAIT - waits for a specified amount of time
            EXIT - exits the script
            DELETE - deletes the file
            COPY - copies a file
            MOVE - moves a file
            GETPTH - gets the path of a file or directory like:
            
                `%USERPROFILE%`
                `%APPDATA%`
                `%TEMP%`
            
            GETCWD - gets the current working directory
            DISCARD - same as DELETE but sends the file to the recycle bin or trash
            
            RUNCMD - runs a command
            RUNCMD_w - runs a command and waits for it to finish
            
            LOG - logs a message if a terminal is available
            
            MKDIR - creates a directory
            MKDIR_F - creates a directory forcefully

            RMDIR - removes a directory
            RMDIR_F - removes a directory and all of its contents forcefully

            DEL_DIR - same as RMDIR but deletes all files and subdirectories and sends them to the recycle bin or trash
            CD - changes the current working directory
            PWD - returns the current working directory

            CD_UP - changes the current working directory to the parent directory

            CD_HOME - changes the current working directory to the home directory aka the user's profile directory

            CD_TEMP - changes the current working directory to the temp directory

            KP - key press (raw)

        KeyBoard:

            ESC - escape
            BACKSPACE - backspace
            TAB - tab
            CTRL - control
            SHIFT - shift
            SUPER - super (windows key) or command key
            ALT - alt (option key)
            CAPS - caps lock
            ENTER - enter (return key)
            SPACE - space
            PAGEUP - page up
            PAGEDOWN - page down
            END - end
            HOME - home
            LEFT - left arrow
            UP - up arrow
            RIGHT - right arrow
            DOWN - down arrow
            NUM_LOCK - num lock
            
            F1 - F1
            F2 - F2
            F3 - F3
            F4 - F4
            F5 - F5
            F6 - F6
            F7 - F7
            F8 - F8
            F9 - F9
            F10 - F10
            F11 - F11
            F12 - F12

            INSERT - insert
            DEL - delete
            FN - function key

#*
