# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
This class outlines the structure of a search problem, but doesn't implement
any of the methods (in object-oriented terminology: an abstract class).

You do not need to change anything in this class, ever.
"""

    def getStartState(self):
        """
Returns the start state for the search problem
"""
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
state: Search state

Returns True if and only if the state is a valid goal state
"""
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
state: Search state

For a given state, this should return a list of triples,
(successor, action, stepCost), where 'successor' is a
successor to the current state, 'action' is the action
required to get there, and 'stepCost' is the incremental
cost of expanding to that successor
"""
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
actions: A list of actions to take

This method returns the total cost of a particular sequence of actions. The sequence must
be composed of legal moves
"""
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
Returns a sequence of moves that solves tinyMaze. For any other
maze, the sequence of moves will be incorrect, so only use this for tinyMaze
"""
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
Search the deepest nodes in the search tree first

Your search algorithm needs to return a list of actions that reaches
the goal. Make sure to implement a graph search algorithm

To get started, you might want to try some of these simple commands to
understand the search problem that is being passed in:
"""
    # closed is a dictionary of nodes {Coordinates, movelist}
    closed = {}
    fringe = util.Stack()

    # the node currently expanded
    expanded = problem.getStartState()
    closed[expanded] = []
    while not problem.isGoalState(expanded):
        #if successors exist, pursue them. otherwise, remove the last move from the list.
        successors = problem.getSuccessors(expanded)
        for successor in successors:
            if successor[0] not in closed:
                # push the tuple containing the coordinates, and a list of directions to reach this node.
                movelist = list(closed[expanded])
                movelist.append(successor[1])
                fringe.push((successor[0], movelist))
        #expand the next node
        if not fringe.isEmpty():
            nextnode = fringe.pop()
            expanded = nextnode[0]

            # add the node the the set of visited nodes
            closed[expanded] = nextnode[1]

    return closed[expanded]

def breadthFirstSearch(problem):
    
    # closed is a dictionary of nodes {Coordinates, movelist}
    closed = {}
    fringe = util.PriorityQueue()

    # the node currently expanded
    expanded = problem.getStartState()
    closed[expanded] = []
    depth = 1

    while not problem.isGoalState(expanded):
        #if successors exist, pursue them. otherwise, remove the last move from the list.
        successors = problem.getSuccessors(expanded)
        for successor in successors:
            if successor[0] not in closed:
                # push the tuple containing the coordinates, and a list of directions to reach this node.
                movelist = list(closed[expanded])
                movelist.append(successor[1])
                fringe.push((successor[0], movelist, depth+1), depth+1)
                closed[successor[0]] = []


        #expand the next node
        if not fringe.isEmpty():
            nextnode = fringe.pop()
            depth = nextnode[2]
            expanded = nextnode[0]

            # add the node the the set of visited nodes
            closed[expanded] = nextnode[1]

    return closed[expanded]

def uniformCostSearch(problem):
    
    # closed is a dictionary of nodes {Coordinates, movelist}
    closed = {}
    fringe = util.PriorityQueue()

    # the node currently expanded
    expanded = problem.getStartState()
    closed[expanded] = []
    exp_cost = 0
    while not problem.isGoalState(expanded):
        #if successors exist, pursue them. otherwise, remove the last move from the list.
        successors = problem.getSuccessors(expanded)
        for successor in successors:
            if successor[0] not in closed:
                # push the tuple containing the coordinates, and a list of directions to reach this node.
                movelist = list(closed[expanded])
                movelist.append(successor[1])
                fringe.push((successor[0], movelist, exp_cost+successor[2]), exp_cost+successor[2])
        #expand the next node
        if not fringe.isEmpty():
            nextnode = fringe.pop()
            exp_cost = nextnode[2]
            expanded = nextnode[0]

            # add the node the the set of visited nodes
            closed[expanded] = nextnode[1]


    return closed[expanded]


def nullHeuristic(state, problem=None):
    """
A heuristic function estimates the cost from the current state to the nearest
goal in the provided SearchProblem. This heuristic is trivial.
"""
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    
    # closed is a dictionary of nodes {Coordinates, movelist}
    closed = {}
    fringe = util.PriorityQueue()

    # the node currently expanded
    expanded = problem.getStartState()
    closed[expanded] = []
    exp_cost = 0
    nextnode = (expanded)
    visited = []
    while not problem.isGoalState(expanded):
        #if successors exist, pursue them. otherwise, remove the last move from the list.
        if nextnode[0] in visited:
            nextnode = fringe.pop()
            exp_cost = nextnode[2]
            expanded = nextnode[0]

            # add the node the the set of visited nodes
            closed[expanded] = nextnode[1]
            continue
        successors = problem.getSuccessors(expanded)
        
        visited.append(nextnode[0])
        
        # print("successors: " + str(successors))
        #print("closed:"+str(closed))
        for successor in successors:
            if successor[0] not in closed:
                # push the tuple containing the coordinates, and a list of directions to reach this node.

                movelist = list(closed[expanded])
                movelist.append(successor[1])

                fringe.push((successor[0], movelist, exp_cost+successor[2]), exp_cost+successor[2]+heuristic(successor[0],problem))
                #closed[successor[0]]=[]


        #expand the next node
        if not fringe.isEmpty():

            nextnode = fringe.pop()

            exp_cost = nextnode[2]
            expanded = nextnode[0]

            # add the node the the set of visited nodes
            closed[expanded] = nextnode[1]

    return closed[expanded]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch