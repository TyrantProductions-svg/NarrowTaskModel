
def hebbian_learning(
    synapse,
    learning_rate=0.01,
    min_weight=-1.0,
    max_weight=1.0
):
    # Get the activity of the connected neurons
    source_output = synapse.source.output
    target_output = synapse.target.output

    # Calculate how much the connection should change
    adjustment = learning_rate * source_output * target_output

    # Calculate the proposed new weight
    new_weight = synapse.weight + adjustment

    # Keep the weight within its permitted range
    new_weight = max(min_weight, min(max_weight, new_weight))

    # Calculate the actual change after applying the limits
    actual_adjustment = new_weight - synapse.weight

    # Update the synapse
    synapse.update_weight(actual_adjustment)

    return actual_adjustment
