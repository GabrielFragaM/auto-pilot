from services.chatgpt import call_chatgpd

class Agent:
    def __init__(self, chatgpd_key, chatgpd_model):
       self.chatgpd_key = chatgpd_key
       self.chatgpd_model = chatgpd_model

    def get_solution(self, instructions):
        list = []
        list.append({"role": "system", "content": 'Você é um robô que recebe uma determinada tarefa e precisa fornecer a solução.'})
        list.append({"role": "user", "content": f'"""{instructions}""". Retorne apenas a sua solução para essa tarefa.'})

        result = call_chatgpd(api_key=self.chatgpd_key, model=self.chatgpd_model, messages=list)

        return result
    
    def build_tasks(self, instructions, solutions):
        list = []
        list.append({"role": "system", "content": 'Você é um robô que recebe uma lista de tarefas prontas e precisa retornar a solução completa juntando todas as tarefas realizadas da lista.'})
        list.append({"role": "user", "content": f'Objetivo: {instructions}, Tarefas Resolvidas: """{solutions}""".'})

        result = call_chatgpd(api_key=self.chatgpd_key, model=self.chatgpd_model, messages=list)
        
        return result