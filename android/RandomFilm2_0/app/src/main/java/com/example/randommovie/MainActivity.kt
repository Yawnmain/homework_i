package com.example.randommovie

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.randommovie.databinding.ActivityMainBinding
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.InputStreamReader

class MainActivity : AppCompatActivity() {

    private lateinit var moviesList: List<Movie>
    private lateinit var displayedMovies: MutableList<Movie>
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        moviesList = loadMoviesFromJson()
        displayedMovies = mutableListOf()
        binding.button.setOnClickListener { showRandomMovie() }
    }

    private fun loadMoviesFromJson(): List<Movie> {
        val inputStream = resources.openRawResource(R.raw.movies)
        val reader = InputStreamReader(inputStream)
        val type = object : TypeToken<List<Movie>>() {}.type
        return Gson().fromJson(reader, type)
    }

    private fun showRandomMovie() {
        if (displayedMovies.size == moviesList.size) {
            binding.textView.text = getString(R.string.allMoviesViewed)
        } else {
            var randomMovie: Movie
            do {
                randomMovie = moviesList.random()
            } while (displayedMovies.contains(randomMovie))
            displayedMovies.add(randomMovie)
            binding.textView.text = randomMovie.title
        }
    }
}
