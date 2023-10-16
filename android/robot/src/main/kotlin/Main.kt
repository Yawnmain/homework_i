enum class Direction {
    UP, DOWN, LEFT, RIGHT
}

fun moveRobot(r: Robot, toX: Int, toY: Int) {
    while (r.x != toX || r.y != toY) {
        val dx = toX - r.x
        val dy = toY - r.y

        if (dx > 0) {
            while (r.direction != Direction.RIGHT) {
                r.turnRight()
            }
        } else if (dx < 0) {
            while (r.direction != Direction.LEFT) {
                r.turnLeft()
            }
        } else if (dy > 0) {
            while (r.direction != Direction.UP) {
                r.turnRight()
            }
        } else if (dy < 0) {
            while (r.direction != Direction.DOWN) {
                r.turnLeft()
            }
        }
        r.stepForward()
    }
}

fun printRobot(r: Robot) {
    println("${r}")
    println()
}

fun main() {
    val r = Robot(0, 0, Direction.RIGHT)

    println("Start position")
    printRobot(r)

    r.stepForward()
    println("Step Forward")
    printRobot(r)
}