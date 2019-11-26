package se.taco.adventofcode

import java.util.*

data class Edge<T>(
    val toNode: T,
    val fromNode: T
)

data class Graph<T>(
    var outgoingEdges: MutableMap<T, MutableList<Edge<T>>> = mutableMapOf(),
    var incomingEdges: MutableMap<T, MutableList<Edge<T>>> = mutableMapOf()
) {

    fun add(node: T) {
        outgoingEdges[node] = mutableListOf()
        incomingEdges[node] = mutableListOf()
    }

    fun connect(node1: T, node2: T) {
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

    fun removeEdge(edge: Edge<T>) {
        outgoingEdges[edge.toNode]!!.remove(edge)
        incomingEdges[edge.fromNode]!!.remove(edge)
    }

    fun removeEdge(node: T, node2: T) {
        outgoingEdges[node]!!.remove(Edge(node, node2))
        incomingEdges[node2]!!.remove(Edge(node, node2))
    }

    fun remove(node: T) {
        outgoingEdges.remove(node)
        incomingEdges.remove(node)
    }
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

fun topologicallySort(graph: Graph<String>): List<String> {
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
