import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, input_dims, n_actions, conv_units, in_channels=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=conv_units, kernel_size=(3,3), bias=False, padding=2)
        self.conv2 = nn.Conv2d(in_channels=conv_units, out_channels=conv_units, kernel_size=(3,3), bias=False, padding=1)
        self.conv3 = nn.Conv2d(in_channels=conv_units, out_channels=conv_units, kernel_size=(3,3), bias=False, padding=1)
        self.conv4 = nn.Conv2d(in_channels=conv_units, out_channels=conv_units, kernel_size=(3,3), bias=False, padding=1)

        self.flatten = nn.Flatten()

        fc_size = conv_units * (input_dims[-1]+2) * (input_dims[-2]+2)

        self.fc = nn.Linear(fc_size, n_actions)

    def forward(self, x):
        # conv area
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))

        x = self.flatten(x)
        # flatten area
        x = self.fc(x)

        return x