print(''' 
      

 __    __    ___  ____        _____   __   ____  ____   ____     ___  ____      
|  T__T  T  /  _]|    \      / ___/  /  ] /    T|    \ |    \   /  _]|    \     
|  |  |  | /  [_ |  o  )    (   \_  /  / Y  o  ||  _  Y|  _  Y /  [_ |  D  )    
|  |  |  |Y    _]|     T     \__  T/  /  |     ||  |  ||  |  |Y    _]|    /     
l  `  '  !|   [_ |  O  |     /  \ /   \_ |  _  ||  |  ||  |  ||   [_ |    \     
 \      / |     T|     |     \    \     ||  |  ||  |  ||  |  ||     T|  .  Y    
  \_/\_/  l_____jl_____j      \___j\____jl__j__jl__j__jl__j__jl_____jl__j\_j    
                                                                                




''')
options = ['1 + Basic Scan' ,'2 + Advanced Scan','3 + Manual Scan']
result = for item in options:
  return item;
  if item == 1:
    print('''
          Basic Scanning 
    ''')
    option = input('Website url please :')
    if option.lenght !== 0:
      print('wait for results please')
