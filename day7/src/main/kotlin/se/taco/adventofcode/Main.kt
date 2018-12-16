package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.util.*

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val graph = parseData(data)
    println(graph)
    var noIncomingEdge: PriorityQueue<String> = graph.findIncomingEdgesZero()
    var time = 0
    var numberOfWorkers = 2
    var tasks: MutableList<String> = mutableListOf()
    while (noIncomingEdge.isNotEmpty() or tasks.isNotEmpty()) {

        val node: String = noIncomingEdge.poll()
        graph.incomingEdges[node]
        if (noIncomingEdge.isNotEmpty() && tasks.size < numberOfWorkers) {

        } else {

        }
    }
}

fun <T> Graph<T>.removeEdges(node: T, noIncomingEdge: PriorityQueue<T>): PriorityQueue<T> {
    val iterator = this.outgoingEdges[node]!!.iterator()
    while (iterator.hasNext()) {
        val edge = iterator.next()
        iterator.remove()
        this.removeEdge(edge)
        if (this.incomingEdges[edge.fromNode]!!.isEmpty()) {
            noIncomingEdge.add(edge.fromNode)
        }
    }
    return noIncomingEdge
}

fun <T> Graph<T>.findIncomingEdgesZero(): PriorityQueue<T> {
    var noIncomingEdge: PriorityQueue<T> = PriorityQueue()
    this.incomingEdges
        .filter { it.value.size == 0 }
        .forEach {
            noIncomingEdge.add(it.key)
        }

    return noIncomingEdge
}

fun parseData(data: List<String>): Graph<String> {
    var graph: Graph<String> = Graph()
    for (c in 65..70) {
        graph.add(c.toChar().toString())
    }
    for (line in data) {
        val node = line.substringAfter("Step ").substringBefore(" ")
        val node2 = line.substringAfter("before step ").substringBefore(" can begin.")
        graph.connect(node, node2)
    }
    return graph
}
