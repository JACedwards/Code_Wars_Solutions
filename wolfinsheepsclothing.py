def warn_the_sheep(queue):

    
    

    
    if 'wolf' == queue[-1]:
        return("Pls go away and stop eating my sheep")
    else:
        res = len(queue) - queue.index('wolf')
        res = res
        
        
    return f"Oi! Sheep number {res -1}! You are about to be eaten by a wolf!"



print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))