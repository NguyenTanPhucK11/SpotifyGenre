import sys
import os
import md5

user_name = os.getlogin()
music_dir = "/Users/" + user_name + "/Music/iTunes/iTunes Media/Music"
cont = False

print("This utility is to remove duplicate music from your iTunes\n"
    + "library, though it will remove duplicates from any folder\n"
    + "that you enter.\n")
print("The default folder for iTunes is located at:\n"
       + "\t" + music_dir)

while (not cont):
   temp = raw_input("\nEnter the name of your folder to remove duplicates\n"
                  + "from or hit enter to use the suggested location\n> ")
   
   if (not temp):
      temp = music_dir

   check = raw_input("\nIs this correct? (y/n)\n\t" + temp + "\n> ")
   
   if (check == 'y'):
      music_dir = temp
      cont = True

def remove_duplicates(dir):
   unique = []
   for filename in os.listdir(dir):
      filename = dir + '/' + filename
      if os.path.isfile(filename):
         filehash = md5.md5(file(filename).read()).hexdigest()
         if filehash not in unique: 
            unique.append(filehash)
         else:
            print "Removing " + filename + "..."
            os.remove(filename)
      elif os.path.isdir(filename):
         remove_duplicates(filename)
      else:
         print("Unable to find file/directory " + filename
             + ", please try again")

print "\nIt's working I promise, give it a minute or two...\n"
remove_duplicates(music_dir)