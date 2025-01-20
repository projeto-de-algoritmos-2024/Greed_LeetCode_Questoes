from typing import List
from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # ordena pelo horario limite
        courses.sort(key=lambda x: x[1])
        
        heap = []  # maxheap com as duracoes
        tempoTotal = 0   # somatorio da duracao dos cursos
        
        for duracao, deadline in courses:
            # Adiciona o curso apenas se ainda houver tempo
            if tempoTotal + duracao <= deadline:
                tempoTotal += duracao
                heappush(heap, -duracao)
            # verifica se da para trocar pelo curso mais longo (topo heap)
            elif heap and -heap[0] > duracao and tempoTotal - (-heap[0]) + duracao <= deadline:
                # Remove o curso mais longo e adiciona o atual
                tempoTotal -= -heappop(heap)
                tempoTotal += duracao
                heappush(heap, -duracao)
        
        return len(heap)