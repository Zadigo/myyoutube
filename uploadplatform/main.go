package main

import (
	"fmt"
	"encoding/json"
	"github.com/gorilla/websocket"
	"net/http"
)

// BaseMessage is the base structure for all messages
type BaseMessage struct {
	Action string `json:"action"`
}

// InitMessage is sent when a client starts an upload
type InitMessage struct {
    BaseMessage
    Data     []byte `json:"data"`
}

const  (
	ActionIdleConnect  string = "idle_connect"
	ActionUpload       string = "upload"
	ActionUploadComplete string = "upload_complete"
)

var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool {
       return true
    },
}

func ReadFileChunk(data []byte) {

}

func ParseMessage(message []byte) {
   var baseMessage BaseMessage

   err := json.Unmarshal(message, &baseMessage)
   if err != nil {
	  fmt.Println("Error unmarshaling base message:", err)
	  return
   }

   switch baseMessage.Action {
	   case ActionIdleConnect:
		   fmt.Println("Idle connect action received")
		case ActionUpload:
			break
	   default:
		   fmt.Printf("Unknown action: %s\n", baseMessage.Action)
   }
}

func UploadHandler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println("Error upgrading connection:", err)
		return
	}
	defer conn.Close()

	for {
       // Read message from the client
       _, message, err := conn.ReadMessage()

       if err != nil {
          fmt.Println("Error reading message:", err)
          break
       }
	   
	   ParseMessage(message)
	   
		// 	   fmt.Printf("Received: %s\\n", message)
		// 	   if err := conn.WriteMessage(websocket.TextMessage, message); err != nil {
		// 	      fmt.Println("Error writing message:", err)
		// 	      break
		// 	   }
    }
}

func main() {
	fmt.Println("WebSocket server started on :8080")
	http.HandleFunc("/ws/upload", UploadHandler)
	err := http.ListenAndServe(":8080", nil)

	if err != nil {
		fmt.Println("Error starting server:", err)
	}
}
