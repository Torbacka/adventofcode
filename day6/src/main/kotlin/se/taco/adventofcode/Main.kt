package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    val data: MutableList<Pair<Int, Int>> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
        .map {
            val split = it.split(",")
            Pair(split[0].toInt(), split[1].trim().toInt())
        }.toMutableList()
    val results: MutableMap<Pair<Int, Int>, Pair<Int, Boolean>> = mutableMapOf()
    data.forEach {
        results[it] = Pair(0, false)
    }
    for (x in 0..400) {
        for (y in 0..400) {
            val sorted = data.map { Pair(it, Math.abs(it.first - x) + Math.abs(it.second - y)) }.sortedBy { it.second }
                .toMutableList()
            if (sorted[0].second == sorted[1].second) {
                continue
            }

            val first = sorted.first().first

            if (x == 0 || y == 0 || x == 400 || y == 400) {
                results[first] = Pair(results[first]!!.first.inc(), true)
            } else {
                results[first] = Pair(results[first]!!.first.inc(), results[first]!!.second)
            }
        }
    }

    println(results.filter { !it.value.second }.entries.sortedByDescending { it.value.first })


}

