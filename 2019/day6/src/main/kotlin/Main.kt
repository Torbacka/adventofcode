import java.io.FileInputStream
import java.io.IOException


/**
 * main method for Kattis assignment.
 *
 * @param args probably never used.
 */
@Throws(IOException::class)
fun main(args: Array<String>) {
    FileInputStream("src/main/resources/input.txt").use { fileInputStream ->
        val io = FastIO(fileInputStream)
        val input: MutableMap<String, MutableList<String>> = mutableMapOf()
        while (io.hasMoreTokens()) {
            val data: List<String> = io.getLine()!!.split(")")
            if (input.containsKey(data[0])) {
                input[data[0]]!!.add(data[1])
            } else {
                input[data[0]] = mutableListOf(data[1])
            }

        }
        val tree = Tree(buildTree(Node("COM", null, mutableListOf()), input))

        println("Part1: ${count(0, "COM", 0, input)}")
        println("Part2: ${tree.shortestPath(tree.find("YOU")!!, tree.find("SAN")!!)}")
    }
}

fun buildTree(currentNode: Node, input: MutableMap<String, MutableList<String>>): Node {
    if (input.containsKey(currentNode.value)) {
        for (next: String in input[currentNode.value]!!) {
            currentNode.children.add(buildTree(Node(next, currentNode, mutableListOf()), input))
        }
    }
    return currentNode
}

fun count(count: Int, current: String, currentLevel: Int, input: MutableMap<String, MutableList<String>>): Int {
    var currentCount = count + currentLevel
    if (input.containsKey(current)) {
        for (next: String in input[current]!!) {
            currentCount += count(count, next, currentLevel + 1, input)
        }
    }
    return currentCount
}


data class Tree(
        val root: Node
) {
    fun add(parent: String, child: String) {
        val parentNode: Node = find(parent) ?: throw RuntimeException("Halt and catch fire!!!")
        parentNode.children.add(Node(child, parentNode, mutableListOf()))
    }

    fun find(value: String): Node? {
        return findRecursive(root, value)
    }

    fun shortestPath(node1: Node, node2: Node): Int {
        return shortestPathRecursive(node1, 0, node2)
    }

    private fun shortestPathRecursive(node1: Node, i: Int, node2: Node): Int {
        var next1 = node1.parent!!
        var next2 = node2.parent!!
        var currentStep = i
        if (findRecursive(node1, node2.value) !=  null) {
            next1 = node1
            currentStep -=1
        }
        if (findRecursive(node2, node1.value) !=  null) {
            next2 = node2
            currentStep -= 1
        }

        return when {
            node1.parent!! == node2.parent!! -> currentStep - 1
            node1.parent == node2 -> currentStep
            node1 == node2.parent -> currentStep
            else -> {
                shortestPathRecursive(next1, currentStep + 2, next2)
            }
        }
    }

    private fun findRecursive(current: Node, value: String): Node? {
        if (value == current.value) {
            return current
        }
        var found: Node? = null
        for (node: Node in current.children) {
            found = findRecursive(node, value)
            if (found != null) {
                break
            }
        }
        return found

    }

    override fun toString(): String {
        return root.value
    }

}

data class Node(
        val value: String,
        val parent: Node?,
        val children: MutableList<Node>
)