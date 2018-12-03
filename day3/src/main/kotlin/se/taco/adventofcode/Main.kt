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
    var points: MutableSet<Point> = mutableSetOf()
    var intersects = 0
    fabricList.forEachIndexed { index, fabric ->
        for (i in 1..(fabricList.size - 1)) {
            if (fabricList[i].rectangle.intersects(fabric.rectangle)) {
                val calculateIntersects = calculateIntersects(fabricList[i].rectangle, fabric.rectangle)
                intersects += calculateIntersects.size
                points.addAll(calculateIntersects)
            }
        }
    }
    println(intersects)
    println(points.size)
}

fun calculateIntersects(rectangle: Rectangle, rectangle2: Rectangle): Set<Point> {
    val intersection = rectangle.intersection(rectangle2)
    val points: MutableSet<Point> = mutableSetOf()

    for (x in (intersection.x..(intersection.width + intersection.x - 1))) {
        for (y in (intersection.y..(intersection.height + intersection.y - 1))) {
            points.add(Point(x, y))
        }
    }
    return points
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

