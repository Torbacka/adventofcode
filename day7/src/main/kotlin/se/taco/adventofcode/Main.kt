package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.util.*
import kotlin.concurrent.timer

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val graph = parseData(data)
    println(graph)
    var noIncomingEdge: PriorityQueue<String> = PriorityQueue()
    graph.incomingEdges
        .filter { it.value.size == 0 }
        .forEach {
            noIncomingEdge.add(it.key)
        }
    var time = 0
    while (noIncomingEdge.isNotEmpty()) {
        val node: String = noIncomingEdge.poll()
        time
    }
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
