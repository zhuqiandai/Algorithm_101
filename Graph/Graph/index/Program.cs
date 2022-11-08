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
        }
    }
}
