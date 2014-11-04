def bubble_Sort_1(L):
    
    for i in range(len(L) - 1):
      
      step = 0
      
      for j in range(0, len(L)-i-1):
          
          
          if L[j] > L[j+1]:
              
              L[j] , L[j+1] = L[j+1] , L[j]
            
      
      

    
    
def bubble_Sort_2(L):

    
    for i in range(len(L) - 1):
        
        step = 0
        
        for j in range(len(L)-1,i,-1):
            

            if L[j] < L[j-1]:
                
                L[j] , L[j-1] = L[j-1] , L[j]