package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

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

    var schedule: Schedule? = null
    var schedules: MutableMap<Int, Schedule> = mutableMapOf()
    input.toSortedMap().forEach { localDateTime, info ->
        if (info.contains("Guard")) {
            schedule?.let {
                schedules[schedule!!.id] = schedule!!
            }
            var id = info.substringAfter("#").substringBefore(" ").toInt()

            schedule = if (schedules.containsKey(id)) {
                schedules[id]
            } else {
                Schedule(id, localDateTime, false)
            }
        } else {
            schedule!!.add(localDateTime, info)
        }
    }

    val maxBy = schedules.maxBy {
        it.value.sleeping_minutes.values.sum()
    }!!
    println("Id: ${maxBy.key},  ${maxBy.value.sleeping_minutes.maxBy { it.value }!!.key}")

}


data class Schedule(
    val id: Int,
    var last_date: LocalDateTime,
    var sleeping: Boolean,
    var awake_minutes: MutableMap<Int, Int> = mutableMapOf(),
    var sleeping_minutes: MutableMap<Int, Int> = mutableMapOf()
) {
    fun add(dateTime: LocalDateTime, data: String) {
        when (data) {
            "wakes up" -> {
                for (i in last_date.minute until dateTime.minute) {
                    if (sleeping_minutes.containsKey(i)) {
                        var numberOfTimes = sleeping_minutes[i]!!
                        sleeping_minutes[i] = ++numberOfTimes
                    } else {
                        sleeping_minutes[i] = 1
                    }
                }
                sleeping = false
            }
            "falls asleep" -> {
                for (i in last_date.minute until dateTime.minute) {
                    if (awake_minutes.containsKey(i)) {
                        var numberOfTimes = awake_minutes[i]!!
                        awake_minutes[i] = ++numberOfTimes
                    } else {
                        awake_minutes[i] = 1
                    }
                }

                sleeping = true
            }
        }
        last_date = dateTime
    }

}

