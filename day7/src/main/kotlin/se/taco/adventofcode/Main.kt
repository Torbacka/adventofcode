package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.util.*

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val parseData = parseData(data)
    val topologicallySort = topologicallySort(parseData)
    topologicallySort.forEach { print(it) }


}

fun parseData(data: List<String>): Graph {
    var graph: Graph = Graph()
    for (c in 65..90) {
        graph.add(c.toChar().toString())
    }
    for (line in data) {
        val node = line.substringAfter("Step ").substringBefore(" ")
        val node2 = line.substringAfter("before step ").substringBefore(" can begin.")
        graph.connect(node, node2)
    }
    return graph
}

/*
L ← Empty list that will contain the sorted elements
S ← Set of all outgoingEdges with no incoming edge
while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error   (graph has at least one cycle)
else
    return L   (a topologically sorted order)
 */

fun topologicallySort(graph: Graph): List<String> {
    var sortedElements: MutableList<String> = mutableListOf()
    var noIncomingEdge: PriorityQueue<String> = PriorityQueue()
    graph.incomingEdges
        .filter { it.value.size == 0 }
        .forEach {
        noIncomingEdge.add(it.key)
    }

    while (noIncomingEdge.isNotEmpty()) {
        val node = noIncomingEdge.poll()
        sortedElements.add(node)
        val iterator = graph.outgoingEdges[node]!!.iterator()
        while (iterator.hasNext()) {
            val edge = iterator.next()
            iterator.remove()
            graph.removeEdge(edge)
            if (graph.incomingEdges[edge.fromNode]!!.isEmpty()) {
                noIncomingEdge.add(edge.fromNode)
            }
        }
        println(graph)

    }
    return sortedElements

}


/*
L ← Empty list that will contain the sorted elements
S ← Set of all outgoingEdges with no incoming edge
while S is non-empty do
    remove a node n from S
    add n to tail of L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S
if graph has edges then
    return error   (graph has at least one cycle)
else
    return L   (a topologically sorted order)
 */

data class Edge(
    val toNode: String,
    val fromNode: String
)

data class Graph(
    var outgoingEdges: MutableMap<String, MutableList<Edge>> = mutableMapOf(),
    var incomingEdges: MutableMap<String, MutableList<Edge>> = mutableMapOf()
) {

    fun add(node: String) {
        outgoingEdges[node] = mutableListOf()
        incomingEdges[node] = mutableListOf()
    }

    fun connect(node1: String, node2: String) {
        if (!outgoingEdges.containsKey(node1)) {
            outgoingEdges[node1] = mutableListOf(Edge(node1, node2))
            incomingEdges[node2] = mutableListOf(Edge(node1, node2))
        } else {
            outgoingEdges[node1]!!.add(Edge(node1, node2))
            if (!incomingEdges.containsKey(node2)) {
                incomingEdges[node2] = mutableListOf(Edge(node1, node2))
            } else {
                incomingEdges[node2]!!.add(Edge(node1, node2))
            }
        }
    }

    fun removeEdge(edge: Edge) {
        outgoingEdges[edge.toNode]!!.remove(edge)
        incomingEdges[edge.fromNode]!!.remove(edge)
    }

    fun removeEdge(node: String, node2: String) {
        outgoingEdges[node]!!.remove(Edge(node, node2))
        incomingEdges[node2]!!.remove(Edge(node, node2))
    }

    fun remove(node: String) {
        outgoingEdges.remove(node)
        incomingEdges.remove(node)
    }
}


