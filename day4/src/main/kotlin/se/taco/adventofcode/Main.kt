package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    val input: MutableMap<LocalDateTime, String> = mutableMapOf()
    val formatter = DateTimeFormatter.ofPattern("yy-MM-dd HH:mm")
    for (line in data) {
        val date = line.substringAfter("[").substringBefore("]")
        input[LocalDateTime.parse(date.substring(2), formatter)] = line.substringAfter("] ")
    }

    input.toSortedMap().forEach { localDateTime, s ->
        println("Date: $localDateTime   data: $s")
    }
    var schedules: MutableMap<Int ,Schedule> = mutableMapOf()
    var last_date: LocalDateTime = LocalDateTime.now()
    var awake_minutes: Long = 0
    var sleep_minutes: Long = 0
    var id = 0
    input.toSortedMap().forEach { localDateTime, info ->
        when {
            info.contains("Guard") -> {
                awake_minutes += ChronoUnit.MINUTES.between(last_date, last_date.withHour(1).withMinute(0))

                if (schedules.containsKey(id)) {
                    var schedule = schedules[id]!!
                    schedule.awake_minutes += awake_minutes
                    schedule.sleep_minutes += sleep_minutes
                } else {
                    schedules[id] = Schedule(id, awake_minutes, sleep_minutes)
                }

                awake_minutes = 0
                sleep_minutes = 0
                id = info.substringAfter("#").substringBefore(" ").toInt()
            }
            info == "falls asleep" -> awake_minutes += ChronoUnit.MINUTES.between(last_date, localDateTime)

            info == "wakes up" -> sleep_minutes += ChronoUnit.MINUTES.between(last_date, localDateTime)

        }
        last_date = localDateTime

    }

    println(schedules.values.maxBy { it -> it.sleep_minutes })


}

data class Schedule(
    val id: Int,
    var awake_minutes: Long,
    var maxSleep: Long,
    var minute: Int,
    var sleep_minutes: Long
)
