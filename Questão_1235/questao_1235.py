class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1]) 
        # Primeiro os trabalhos são organizados de acordo com o tempo de término
        
        
        dp = [0] * len(jobs)
        # dp vai armazenar o maior valor de lucro que se pode ter considerando a quantidade de trabalho
        
        
        dp[0] = jobs[0][2]
        # Inicializa o valor de dp[0] com o valor do primeiro trabalho

        # função para encontrar o ultimo trabalho que não conflita com o trabalho atual
        def ver_conflito(atual):
            # Busca binária com min e max definindo o intervalo de busca
            min, max = 0, atual - 1
            while min <= max:
                mid = (min + max) // 2
                if jobs[mid][1] <= jobs[atual][0]:
                    if jobs[mid + 1][1] <= jobs[atual][0]:
                        min = mid + 1
                    else:
                        return mid
                else:
                    max = mid - 1
            return -1
        
        # loop para calcular o valor de dp[i] para cada trabalho
        for i in range(1, len(jobs)):
            # lucro sem considerar o trabalho atual
            dp[i] = dp[i - 1]
            
            # lucro considerando o trabalho atual
            lucro_atual = jobs[i][2]
            ultimo_trabalho_sem_conflito = ver_conflito(i)
            if ultimo_trabalho_sem_conflito != -1:
                lucro_atual += dp[ultimo_trabalho_sem_conflito]
            
            # Atualiza dp[i] com o maior valor entre o lucro considerando o trabalho atual e o sem considerar
            dp[i] = max(dp[i], lucro_atual)
        
        # Retorna o maior lucro possível
        return dp[-1]
