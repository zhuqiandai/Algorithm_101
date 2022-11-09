using System.Collections.Generic;
using static System.Console;

namespace GraphBase;

/// <summary>
/// Graph 数据结构
/// </summary>
public class Graph
{
    public enum VerColor
    {
        WHITE = 0,
        GREY = 1,
        BLACK = 2,
    }

    private bool _isDerected;
    private List<string> _vertices;
    private Dictionary<string, List<string>> _adtices;

    private Dictionary<string, VerColor> _color;

    public Graph(bool isDerected = false)
    {
        this._isDerected = isDerected;
        this._vertices = new List<string> { };
        this._adtices = new Dictionary<string, List<string>> { };

        this._color = new Dictionary<string, VerColor> { };
    }

    public void addVertex(string vertex)
    {
        int index = this._vertices.IndexOf(vertex);

        if (index == -1)
        {
            this._vertices.Add(vertex);

            List<string> edges = new List<string> { };
            this._adtices.Add(vertex, edges);
        }
    }

    public void addEdge(string vertexa, string vertexb)
    {
        int index = this._vertices.IndexOf(vertexa);

        if (index == -1)
        {
            this.addVertex(vertexa);
        }

        if (this._adtices.ContainsKey(vertexb) == true)
        {
            this.addVertex(vertexb);
        }

        this._adtices[vertexa].Add(vertexb);

        if (!this._isDerected)
        {
            this._adtices[vertexb].Add(vertexa);
        }
    }

    public List<string> vertices
    {
        get
        {
            return this._vertices;
        }
    }

    public Dictionary<string, List<string>> adtices
    {
        get
        {
            return this._adtices;
        }
    }

    public Dictionary<string, VerColor> colors
    {
        get
        {
            return this._color;
        }
    }


    private void PaintWhite()
    {
        foreach (string ele in this._vertices)
        {
            this._color[ele] = VerColor.WHITE;
        }
    }

    public static void BFS(Graph g, string s)
    {
        Queue<string> queue = new Queue<string> { };

        // paint all vertex to white
        g.PaintWhite();

        // source vertex operate
        g.colors[s] = Graph.VerColor.GREY;
        queue.Enqueue(s);

        WriteLine(queue);

        while (queue.Count != 0)
        {
            string u = queue.Dequeue();
            WriteLine($"current bfs node is {u}");

            List<string> es = g.adtices[u];

            foreach (string e in es)
            {
                if (g.colors[e] == Graph.VerColor.WHITE)
                {
                    g.colors[e] = Graph.VerColor.GREY;
                    queue.Enqueue(e);
                }
            }

            g.colors[u] = Graph.VerColor.BLACK;
        }

    }

    private static void DFS_V(Graph g, string u)
    {
        WriteLine($"current dfs node is {u}");
        g.colors[u] = Graph.VerColor.GREY;

        List<string> es = g.adtices[u];
        foreach (string e in es)
        {
            if (g.colors[e] == Graph.VerColor.WHITE)
            {
                DFS_V(g, e);
            }
        }

        g.colors[u] = Graph.VerColor.BLACK;
    }

    public static void DFS(Graph g)
    {
        // paint all vertex to white
        g.PaintWhite();

        foreach (string s in g.vertices)
        {
            if (g.colors[s] == Graph.VerColor.WHITE)
            {
                Graph.DFS_V(g, s);
            }
        }
    }
}
