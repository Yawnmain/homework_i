package com.example.game

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class GameActivity : AppCompatActivity() {
    private var begin: Int = 0
    private var end: Int = 100
    private var guess: Int = 0
    private lateinit var tvQuestion: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game)
        begin = intent.getIntExtra("begin", 0)
        end = intent.getIntExtra("end", 100)
        guessNumber()
    }

    private fun guessNumber() {
        guess = (begin + end) / 2
        tvQuestion = findViewById(R.id.question)
        tvQuestion.text = "Ваше число больше или равно $guess?"
    }


    fun onYesNoClick(view: View) {
        when (view.id) {
            R.id.yes -> handleAnswer(true)
            R.id.no -> handleAnswer(false)
        }
    }

    private fun handleAnswer(isYes: Boolean) {
        if (isYes) {
            begin = guess
        } else {
            end = guess
        }

        if (end - begin > 1) {
            guessNumber()
        } else {
            end = end - 1
            showResult()
        }
    }



    private fun showResult() {
        tvQuestion.text = "Ваше число: $end"
        disableButtons()
    }

    private fun disableButtons() {
        val btnYes = findViewById<Button>(R.id.yes)
        val btnNo = findViewById<Button>(R.id.no)
        btnYes.isEnabled = false
        btnNo.isEnabled = false
    }
}
