class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:       
        # ordena pelo tempo de fim da tarefa
        intervals.sort(key=lambda x: x[1])
        
        removedIntervals = 0
        lastEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            # se o início atual é menor que o último fim, remove sobreposição
            if start < lastEnd:
                removedIntervals += 1
            # se nao, atualiza ultimo fim
            else: 
              lastEnd = end
            
        return removedIntervals