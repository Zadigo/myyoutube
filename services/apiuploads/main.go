package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Welcome to the home page!")
}

func uploadWsHandler(w http.ResponseWriter, r *http.Request) {
	connection, error := upgrader.Upgrade(w, r, nil)

	if error != nil {
		fmt.Println("Error upgrading connection:", error)
		return
	}

	defer connection.Close()

	log.Printf("New WebSocket connection established from %s", connection.RemoteAddr())

	for {
		_, _, err := connection.ReadMessage()
		if err != nil {
			fmt.Println("Error reading message:", err)
			break
		}
	}
}

func main() {
	log.Println("Starting server on 0.0.0.0:14001")

	// Set up the routes
	http.HandleFunc("/", homePage)
	http.HandleFunc("/ws/upload", uploadWsHandler)

	// Start the server
	log.Fatal(http.ListenAndServe("0.0.0.0:14001", nil))
}
