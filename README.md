## Automated Market Maker Simulator - With Hooks
A lightweight simulator for running experiments on Uniswap-style Automated Market Makers (AMMs) with support for configurable hooks (like dynamic fees). Designed for research, education, and strategy prototyping.

### Features
 - Modular hook system (like Uniswap v4's hooks)

 - YAML-configured simulations (no code changes needed)

 - Customizable trade patterns and oracle updates

 - Easy to extend with new hook strategies

### Installation
Clone the repository:

```bash
git clone https://github.com/your-username/automated-market-maker-simulator.git
cd automated-market-maker-simulator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

🛠️ Folder Structure
```graphql
.
├── simulator/                    # Main simulator package  
│   ├── amm_simulator.py         # Top-level simulation logic  
│   ├── core/                    # Core AMM + hook manager + types  
│   └── hooks/                   # Custom hook implementations  
├── simulation_configs/          # YAML config files  
│   └── initial_config.yaml      # Example config  
├── run_amm_sim.py               # Entrypoint to run the simulation  
└── README.md  

```