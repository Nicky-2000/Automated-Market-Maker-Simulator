import yaml
from simulator.amm_simulator import AMMSimulator

if __name__ == "__main__":
    with open("simulation_configs/initial_config.yaml", "r") as file:
        config = yaml.safe_load(file)

    sim = AMMSimulator(config)
    sim.run()