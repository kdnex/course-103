import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Base64;

public class WordPressPageCreation {
    public static void main(String[] args) {

        // Specify the name of the environment variable you want to read
        String WP_USERNAME = System.getenv("WP_USERNAME");

        if (WP_USERNAME != null) {
            System.out.println("WP_USERNAME: " + WP_USERNAME);
        } else {
            System.out.println("WP_USERNAME: is not set.");
            System.exit(1);;
        }

        String WP_KEY = System.getenv("WP_KEY");

        if (WP_KEY != null) {
            System.out.println("WP_KEY: read");
        } else {
            System.out.println("WP_KEY: is not set.");
            System.exit(1);;
        }

        String BASE_URL = "https://toddbooth.com/wp-json/wp/v2";

        // URL for creating a new page
        String createPageUrl = BASE_URL + "/pages/";

        try {
            // Create a URL object
            URL url = new URL(createPageUrl);

            // Open a connection to the URL
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();

            // Set the request method to POST
            connection.setRequestMethod("POST");

            // Set up basic authentication
            String userCredentials = WP_USERNAME + ":" + WP_KEY;
            String basicAuth = "Basic " + Base64.getEncoder().encodeToString(userCredentials.getBytes());
            connection.setRequestProperty("Authorization", basicAuth);

            // Set the request headers
            connection.setRequestProperty("Content-Type", "application/json");

            // Enable input/output streams
            connection.setDoOutput(true);

            // Create JSON data for the new page
            String jsonData = "{"
                    + "\"title\": \"Just a Random Page Title - 2632\","
                    + "\"content\": \"This is the content of the new page - 2632.\","
                    + "\"status\": \"publish\""
                    + "}";

            // Write the JSON data to the request body
            try (DataOutputStream outputStream = new DataOutputStream(connection.getOutputStream())) {
                outputStream.writeBytes(jsonData);
                outputStream.flush();
            }

            // Get the HTTP response code
            int responseCode = connection.getResponseCode();

            // Read and print the response from the server
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                StringBuilder response = new StringBuilder();
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                System.out.println("Response Code: " + responseCode);
                // System.out.println("Response Data: " + response.toString());

                // check if the response code is 201
                if (responseCode == 201) {
                    System.out.println("Page created successfully.");
                    System.exit(0);
                } else {
                    System.out.println("Page creation failed.");
                    System.exit(1);
                }
            }

            // Close the connection
            connection.disconnect();
            System.exit(0);

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
        finally {
            System.out.println("Done.");
        }
    }
}
