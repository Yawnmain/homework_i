package com.example.randommovie

data class Movie(
    val title: String,
    val genre: String,
    val year: Int,
    val actors: List<String>,
    val director: String,
    val rating: Double
)
