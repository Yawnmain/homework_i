package com.example.game

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onGuessClick(view: View) {
        val intent = Intent(this, GameActivity::class.java)

        val beginEditText = findViewById<EditText>(R.id.begin)
        val endEditText = findViewById<EditText>(R.id.end)

        val begin = beginEditText.text.toString().toIntOrNull() ?: 0
        val end = endEditText.text.toString().toIntOrNull() ?: 100

        intent.putExtra("begin", begin)
        intent.putExtra("end", end)
        startActivity(intent)
    }
}
