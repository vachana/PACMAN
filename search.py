# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Stack = util.Stack()
    # VisitedCells = []
    # StartCell = problem.getStartState()
    # StartPair = (StartCell, [])
    # Stack.push(StartPair)
    # while not Stack.isEmpty():
    #     CurrentPair = Stack.pop()
    #     CurrentCell = CurrentPair[0]
    #     DirectionsToCell = CurrentPair[1]
    #     if problem.isGoalState(CurrentCell):
    #         print(DirectionsToCell)
    #     return DirectionsToCell
    # else:
    #     if CurrentCell not in VisitedCells:
    #         VisitedCells.append(CurrentCell)
    #         SuccessorList = problem.getSuccessors(CurrentCell)
    #         for Triplet in SuccessorList:
    #             Stack.push((Triplet[0], DirectionsToCell + [Triplet[1]]))
    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited.
    stackVal = util.Stack()
    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()
    # Initialize the Starting Pair, which could be something like ([3,2], []). In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartPair = (StartCell, [])
    stackVal.push(StartPair)
    # VisitedCells = {StartCell}
    VisitedCells = set()
    while not stackVal.isEmpty():
        CurrentPair = stackVal.pop()
        CurrentCell, DirectionsToCell = CurrentPair
        VisitedCells.add(CurrentCell)
        if problem.isGoalState(CurrentCell):
            print(DirectionsToCell)
            return DirectionsToCell

        SuccessorList = problem.getSuccessors(CurrentCell)
        for cell, direction, _ in SuccessorList:
            if cell not in VisitedCells:
                # VisitedCells.add(cell)
                stackVal.push((cell, DirectionsToCell + [direction]))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Initialize the queue using the already-built in util.py package.
    Queue = util.Queue()
    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited.
    VisitedCells = []
    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()
    # Initialize the Starting Pair, which could be something like ([3,2], []). In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartPair = (StartCell, [])
    Queue.push(StartPair)
    while not Queue.isEmpty():
        CurrentPair = Queue.pop()
        CurrentCell = CurrentPair[0]
        DirectionsToCell = CurrentPair[1]
        if problem.isGoalState(CurrentCell):
            print(DirectionsToCell)
            return DirectionsToCell
        else:
            if CurrentCell not in VisitedCells:
                VisitedCells.append(CurrentCell)
                SuccessorList = problem.getSuccessors(CurrentCell)
                for Triplet in SuccessorList:
                    Queue.push((Triplet[0], DirectionsToCell + [Triplet[1]]))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """Search the shallowest nodes in the search tree first."""
    # Initialize the queue using the already-built in util.py package.
    pQueue = util.PriorityQueue()
    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited.

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()
    # Initialize the Starting Pair, which could be something like ([3,2], []). In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartPair = (StartCell, [], 0)
    pQueue.push(StartPair, 0)
    # VisitedCells = {StartCell}
    VisitedCells = {StartCell: 0}
    while not pQueue.isEmpty():
        CurrentPair = pQueue.pop()
        CurrentCell, DirectionsToCell, costSoFar = CurrentPair
        if problem.isGoalState(CurrentCell):
            print(DirectionsToCell)
            return DirectionsToCell

        SuccessorList = problem.getSuccessors(CurrentCell)
        for cell, direction, cost in SuccessorList:
            if cell not in VisitedCells or cost + costSoFar < VisitedCells[cell]:
                # VisitedCells += (Triplet[0]),
                VisitedCells[cell] = cost + costSoFar
                pQueue.push((cell, DirectionsToCell + [direction], cost + costSoFar), cost + costSoFar)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    pQueue = util.PriorityQueue()
    # Initialize the set of Visited Cells, which we use to keep track of which cells we've visited.

    # Get the Starting Cell, using the command that is already built into the project.
    StartCell = problem.getStartState()
    # Initialize the Starting Pair, which could be something like ([3,2], []). In other words, the
    # start cell is [3,2] and the second entry is [] since we don't have to do anything to get to [3,2].
    StartPair = (StartCell, [], 0)
    pQueue.push(StartPair, 0)

    VisitedCells = {StartCell: 0}
    while not pQueue.isEmpty():
        CurrentPair = pQueue.pop()
        CurrentCell, DirectionsToCell, costSoFar = CurrentPair
        if problem.isGoalState(CurrentCell):
            print(DirectionsToCell)
            return DirectionsToCell

        SuccessorList = problem.getSuccessors(CurrentCell)
        for cell, direction, cost in SuccessorList:
            if cell not in VisitedCells or cost + costSoFar < VisitedCells[cell]:
                # VisitedCells += (Triplet[0]),
                VisitedCells[cell] = cost + costSoFar
                pQueue.push((cell, DirectionsToCell + [direction], cost + costSoFar),
                            cost + costSoFar + heuristic(cell, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
