from app.simulator import Simulator


def main():
    sim = Simulator(num_nodes=3)
    sim.insert_keys(1000)
    sim.report_distribution()
    
    sim.add_node()
    print("\nAfter adding a node:")
    sim.report_distribution()

    sim.remove_node(1)
    print("\nAfter removing a node:")
    sim.report_distribution()

if __name__ == "__main__":
    main()