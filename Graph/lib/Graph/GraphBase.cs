using System.Collections.Generic;

namespace GraphBase;

public class Graph
{
    private bool _isDerected;
    private List<string> _vertices;
    private Dictionary<string, List<string>> _adtices;

    public Graph(bool isDerected = false)
    {
        this._isDerected = isDerected;
        this._vertices = new List<string> { };
        this._adtices = new Dictionary<string, List<string>> { };

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
}
