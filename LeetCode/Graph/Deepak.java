import java.io.File;
import java.util.*;

class PowerGrid {
    private int time;
    private int[] low;
    private int[] discovery;
    private boolean[] visited;
    private int[] parent;
    private List<List<Integer>> graph;
    private List<int[]> bridges;

    int n; // number of cities
    List<List<Integer>> adjList; // adjacency list representation of the graph
    Map<Integer, String> cityMap;

    PowerGrid(String filename) throws Exception {
        Scanner in = new Scanner(new File(filename));
        n = in.nextInt();
        int m = in.nextInt();
        
        // initialize adjacency list and city map
        adjList = new ArrayList<>();
        cityMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            String cityName = in.next();
            cityMap.put(i, cityName);
        }
        
        // add edges to the adjacency list
        for (int i = 0; i < m; i++) {
            String city1 = in.next();
            String city2 = in.next();
            int u = cityMap.entrySet().stream().filter(e -> e.getValue().equals(city1)).findFirst().get().getKey();
            int v = cityMap.entrySet().stream().filter(e -> e.getValue().equals(city2)).findFirst().get().getKey();
            adjList.get(u).add(v);
            adjList.get(v).add(u); // for undirected graph
        }
    }



    public List<int[]> findBridges(List<List<Integer>> graph) {
        this.graph = graph;
        int n = graph.size();
        time = 0;
        low = new int[n];
        discovery = new int[n];
        visited = new boolean[n];
        parent = new int[n];
        bridges = new ArrayList<>();
        Arrays.fill(parent, -1);
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }
        return bridges;
    }

    private void dfs(int u) {
        visited[u] = true;
        low[u] = discovery[u] = ++time;
        for (int v : graph.get(u)) {
            if (!visited[v]) {
                parent[v] = u;
                dfs(v);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > discovery[u]) {
                    bridges.add(new int[]{u, v});
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], discovery[v]);
            }
        }
    }
}


public class Deepak {
    public static void main(String[] args) throws Exception{    
        PowerGrid powerGrid = 
    }
}