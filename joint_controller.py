from bge import logic
from math import radians

# Get object handles
cont = logic.getCurrentController()
beam = cont.owner
scene = logic.getCurrentScene()
base = scene.objects['Base']

# Mechanical feedback
rot = (beam.worldOrientation.transposed() * base.worldOrientation).to_euler()
T_theta = beam['K_theta'] * (rot[1] - radians(beam['theta_0'])) - \
          beam['C_theta'] * beam.getAngularVelocity(True)[1]
beam.applyTorque([0.0, T_theta, 0.0], True)