#include <WiFi.h>
#include <PubSubClient.h>
#include <Firebase_ESP_Client.h>
#include <addons/TokenHelper.h>
#include <Keypad.h>

// Replace the next variables with your SSID/Password combination
const char* ssid = "estrada";
const char* password = "ferestrada213";

#define ROW_NUM     4 // four rows
#define COLUMN_NUM  4 // four columns

int barr; 
String direc; 
int coll; 

char inputNumber[4] = {0};       // Array to store the input number
int currentIndex = 0;   
int number;         

char keys[ROW_NUM][COLUMN_NUM] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte pin_rows[ROW_NUM]      = {21, 19, 18, 5}; // GIOP19, GIOP18, GIOP5, GIOP17 connect to the row pins
byte pin_column[COLUMN_NUM] = {12, 26, 14, 15};   // GIOP16, GIOP4, GIOP0, GIOP2 connect to the column pins

Keypad keypad = Keypad( makeKeymap(keys), pin_rows, pin_column, ROW_NUM, COLUMN_NUM );


// Insert Firebase project API Key
#define API_KEY "AIzaSyAYHUhONVse4aLsBPpbSN1URs8KxTNdNgQ"//AIzaSyAjjTHMIV0y394tayvijhU-aVVcKdkIZxU//AIzaSyAjjTHMIV0y394tayvijhU-aVVcKdkIZxU

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://pryecto1-b58cc-default-rtdb.firebaseio.com/"

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;

bool signupOK = false;
int count = 0;

void setup() {
  Serial.begin(9600);
  delay(10);
  setup_wifi();

}

void setup_wifi() {
  //WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  //Serial.println("WiFi connected");
  //Serial.println("IP address: ");
  //Serial.println(WiFi.localIP());
  //* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    //Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}

void direccion(){
    if (Firebase.RTDB.getString(&fbdo, "Direction")){
      direc = fbdo.stringData(); 
      Serial.print(direc);      
    }  
}

void matrixTemp (){
  char key = keypad.getKey();

  if (key != NO_KEY) {
    // Check if key is a digit
    if (key >= '0' && key <= '9') {
      // Store the digit in the input number array
      inputNumber[currentIndex] = key;
      
      // Increment the current index
      currentIndex++;
      
      // Check if all digits have been entered
      if (currentIndex >= 2) {
        // Convert the input number to an integer
         number = atoi(inputNumber);
       
        // Reset the current index and input number array
        currentIndex = 0;
        memset(inputNumber, 0, sizeof(inputNumber));
      }
    }
  }

  Firebase.RTDB.setInt(&fbdo, "Matrix", number); 
}

void barrier(){
    barr = Serial.read(); 
    Firebase.RTDB.setInt(&fbdo, "Barrier", barr); 
}

void collision(){
    coll = Serial.read(); 
    Firebase.RTDB.setInt(&fbdo, "Collision", coll);
}

void loop() {
  //matrix(); 
  if (Firebase.ready() && signupOK && (millis() - sendDataPrevMillis >100 || sendDataPrevMillis == 0)) {
      sendDataPrevMillis = millis();
      direccion(); 
      collision(); 
      barrier(); 
      matrixTemp(); 
      //song(); 
  }
}
