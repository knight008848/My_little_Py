#http://www.codeskulptor.org/#user34_QnJIISmntm_21.py

"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookie = 0.0
        self._cps = 1.0
        self._game_time = 0.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Time:" + str(self._game_time) + ", Current Cookies:" + \
    str(self._current_cookie) + ", CPS:" + str(self._cps) + ", Total Cookies:" + str(self._total_cookies) + \
    " History (length:" + str(len(self._history)) + "): " + str(self._history)
        
    def get_cookies(self):
        """ 
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookie
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._game_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookie >= cookies:
            return 0.0
        else:
            plus_time = 0
            if ((cookies - self._current_cookie) % self._cps) > 0:
                plus_time = 1
            return ((cookies - self._current_cookie) // self._cps) + plus_time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time > 0:
            self._game_time += time
            self._current_cookie += self._cps * time
            self._total_cookies += self._cps * time #don't use current cookies
        return 0
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        
        if self._current_cookie >= cost:
            self._cps += additional_cps
            self._current_cookie -= cost
            self._history.append((self._game_time, item_name, cost, self._total_cookies))
        return 0
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """

    # Replace with your code
    new_build_info = build_info.clone()
    clicker_state = ClickerState()
    stop = False
    while ((clicker_state.get_time() <= duration) and (not stop)):
        time_left = duration - clicker_state.get_time()
        cps = clicker_state.get_cps()
        cookies = clicker_state.get_cookies()
        item = strategy(cookies, cps, time_left, new_build_info)
        if  item == None:
            break
        else:
            item_cost = new_build_info.get_cost(item)
            item_cps = new_build_info.get_cps(item)
            item_time = clicker_state.time_until(item_cost)
            if item_time <= time_left:
                clicker_state.wait(item_time)
                clicker_state.buy_item(item, item_cost, item_cps)
                new_build_info.update_item(item)
            else:
                stop = True
                clicker_state.wait(time_left)
    clicker_state.wait(duration - clicker_state.get_time())
    return clicker_state


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"

def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    this strategy should always select the cheapest item.
    """
    obj = build_info.clone()
    items = obj.build_items()
    the_item = items[0]
    for item in items:
        if obj.get_cost(item) < obj.get_cost(the_item):
            the_item = item
            
    if time_left < obj.get_cost(the_item) / (cps + obj.get_cps(the_item)):
        return None
    else:
        return the_item

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    this strategy should always select the most expensive item you can afford in the time left.
    """
    obj = build_info.clone()
    items = obj.build_items()
    the_item = items[0]
    for item in items:
        if obj.get_cost(item) >= obj.get_cost(the_item) and cookies >= obj.get_cost(item):
            the_item = item   
            
    if cookies < obj.get_cost(the_item) :
        return None
    else:
        return the_item


def strategy_best(cookies, cps, time_left, build_info):
    """
    this is the best strategy that you can come up with.
    """
    obj = build_info.clone()
    items = obj.build_items()
    the_item = items[0]
    for item in items:
        if (obj.get_cps(item) / obj.get_cost(item)) > (obj.get_cps(the_item) / obj.get_cost(the_item)):
            the_item = item   
            
    if time_left < obj.get_cost(the_item) / (cps + obj.get_cps(the_item)):
        return None
    else:
        return the_item
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

