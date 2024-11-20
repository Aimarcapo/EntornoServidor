from typing import Dict

def hiriak_ordenatzen(hiriak: Dict[str, int]) -> list:
    filtered_list = []
   
    for key, value in hiriak.items():
        if value >= 200000:
           
            filtered_list.append((key, value))
    
   
    filtered_list.sort(key=lambda x: x[1], reverse=True) 

   
    return [key for key, value in filtered_list]


hiriak = dict(Bilbo=345000, Gasteiz=250000, Eibar=27000)

print(hiriak_ordenatzen(hiriak))
