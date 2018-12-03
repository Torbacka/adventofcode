package se.taco.adventofcode

import java.awt.Point
import java.awt.Rectangle
import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val fabricList: MutableList<Fabric> = mutableListOf()
    for (line in data) {
        fabricList.add(parseFabric(line))
    }
    var intersects: MutableSet<Int> = mutableSetOf()

    fabricList.forEachIndexed { index, fabric ->
        for (i in 0..fabricList.lastIndex) {
            if (fabric == fabricList[i]) {
                continue
            }
            if (fabric.rectangle.intersects(fabricList[i].rectangle)) {
                intersects.add(fabric.id)
            }
        }
    }
    println(fabricList.filter { !intersects.contains(it.id) })

}

fun parseFabric(line: String): Fabric {
    val firstSplit = line.split("@")
    val id = firstSplit[0].replace("#", "").trim().toInt()
    val secondSplit = firstSplit[1].split(":")
    val thirdSplit = secondSplit[0].trim().split(",")
    val fourth = secondSplit[1].trim().split("x")
    return Fabric(id, Rectangle(thirdSplit[0].toInt(), thirdSplit[1].toInt(), fourth[0].toInt(), fourth[1].toInt()))
}

data class Fabric(
    val id: Int,
    val rectangle: Rectangle
)

