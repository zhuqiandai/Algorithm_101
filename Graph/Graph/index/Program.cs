using static System.Console;
using GraphBase;

namespace ProgramExe
{
    class Program
    {
        public static void Main()
        {

            Graph g = new Graph();

            List<string> myVertices = new List<string> { "A", "B", "C", "D", "E", "F", "G", "H", "I" };


            foreach (string ver in myVertices)
            {
                g.addVertex(ver);
            }

            foreach (string ver in g.vertices)
            {
                WriteLine("vertex is {0}", ver);
            }

            g.addEdge("A", "B");
            g.addEdge("A", "C");
            g.addEdge("A", "D");
            g.addEdge("C", "D");
            g.addEdge("C", "G");
            g.addEdge("D", "G");
            g.addEdge("D", "H");
            g.addEdge("B", "E");
            g.addEdge("B", "F");
            g.addEdge("E", "I");


            foreach (KeyValuePair<string, List<string>> ele in g.adtices)
            {
                WriteLine("edge key is {0} -->", ele.Key);
                foreach (string item in ele.Value)
                {
                    WriteLine("{0}", item);
                }
            }
        }
    }
}
