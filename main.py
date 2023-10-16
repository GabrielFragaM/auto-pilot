from manager import Manager


class Simulation:
    def run_simulation(self, num_steps):
        for _ in range(num_steps):
            manager = Manager(chatgpd_key='XXX', chatgpd_model='gpt-3.5-turbo-16k')
            manager.get_solution(instructions='Como eu posso criar um script em python para avaliar gestoes da mão.')

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run_simulation(num_steps=1)
