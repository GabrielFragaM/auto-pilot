
from agent import Agent
from services.chatgpt import call_chatgpd
import json
import re
import time

class Manager:
    def __init__(self, chatgpd_key, chatgpd_model):
       self.chatgpd_key = chatgpd_key
       self.chatgpd_model = chatgpd_model

    def format_tasks(self, text):
        default = r'\d+\.\s+(.*?)(?=\d+\.|\Z)'
        tasks = re.findall(default, text, re.DOTALL)

        return [task.strip() for task in tasks]

    def get_solution(self, instructions):
        agent = Agent(chatgpd_key=self.chatgpd_key, chatgpd_model=self.chatgpd_model)
        
        list = []
        list.append({"role": "system", "content": 'Você é um Gerente, com base no que se pede você deverá retornar uma lista de tarefas numeradas sobre o assunto para a solução.'})
        list.append({"role": "user", "content": f'Para o assunto: {instructions}. Retorne uma lista de tarefas numeradas.'})
      
        result = call_chatgpd(api_key=self.chatgpd_key, model=self.chatgpd_model, messages=list)
   
        tasks = self.format_tasks(text=result)

        solutions = []
 
        for task in tasks:
            solution = agent.get_solution(instructions=task)
            solutions.append({
                'tarefa': task,
                'solução': solution
            })
            time.sleep(5)

        print(json.dumps(solutions))
        result = agent.build_tasks(instructions=instructions, solutions=json.dumps(solutions))
        print('\n\n\n===========================================\n\n\n')
        print(result)
        return result