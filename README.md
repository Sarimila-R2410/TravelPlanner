# Travel Planner

#### Video Demo: https://youtu.be/Sgts_0rXPh8?si=Clvc0UlrRY8nwP88

#### Description:
Travel Planner is a Python-based application designed to help users plan travel routes to famous destinations inspired by the anime One Piece. The program calculates the shortest travel route between various attractions and provides detailed information on travel time, transportation modes, and costs.

Using a graph-based approach, the system efficiently computes the shortest travel routes through the use of Dijkstra's Algorithm implemented with the heapq priority queue. It supports both an intuitive user interface and an easy-to-navigate structure for both route calculation and data display.

The system supports:
- Calculating the shortest route between two destinations.
- Displaying travel data in a structured format.
- An easy-to-use interface where users can input starting and destination points.


## Files:

- **project.py**: This is the main file that contains the logic of the travel planner. It defines the core functions that manage the graph of attractions, calculate the shortest route between destinations, and display the travel data in a tabular format.

- **test_project.py**: Contains test cases that verify the correctness of the functions defined in `project.py`. The tests are designed to check that the travel planner works as expected and returns the correct shortest route and travel details.


## Design Choices:

- **Graph Representation**: I used an undirected graph to represent the travel routes between the attractions. Each node in the graph is an attraction, and each edge represents a travel route with details such as travel time, transportation mode, and cost.

- **Shortest Path Algorithm**: The application uses a modified version of Dijkstra’s algorithm, implemented using a priority queue (`heapq`), to find the shortest route between the start and destination points based on travel time.

- **Data Display**: I used the `tabulate` module to display travel details in a clean and readable format, which makes it easy to compare travel times, costs, and transportation modes for each route.

## Installation Instructions:

To install and run Travel Planner on your system, follow these steps:

Clone the repository:
git clone <your-repository-url>
cd <project-directory>

Install the dependencies:
pip install -r requirements.txt

Run the program:
python project.py
pytest test_project.py
