# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

from ps2_verify_movement27 import testRobotMovement

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    temp=[]
    """
        A RectangularRoom represents a rectangular region containing clean or dirty
        tiles.
        
        A room has a width and a height and contains (width * height) tiles. At any
        particular time, each of these tiles is either clean or dirty.
        """
    def __init__(self, width, height):
        """
            Initializes a rectangular room with the specified width and height.
            
            Initially, no tiles in the room have been cleaned.
            
            width: an integer > 0
            height: an integer > 0
            """
        self.width=width
        self.height=height
        self.cleanedTiles = []
    def cleanTileAtPosition(self, pos):
        """
            Mark the tile under the position POS as cleaned.
            
            Assumes that POS represents a valid position inside this room.
            
            pos: a Position
            """
        # gets the x,y coordinates of the position and converts to integer. Integer x,y values represent the current tile.
        tile = (int(pos.getX()),int(pos.getY()))
        # if the title is not already cleaned, it is recorded as cleaned.
        if not tile in self.cleanedTiles:
            self.cleanedTiles.append(tile)



def isTileCleaned(self, m, n):
    """
        Return True if the tile (m, n) has been cleaned.
        
        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
            return (m,n) in self.cleanedTiles

        def getNumTiles(self):
        """
            Return the total number of tiles in the room.
            
            returns: an integer
            """
        self.total=self.width*self.height
                return self.total

def getNumCleanedTiles(self):
    """
        Return the total number of clean tiles in the room.
        
        returns: an integer
        """
            return len(self.cleanedTiles)

        def getRandomPosition(self):
        """
            Return a random position inside the room.
            
            returns: a Position object.
            """
        positionx=range(0,self.width)
        positiony=range(0,self.height)
        self.pos=Position(random.choice(positionx),random.choice(positiony))
                return self.pos

def isPositionInRoom(self, pos):
    """
        Return True if pos is inside the room.
        
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
            return 0<=pos.getX()<self.width and 0<=pos.getY()<self.height


class RectangularRoom(object):
    temp=[]
    """
        A RectangularRoom represents a rectangular region containing clean or dirty
        tiles.
        
        A room has a width and a height and contains (width * height) tiles. At any
        particular time, each of these tiles is either clean or dirty.
        """
    def __init__(self, width, height):
        """
            Initializes a rectangular room with the specified width and height.
            
            Initially, no tiles in the room have been cleaned.
            
            width: an integer > 0
            height: an integer > 0
            """
        self.width=width
        self.height=height
        self.cleanedTiles = []
    def cleanTileAtPosition(self, pos):
        """
            Mark the tile under the position POS as cleaned.
            
            Assumes that POS represents a valid position inside this room.
            
            pos: a Position
            """
        # gets the x,y coordinates of the position and converts to integer. Integer x,y values represent the current tile.
        tile = (int(pos.getX()),int(pos.getY()))
        # if the title is not already cleaned, it is recorded as cleaned.
        if not tile in self.cleanedTiles:
            self.cleanedTiles.append(tile)



def isTileCleaned(self, m, n):
    """
        Return True if the tile (m, n) has been cleaned.
        
        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
            return (m,n) in self.cleanedTiles

        def getNumTiles(self):
        """
            Return the total number of tiles in the room.
            
            returns: an integer
            """
        self.total=self.width*self.height
                return self.total

def getNumCleanedTiles(self):
    """
        Return the total number of clean tiles in the room.
        
        returns: an integer
        """
            return len(self.cleanedTiles)

        def getRandomPosition(self):
        """
            Return a random position inside the room.
            
            returns: a Position object.
            """
        positionx=range(0,self.width)
        positiony=range(0,self.height)
        self.pos=Position(random.choice(positionx),random.choice(positiony))
                return self.pos

def isPositionInRoom(self, pos):
    """
        Return True if pos is inside the room.
        
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
            return 0<=pos.getX()<self.width and 0<=pos.getY()<self.height

class Robot(object):
    """
        Represents a robot cleaning a particular room.
        
        At all times the robot has a particular position and direction in
        the room.  The robot also has a fixed speed.
        
        Subclasses of BaseRobot should provide movement strategies by
        implementing updatePositionAndClean(), which simulates a single
        time-step.
        """
    def __init__(self, room, speed):
        """
            Initializes a Robot with the given speed in the specified
            room. The robot initially has a random direction d and a
            random position p in the room.
            
            The direction d is an integer satisfying 0 <= d < 360; it
            specifies an angle in degrees.
            
            p is a Position object giving the robot's position.
            
            room:  a RectangularRoom object.
            speed: a float (speed > 0)
            """
        assert type(speed)== float,'Speed should be a float'
        self.room = room
        self.speed = speed
        self.d = random.randrange(360)
        self.p = self.room.getRandomPosition()
    
    
    def getRobotPosition(self):
        """
            Return the position of the robot.
            
            returns: a Position object giving the robot's position.
            """
        return self.p
    
    def getRobotDirection(self):
        """
            Return the direction of the robot.
            
            returns: an integer d giving the direction of the robot as an angle in
            degrees, 0 <= d < 360.
            """
        return self.d
    
    def setRobotPosition(self, position):
        """
            Set the position of the robot to POSITION.
            
            position: a Position object.
            """
        self.p = position
    
    def setRobotDirection(self, direction):
        """
            Set the direction of the robot to DIRECTION.
            
            direction: integer representing an angle in degrees
            """
        self.d = direction
    
    
    def updatePositionAndClean(self):
        """
            Simulate the raise passage of a single time-step.
            
            Move the robot to a new position and mark the tile it is on as having
            been cleaned.
            """
        raise NotImplementedError


# === Problem 2
class StandardRobot(Robot):
    
    def updatePositionAndClean(self):
        """
            Simulate the passage of a single time-step.
            
            Move the robot to a new position and mark the tile it is on as having
            been cleaned.
            """
        # the next position is calculated with respect to given speed and direction
        newPosition = self.p.getNewPosition(self.d,self.speed)
        
        
        # if the next position is within the room,
        if self.room.isPositionInRoom(newPosition):
            
            # the robot is moved to the next position and,
            self.setRobotPosition(newPosition)
            # the tile underneath is cleaned,
            self.room.cleanTileAtPosition(newPosition)
        #else if next position is outside the room, the direction of the robot is changed
        else:
            self.setRobotDirection(random.randrange(360))
            self.room.cleanTileAtPosition(self.p)


testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
        Runs NUM_TRIALS trials of the simulation and returns the mean number of
        time-steps needed to clean the fraction MIN_COVERAGE of the room.
        
        The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
        speed SPEED, in a room of dimensions WIDTH x HEIGHT.
        
        num_robots: an int (num_robots > 0)
        speed: a float (speed > 0)
        width: an int (width > 0)
        height: an int (height > 0)
        min_coverage: a float (0 <= min_coverage <= 1.0)
        num_trials: an int (num_trials > 0)
        robot_type: class of robot to be instantiated (e.g. StandardRobot or
        RandomWalkRobot)
        """
    trialsList = []
    
    # Run num_trials amount of tests
    for trial in range(num_trials):
        room = RectangularRoom(width,height)
        botList = []
        for n in range(num_robots):
            botList.append(robot_type(room,speed))
        steps = 0
        ## While the room is not cleaned enough: Let all bots have another 'turn'
        while (1.0*room.getNumCleanedTiles()/room.getNumTiles()) <= min_coverage:
            for bot in botList:

                bot.updatePositionAndClean()
            steps += 1

        trialsList.append(steps)

    return float(sum(trialsList)) / len(trialsList)

print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    
    def updatePositionAndClean(self):
        
        self.room.cleanTileAtPosition(self.getRobotPosition())
        self.setRobotDirection(random.randrange(360))
        newPosition = self.p.getNewPosition(self.d,self.speed)
        
        
        # if the next position is within the room,
        if self.room.isPositionInRoom(newPosition):
            
            # the robot is moved to the next position and,
            self.setRobotPosition(newPosition)
            # the tile underneath is cleaned,
            self.room.cleanTileAtPosition(newPosition)
        #else if next position is outside the room, the direction of the robot is changed
        else:
            self.setRobotDirection(random.randrange(360))
            self.room.cleanTileAtPosition(self.p)


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
