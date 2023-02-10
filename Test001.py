from schelling import Experiment
experiment = Experiment(20)
experiment.setUp(100)
experiment.iterate()
sim, happy, unhappy = experiment.getResultMatrix()
print(sim, happy, unhappy)