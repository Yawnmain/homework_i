package com.example.color_tiles

import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import java.util.*

data class Coord(val x: Int, val y: Int)

class MainActivity : AppCompatActivity() {

    lateinit var tiles: Array<Array<View>>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tiles = arrayOf(
            arrayOf(findViewById(R.id.t00), findViewById(R.id.t01), findViewById(R.id.t02), findViewById(R.id.t03)),
            arrayOf(findViewById(R.id.t10), findViewById(R.id.t11), findViewById(R.id.t12), findViewById(R.id.t13)),
            arrayOf(findViewById(R.id.t20), findViewById(R.id.t21), findViewById(R.id.t22), findViewById(R.id.t23)),
            arrayOf(findViewById(R.id.t30), findViewById(R.id.t31), findViewById(R.id.t32), findViewById(R.id.t33))
        )

        initField()
    }

    fun getCoordFromString(s: String): Coord {
        val x = s.substring(0, 1).toInt()
        val y = s.substring(1, 2).toInt()
        return Coord(x, y)
    }

    fun changeColor(view: View) {
        val brightColor = resources.getColor(R.color.bright)
        val darkColor = resources.getColor(R.color.dark)
        val drawable = view.background as ColorDrawable
        if (drawable.color == brightColor) {
            view.setBackgroundColor(darkColor)
        } else {
            view.setBackgroundColor(brightColor)
        }
    }

    fun onClick(v: View) {
        val coord = getCoordFromString(v.tag.toString())
        changeColor(v)

        for (i in 0 until 4) {
            changeColor(tiles[coord.x][i])
            changeColor(tiles[i][coord.y])
        }

        checkVictory()
    }

    fun checkVictory() {
        val firstTileColor = (tiles[0][0].background as ColorDrawable).color

        for (i in 0 until 4) {
            for (j in 0 until 4) {
                val currentColor = (tiles[i][j].background as ColorDrawable).color
                if (currentColor != firstTileColor) {
                    return
                }
            }
        }

        Toast.makeText(this, "Поздравляю! Вы выиграли!", Toast.LENGTH_SHORT).show()
    }

    fun initField() {
        val brightColor = resources.getColor(R.color.bright)
        val darkColor = resources.getColor(R.color.dark)
        val random = Random()

        for (i in 0 until 4) {
            for (j in 0 until 4) {
                val randomNum = random.nextInt(2)
                if (randomNum == 0) {
                    tiles[i][j].setBackgroundColor(darkColor)
                } else {
                    tiles[i][j].setBackgroundColor(brightColor)
                }
            }
        }
    }
}
