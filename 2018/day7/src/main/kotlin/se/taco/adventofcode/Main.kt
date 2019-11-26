@file:Suppress("SENSELESS_COMPARISON")

package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.util.*

fun main() {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val graph = parseData(data)
    println(graph)
    var noIncomingEdge: PriorityQueue<String> = graph.findIncomingEdgesZero()
    var time = 0
    var numberOfWorkers = 2
    var tasks: MutableMap<String, Int> = mutableMapOf()
    var taskString: String = ""
    while (noIncomingEdge.isNotEmpty() or tasks.isNotEmpty()) {
        var node: String? = null

        val iterator = tasks.iterator()
        while (iterator.hasNext()) {
            val task: MutableMap.MutableEntry<String, Int> = iterator.next()
            val finishTime: Int = task.key[0].minus(64).toInt() + 60 + task.value
            if (time >= finishTime) {
                noIncomingEdge = graph.removeEdges(task.key, noIncomingEdge)
                iterator.remove()

            }
        }

        if (noIncomingEdge.isNotEmpty() && tasks.size < numberOfWorkers) {
            node = noIncomingEdge.poll()
            tasks[node] = time
            taskString += node
            val freeTasks = numberOfWorkers - tasks.size

            for (i in 1..freeTasks) {
                if (noIncomingEdge.isNotEmpty()) {
                    node = noIncomingEdge.poll()
                    tasks[node] = time
                    taskString += node
                }
            }
        }
        time++
    }
    print(taskString)
    print((time - 1))
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
    val noIncomingEdge: PriorityQueue<T> = PriorityQueue()
    this.incomingEdges
        .filter { it.value.size == 0 }
        .forEach {
            noIncomingEdge.add(it.key)
        }

    return noIncomingEdge
}

fun parseData(data: List<String>): Graph<String> {
    var graph: Graph<String> = Graph()
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
