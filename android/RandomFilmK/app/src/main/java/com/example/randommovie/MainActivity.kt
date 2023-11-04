package com.example.randommovie

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.randommovie.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var moviesList: Array<String>
    private lateinit var displayedMovies: MutableList<String>
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        moviesList = resources.getStringArray(R.array.movies)
        displayedMovies = mutableListOf()
        binding.button.setOnClickListener { showRandomMovie() }
    }

    private fun showRandomMovie() {
        if (displayedMovies.size == moviesList.size) {
            binding.textView.text = getString(R.string.allMoviesViewed)
        } else {
            var randomMovie: String
            do {
                randomMovie = moviesList.random()
            } while (displayedMovies.contains(randomMovie))
            displayedMovies.add(randomMovie)
            binding.textView.text = randomMovie
        }
    }
}
