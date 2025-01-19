using System;
using System.Speech.Recognition;
using System.Speech.Synthesis;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;
using System.Net.Http;

class Program
{
    static async Task Main(string[] args)
    {
        string openaiKey = ""; // replace with your OpenAI API key

        // Create an instance of the speech recognizer
        var recognizer = new SpeechRecognitionEngine();

        // Create an instance of the speech synthesizer
        var synth = new SpeechSynthesizer();

        // Create a grammar that only recognizes the word "Vironica"
        var grammar = new GrammarBuilder("Vironica");
        recognizer.LoadGrammar(new Grammar(grammar));

        // Set the input to the default audio device
        recognizer.SetInputToDefaultAudioDevice();

        // Start listening for speech input
        Console.WriteLine("Listening for 'Vironica' command...");
        while (true)
        {
            // Listen for speech input
            var result = recognizer.Recognize();

            if (result.Text == "Vironica")
            {
                // Speak the prompt to ask question
                synth.Speak("What is your question?");
                // Listen for question
                var question = recognizer.Recognize();
                Console.WriteLine("You said: " + question.Text);

                // Send query to OpenAI API
                var client = new HttpClient();
                client.DefaultRequestHeaders.Add("Authorization", "Bearer " + openaiKey);

                var response = await client.PostAsync("https://api.openai.com/v1/engines/davinci/completions", new StringContent(
                    "{\"prompt\":\"" + question.Text + "\",\"engine\":\"davinci\",\"temperature\": 0.5,\"max_tokens\":2048,\"top_p\":1,\"frequency_penalty\":0,\"presence_penalty\":0}",
                    System.Text.Encoding.UTF8, "application/json"));

                var responseString = await response.Content.ReadAsStringAsync();
                dynamic json = JObject.Parse(responseString);
                Console.WriteLine("OpenAI response: " + json.choices[0].text);
                // Speak the answer
                synth.Speak(json.choices[0].text);
            }
        }
    }
}
