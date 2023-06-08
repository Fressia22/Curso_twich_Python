# Solución dada en Kotlin:

fun main() {
    println(checkRace(listOf(AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN), "_|_|_"))
    println(checkRace(listOf(AthleteState.RUN, AthleteState.RUN, AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN), "_|_|_"))
    println(checkRace(listOf(AthleteState.RUN, AthleteState.RUN, AthleteState.JUMP, AthleteState.JUMP, AthleteState.RUN), "_|_|_"))
    println(checkRace(listOf(AthleteState.RUN, AthleteState.RUN, AthleteState.JUMP, AthleteState.JUMP, AthleteState.RUN), "_|_|_|_"))
    println(checkRace(listOf(AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP), "_|_|_"))
    println(checkRace(listOf(AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN), "_|_|_"))
    println(checkRace(listOf(AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP), "|||||"))
    println(checkRace(listOf(AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP, AthleteState.JUMP), "||?||"))
}


private enum class AthleteState(val segment: String) {
    RUN("_"),
    JUMP("|")
}

private fun checkRace(athlete: List<AthleteState>, track: String) : Boolean {

    val totalActions = if (athlete.count() > track.count())  athlete.count() else track.count()
    val minActions = if (athlete.count() > track.count()) track.count() else athlete.count()

    val trackSegments = track.toList()

    var athleteTrack = ""

    for (index in (0 until totalActions)) {
        athleteTrack += if (index >= minActions) {
            "?"
        } else {
            val segment = trackSegments[index]
            when(val state = athlete[index]) {
                AthleteState.RUN -> if (segment.toString() == state.segment) state.segment else "/"
                AthleteState.JUMP -> if (segment.toString() == state.segment) state.segment else "x"
            }
        }
    }

    println(athleteTrack)

    return track == athleteTrack
}

