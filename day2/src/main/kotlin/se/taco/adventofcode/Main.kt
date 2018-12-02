package se.taco.adventofcode

import java.nio.file.Files
import java.nio.file.Paths

fun main(args: Array<String>) {
    val data: List<String> = Files.readAllLines(Paths.get("src/main/resources/data.txt"))
    var words: MutableSet<String> = mutableSetOf()
    for (line in data) {
        val newWords = getWords(line)
        for (word in newWords) {
            if (words.contains(word)) {
                println(word)
            } else {
                words.add(word)
            }
        }
    }
}

fun getWords(word: String): Set<String> {
    var words: MutableSet<String> = mutableSetOf()
    for (i in (0..(word.length - 1))) {
        words.add(word.substring(0,i) + word.subSequence(i+1,word.length))
    }
    return words
}

