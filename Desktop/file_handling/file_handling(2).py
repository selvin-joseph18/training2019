with open('details','r') as  f1:
   with open('write','w') as f2:
       for line in f1:
           print(f2.write(line))