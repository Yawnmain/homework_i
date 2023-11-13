package com.example.s7

import android.os.Bundle
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.EditText
import android.widget.Spinner
import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity() {
    private lateinit var spinnerDeparture: Spinner
    private lateinit var spinnerArrival: Spinner
    private lateinit var editTextDepartureDate: EditText
    private lateinit var editTextArrivalDate: EditText
    private lateinit var editTextAdults: EditText
    private lateinit var editTextChildren: EditText
    private lateinit var editTextInfants: EditText
    private lateinit var btnSearch: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.layout)

        spinnerDeparture = findViewById(R.id.spinnerDeparture)
        spinnerArrival = findViewById(R.id.spinnerArrival)
        editTextDepartureDate = findViewById(R.id.editTextDepartureDate)
        editTextArrivalDate = findViewById(R.id.editTextArrivalDate)
        editTextAdults = findViewById(R.id.editTextAdults)
        editTextChildren = findViewById(R.id.editTextChildren)
        editTextInfants = findViewById(R.id.editTextInfants)
        btnSearch = findViewById(R.id.btnSearch)

        val cities = resources.getStringArray(R.array.city_array)
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, cities)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinnerDeparture.adapter = adapter
        spinnerArrival.adapter = adapter

        btnSearch.setOnClickListener {
            val departureCity = spinnerDeparture.selectedItem.toString()
            val arrivalCity = spinnerArrival.selectedItem.toString()
            val departureDate = editTextDepartureDate.text.toString()
            val arrivalDate = editTextArrivalDate.text.toString()
            val adults = editTextAdults.text.toString()
            val children = editTextChildren.text.toString()
            val infants = editTextInfants.text.toString()

            performSearch(departureCity, arrivalCity, departureDate, arrivalDate, adults, children, infants)
        }
    }

    private fun performSearch(
        departureCity: String,
        arrivalCity: String,
        departureDate: String,
        arrivalDate: String,
        adults: String,
        children: String,
        infants: String
    ) {
    }
}