# Google-Self-driving-car-localizer
This is a simple algorithm that computes a possible location of a Robocar in motion.

Entropy of the robocar will decrease after the measurement update (sense) step and entropy will increase after movement step (move).

In general, entropy represents the amount of uncertainty in a system. Since the measurement update step decreases uncertainty, entropy will decrease. The movement step increases uncertainty, so entropy will increase after this step.

Looking at an example where the robot could be at one of five different positions. The maximum uncertainty occurs when all positions have equal probabilities [0.2, 0.2, 0.2, 0.2, 0.2][0.2,0.2,0.2,0.2,0.2]

Following the formula Entropy = \Sigma (-p \times log(p))Entropy=Σ(−p×log(p)), we get -5 \times (.2)\times log(0.2) = 0.699−5×(.2)×log(0.2)=0.699.

Taking a measurement will decrease uncertainty and entropy. Let's say after taking a measurement, the probabilities become [0.05, 0.05, 0.05, 0.8, 0.05][0.05,0.05,0.05,0.8,0.05]. Now we have a more certain guess as to where the robot is located and our entropy has decreased to 0.338.
