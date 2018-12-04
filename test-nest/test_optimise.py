import pyNN.nest as pynn
import numpy as np
import volrpynn as v

pynn.setup()

def test_gradient_descent_optimiser():
    p1 = pynn.Population(2, pynn.IF_cond_exp())
    p2 = pynn.Population(1, pynn.IF_cond_exp())
    l = v.Dense(pynn, p1, p2, v.relu_derived)
    model = v.Model(pynn, l)
    optimiser = v.GradientDescentOptimiser(v.spike_softmax, 0.1)
    error = v.sum_squared_error
    xs = np.array([[1, 0], [0, 1], [1, 0]])
    ys = np.array([[1], [0], [1]])
    m, e = optimiser.train(model, xs, ys, error)
    assert np.allclose(e, np.array([0, 1, 0]))