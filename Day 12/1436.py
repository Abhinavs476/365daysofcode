''' You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city. '''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        trajectory = {path[0] : path[1] for path in paths }
        destinations = trajectory.values()

        ans = ""
        for entry in destinations:
            if  entry not in trajectory.keys():
                ans = entry
                break
                
        return ans
      
''' Link: https://leetcode.com/problems/destination-city/ '''
