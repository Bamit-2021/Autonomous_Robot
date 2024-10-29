import matplotlib.pyplot as plt
import time

# Warehouse dimensions
WAREHOUSE_WIDTH = 10  # in meters
WAREHOUSE_HEIGHT = 10  # in meters

# Robot properties
SPEED = 0.1  # meters per second
PAUSE_TIME = 2  # seconds
STEP_DURATION = 0.1  # seconds

class Robot:
    def __init__(self, start_x, start_y, dest_x, dest_y):
        self.x = start_x
        self.y = start_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.path = [(self.x, self.y)]
    
    def move(self):
        while (self.x, self.y) != (self.dest_x, self.dest_y):
            # Calculate direction vector to the destination
            dx = self.dest_x - self.x
            dy = self.dest_y - self.y
            
            # Normalize the direction vector
            distance = (dx**2 + dy**2)**0.5
            if distance == 0:
                break  # Reached destination
            
            # Calculate step size
            step_x = (dx / distance) * SPEED * STEP_DURATION
            step_y = (dy / distance) * SPEED * STEP_DURATION
            
            # Update position
            self.x += step_x
            self.y += step_y
            
            # Add to path for visualization
            self.path.append((self.x, self.y))
            
            # Display movement
            self.plot_movement()
            
            # Simulate movement and stop
            time.sleep(STEP_DURATION)
            time.sleep(PAUSE_TIME)

    def plot_movement(self):
        plt.clf()
        plt.plot(*zip(*self.path), marker='o', color='b', markersize=4, label="Path")
        plt.plot(self.dest_x, self.dest_y, 'go', label="Destination")
        plt.xlim(0, WAREHOUSE_WIDTH)
        plt.ylim(0, WAREHOUSE_HEIGHT)
        plt.legend()
        plt.pause(0.1)


def run_simulation():
    # Initialize robot at start position (0, 0) with destination (7, 9)
    robot = Robot(start_x=0, start_y=0, dest_x=7, dest_y=9)
    
    # Start the movement
    plt.ion()  # Enable interactive plotting
    robot.move()
    plt.ioff()  # Disable interactive plotting
    plt.show()  # Show the final path


if __name__ == "__main__":
    run_simulation()
