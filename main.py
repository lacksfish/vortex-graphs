from vortexgraph import VortexGraph


def main():
    # Initiate vortex graph in any number base
    vg = VortexGraph(base=10)
    # Connect the dots
    vg.connect_nodes()
    # Draw the vortex graph
    vg.draw_graph()
    input("Press ENTER to quit..")


if __name__ == "__main__":
    main()
