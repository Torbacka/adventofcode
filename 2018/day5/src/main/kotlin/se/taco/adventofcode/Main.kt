package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    var data: String = Files.readAllLines(Paths.get("src/main/resources/data.txt"))[0]
    var reductions = 1
    while (reductions > 0) {
        val reduce = reduce(data)
        data = reduce.second
        reductions = reduce.first
    }
    println(data.length)
}

fun reduce(data: String): Pair<Int, String> {
    val stringBuilder = StringBuilder()
    var reductions = 0
    var index = 0
    while (index < data.length) {
        if (index + 1 == data.length) {
            stringBuilder.append(data[index])
            break
        }
        if (data[index + 1].equals(data[index], true)) {
            if (data[index + 1].isUpperCase() && data[index].isLowerCase() ||
                data[index].isUpperCase() && data[index + 1].isLowerCase()
            ) {
                index++
                reductions++
            } else {
                stringBuilder.append(data[index])
            }
        } else {
            stringBuilder.append(data[index])
        }
        index++
    }
    return Pair(reductions, stringBuilder.toString())
}

