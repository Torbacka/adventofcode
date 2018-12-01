package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val values: IntArray = data.map { it.toInt() }.toIntArray()
    var calculatedSums: MutableSet<Int> = mutableSetOf()

    var sum: Int = 0
    var bool = true
    while(bool) {
        for (value in values) {
            sum += value
            if (calculatedSums.contains(sum)) {
                bool = false
                break
            } else {
                calculatedSums.add(sum)
            }
        }
    }
    println(sum)

}

