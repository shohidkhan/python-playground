# cluster_config = {
#     "cluster_name": "dhaka-prod-east",
#     "total_max_slots": 8,
#     "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
# }


# def calculate_capacity(config):
#     # TODO: Calculate how many items are in the active_nodes list
#     active_nodes_count = len(config["active_nodes"])
#     print(f"Active Nodes Count: {active_nodes_count}")
#     total_slots = config["total_max_slots"]

    
#     for node in config["active_nodes"]:
#         utilization = (active_nodes_count / total_slots) * 100
#         print(f"Node: {node}, Utilization: {utilization}%")

# calculate_capacity(cluster_config)

cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}


def calculate_capacity(config):
    # Calculate how many items are in the active_nodes list
    active_nodes_count = len(config["active_nodes"])
    total_slots = config["total_max_slots"]

    # Utilization formula (ekbar-i hishab)
    utilization = (active_nodes_count / total_slots) * 100

    # Print the status statement
    print(f"Cluster Name: {config['cluster_name']}")
    print("Active Nodes:")
    for node in config["active_nodes"]:
        print(f"  - {node}")

    print(f"Active Nodes Count: {active_nodes_count}")
    print(f"Total Max Slots: {total_slots}")
    print(f"Utilization: {utilization:.1f}%")


calculate_capacity(cluster_config)