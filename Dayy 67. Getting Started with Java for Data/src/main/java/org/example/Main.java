package org.example;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.FileReader;

class WeatherData {
    // TODO: implement the WeatherData class (see Exercise 2)
    private String date;
    private double temperature;
    private double humidity;

    public WeatherData(String data, double temperature, double humidity){
        this.date = date;
        this.temperature = temperature;
        this.humidity = humidity;
    }

    public String getDate () {
        return date;
    }

    public double getTemperature() {
        return temperature;
    }

    public double getHumidity() {
         return humidity;
    }

    public boolean isHotDay () {
        return temperature > 30;
    }

    public boolean isHumidDay() {
        return humidity > 70;
    }
}


// This is the main class of our Weather Data Analyzer program
public class Main {

    // The main method is the entry point of any Java application
    public static void main(String[] args) {
        // Greet the user and explain what the program does
        System.out.println("Welcome to the Weather Data Analyzer!");

        // 1. Call the method for the first exercise: basic data types and variable assignment
        System.out.println("###### Exercise 1 ######");
        basicDataTypesExercise();

        // 2. Call the method for the second exercise: creating the WeatherData class
        System.out.println("###### Exercise 2 ######");
        createWeatherDataClass();

        // 3. Call the method for the third exercise: creating and using a WeatherData object
        System.out.println("###### Exercise 3 ######");
        createWeatherDataObject();

        // 4. Call the method for the fourth exercise: analyzing a single day's weather
        System.out.println("###### Exercise 4 ######");
        analyzeSingleDayWeather();

        // 5. Call the method for the fifth exercise: working with an array of WeatherData objects
        System.out.println("###### Exercise 5 ######");
        analyzeMultipleDaysWeather();

        // 6. Call the method for the sixth exercise: reading weather data from a CSV file
        System.out.println("###### Exercise 6 ######");
        analyzeWeatherDataFromCSV();
    }

    /**
     * Exercise 1: Basic Data Types and Variable Assignment
     * <p>
     * In this exercise, you'll get familiar with basic Java data types (e.g., int, double, String)
     * and learn how to assign values to variables.
     * <p>
     * Follow these steps:
     * - Declare an integer variable named `dayNumber` and assign it the value 12.
     * - Declare a double variable named `temperature` and assign it the value 28.5.
     * - Declare a String variable named `weatherDescription` and assign it the value "Sunny".
     * - Print each of these variables to the console.
     */
    public static void basicDataTypesExercise() {
        // TODO: Declare and assign values to variables
        int dayNumber = 12;
        double temperature = 28.5;
        String weatherDescription = "Sunny";

        System.out.println("Day number: " + dayNumber);
        System.out.println("Temperature: " + temperature);
        System.out.println("Weather description: " + weatherDescription);
    }

    /**
     * Exercise 2: Create the WeatherData Class
     * <p>
     * In this exercise, you'll create a class called WeatherData that represents the weather data for a single day.
     * <p>
     * A class in Java is a blueprint for creating objects. It can contain fields (variables) and methods (functions).
     * The WeatherData class should have the following fields:
     * - `date` (String): the date of the weather data
     * - `temperature` (double): the temperature on that day
     * - `humidity` (double): the humidity on that day
     * <p>
     * Follow these steps:
     * - Create a new class named `WeatherData`.
     * - Add the fields `date`, `temperature`, and `humidity` as instance variables.
     * - Write a constructor that takes in values for these fields and assigns them to the instance variables.
     * - Generate getter methods for each of the fields to allow other classes to access the data.
     * <p>
     * (Note: The actual implementation of this exercise will be in the class defined above)
     */
    public static void createWeatherDataClass() {
        // TODO: Implement the WeatherData class above
    }

    /**
     * Exercise 3: Create and Use a WeatherData Object
     * <p>
     * In this exercise, you will create an instance (object) of the WeatherData class and use it to store and retrieve weather data.
     * <p>
     * Follow these steps:
     * - In this method, create a WeatherData object using the constructor.
     * - Pass in a date, temperature, and humidity when creating the object.
     * - Use the getter methods to retrieve the values from the object and print them to the console.
     */
    public static void createWeatherDataObject() {
        // TODO: Create a WeatherData object and print its values
        WeatherData weatherData = new WeatherData(data: "2025-04-08", temperature: 36.0, humidity: 75.0);
        System.out.println("Date: ", + weatherData.getDate());
        System.out.println("Temperature: " + weatherData.getTemperature());
        System.out.println("Humidity: " + weatherData.getHumidity());
    }

    /**
     * Exercise 4: Analyze a Single Day's Weather
     * <p>
     * In this exercise, you'll add methods to the WeatherData class to analyze the weather data.
     * <p>
     * Follow these steps:
     * - Add a method `isHotDay()` in the WeatherData class that returns true if the temperature is above 30 degrees.
     * - Add a method `isHumidDay()` in the WeatherData class that returns true if the humidity is above 70%.
     * - In this method, create a WeatherData object and use the new methods to analyze the weather.
     * - Print out whether it is a hot day and/or a humid day.
     */
    public static void analyzeSingleDayWeather() {
        // TODO: Implement the isHotDay() and isHumidDay() methods in the WeatherData class
        WeatherData weatherData = new WeatherData(data: "2025-04-08", temperature: 36.0, humidity: 75.0);
        System.out.println("Is hot day?: " + weatherData.isHotDay());
        System.out.println("Is humid day?: " + weatherData.isHumidDay());

    }

    /**
     * Exercise 5: Analyze Multiple Days of Weather
     * <p>
     * In this exercise, you'll work with an array of WeatherData objects and calculate the average temperature.
     * <p>
     * Follow these steps:
     * - Create an array of WeatherData objects representing different days.
     * - Implement the method in the Main class called `calculateAverageTemperature` that takes an array of WeatherData objects and returns the average temperature.
     * - In this method, create an array of WeatherData objects, call `calculateAverageTemperature`, and print the result.
     */
    public static void analyzeMultipleDaysWeather() {
        // TODO: Create an array of WeatherData objects and implement a method to calculate the average temperature
        WeatherData[] data = { 
            new WeatherData(data: "2025-04-08", temperature: 36.0, humidity:75.0)
            new WeatherData(data: "2025-04-09", temperature: 28.0, humidity:70.0)
            new WeatherData(data: "2025-04-10", temperature: 24.0, humidity:65.0)
        };

        double averageTemp = calculateAverageTemperature(data);
        System.out.println("Average temperature: " + averageTemp);
    }

    /**
     * Helper Method: Calculate the Average Temperature
     * <p>
     * This method takes an array of WeatherData objects and returns the average temperature.
     */
    public static double calculateAverageTemperature(WeatherData[] data) {
        double sum = 0;
        for (WeatherData day: data) {
            sum += day.getTemperature();
        }
        return sum / data.length;
    }

    /**
     * Exercise 6: Read Weather Data from a CSV File
     * <p>
     * In this exercise, you'll read weather data from a CSV file and analyze it.
     * <p>
     * Follow these steps:
     * - Write a method in the Main class called `readWeatherDataFromCSV` that reads data from a CSV file and creates an array of WeatherData objects.
     * - In this method, call `readWeatherDataFromCSV` to read data from a sample CSV file and analyze it by calculating the average temperature.
     * - Print the average temperature from the CSV data to the console.
     */
    public static void analyzeWeatherDataFromCSV() {
        // TODO: Implement the readWeatherDataFromCSV method and analyze the data
        WeatherData[] csvData = readWeatherDataFromCSV(fileName: "weather_data.csv");
        double averageTemperature = calculateAverageTemperature(csvData);
        System.out.println("Average temperature from CSV: " + averageTemperature);
    }

    /**
     * Helper Method: Read Weather Data from a CSV File
     * <p>
     * This method reads data from a CSV file and returns an array of WeatherData objects.
     */
    public static WeatherData[] readWeatherDataFromCSV(String fileName) {
        // TODO: Implement the logic to read from a CSV file
        ArrayList<WeatherData> weatherDataList = new ArrayList<>();
        
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            //Skip
            br.readLine();

            while ((line = br.readLine()) != null) {
                // Split line into fields
                String [] splitLine = line.split(regex: ",");

                // Extract the values
                String date =  splitLine[0];
                double temperature = Double.parseDouble(splitLine[1]);
                double humidity = Double.parseDouble(splitLine[2]);

                WeatherData weatherData = new WeatherData(data, temperature, humidity);
                weatherDataList.add(weatherData);
            }
            
        }
        catch (IOException e){
            System.out.println("An error occurred " + e.getMessage());
        }

        return weatherDataList.toArray(new WeatherData[0]);
    }
}
