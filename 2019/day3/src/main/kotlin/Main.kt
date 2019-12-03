import java.io.FileInputStream
import java.io.IOException

data class Point(
        var x: Int,
        var y: Int,
        var steps: Int
) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Point

        if (x != other.x) return false
        if (y != other.y) return false
        return true
    }

    override fun hashCode(): Int {
        var result = x
        result = 31 * result + y
        return result
    }
}

/**
 * main method for Kattis assignment.
 *
 * @param args probably never used.
 */
@Throws(IOException::class)
fun main(args: Array<String>) {
    FileInputStream("src/main/resources/testData.txt").use { fileInputStream ->
        val io = FastIO(fileInputStream)
        val points1: List<Point> = createPoints(io.getLine()!!)
        val points2: List<Point> = createPoints(io.getLine()!!)
        val setOfPoints: Set<Point> = HashSet(points2)
        val filtered = points1.filter { point -> setOfPoints.contains(point) }
        filtered.forEach { point -> points2.find { point == it }!!.also { point.steps += it.steps } }

        print(filtered.sortedBy { it.steps }.first().steps)

    }
}

fun createPoints(line: String): List<Point> {
    val splitData = line.split(",")
    val points: MutableList<Point> = mutableListOf()
    var steps = 0
    val previousPoint = Point(0, 0, steps)
    for (data in splitData) {
        val direction: Char = data[0]
        val length: Int = Integer.parseInt(data.substring(1))

        when (direction) {
            'R' -> {
                for (i in 1..length) {
                    points.add(Point(previousPoint.x + i, previousPoint.y, ++steps))
                }
                previousPoint.x += length
            }
            'L' -> {
                for (i in 1..length) {
                    points.add(Point(previousPoint.x - i, previousPoint.y, ++steps))
                }
                previousPoint.x -= length
            }
            'U' -> {
                for (i in 1..length) {
                    points.add(Point(previousPoint.x, previousPoint.y + i, ++steps))
                }
                previousPoint.y += length
            }
            'D' -> {
                for (i in 1..length) {
                    points.add(Point(previousPoint.x, previousPoint.y - i, ++steps))
                }
                previousPoint.y -= length
            }
        }
    }
    return points
}
