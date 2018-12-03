package se.taco.adventofcode

import java.awt.Rectangle
import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val table: Array<Array<Int>> = Array(1001) { Array(1001) {0} }

    for (line in data) {
        val fabric = parseFabric(line)
        for (i in 0 until fabric.rectangle.width) {
            for (n in 0 until fabric.rectangle.height) {
                table[fabric.rectangle.x + i][fabric.rectangle.y + n]++
            }
        }
    }
    for (i in 0..1000) {
        for (n in 0..1000) {
            print(table[i][n])
        }
        println()
    }
    var total = 0
    for (i in 0..1000) {
        for (n in 0..1000) {
            if (table[i][n] > 1) {
                total++
            }
        }
    }

    println(total)

}


fun parseFabric(line: String): Fabric {
    val firstSplit = line.split("@")
    val id = firstSplit[0].replace("#", "").trim().toInt()
    val secondSplit = firstSplit[1].split(":")
    val thirdSplit = secondSplit[0].trim().split(",")
    val fourth = secondSplit[1].trim().split("x")
    /*val points: MutableList<Point> = mutableListOf()

    for (x in (thirdSplit[0].toInt()..fourth[0].toInt())) {
        for (y in (thirdSplit[1].toInt()..fourth[1].toInt())) {
            points.add(Point(x, y))
        }
    }*/
    return Fabric(id, Rectangle(thirdSplit[0].toInt(), thirdSplit[1].toInt(), fourth[0].toInt(), fourth[1].toInt()))
}

data class Fabric(
    val id: Int,
    val rectangle: Rectangle
)

