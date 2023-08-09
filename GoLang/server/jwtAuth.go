package main

import (
	"fmt"
	"time"

	"github.com/dgrijalva/jwt-go"
)

const (
	SECRET_KEY = "F9BNdSJqoV0j+YuEq0erYXp+/eY7rAVU9+U+AFHzy3w="
)

func encodeJWT(payload map[string]interface{}) (string, error) {
	token := jwt.New(jwt.SigningMethodHS256)
	claims := token.Claims.(jwt.MapClaims)
	claims["clientId"] = payload["clientId"]
	claims["exp"] = time.Now().Add(time.Hour * 24).Unix() // Token expiration time, adjust as needed

	tokenString, err := token.SignedString([]byte(SECRET_KEY))
	return tokenString, err
}

func decodeJWT(tokenString string) (map[string]interface{}, error) {
	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return []byte(SECRET_KEY), nil
	})

	if err != nil {
		return nil, err
	}

	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		payload := map[string]interface{}{
			"clientId": claims["clientId"],
		}
		return payload, nil
	} else {
		return nil, fmt.Errorf("invalid token")
	}
}

func main() {
	payload := map[string]interface{}{"clientId": "456434"}

	token, err := encodeJWT(payload)
	if err != nil {
		fmt.Println("Error encoding token:", err)
		return
	}

	fmt.Println("Token:", token)

	decodedPayload, err := decodeJWT(token)
	if err != nil {
		fmt.Println("Error decoding token:", err)
		return
	}

	fmt.Println("Payload:", decodedPayload)
}
