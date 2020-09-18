package main

import (
	"io"
	"net/http"
	"net/url"
	"os"
)

func main() {
	client := http.Client{}
	url, _ := url.Parse("http://localhost:32400/status/sessions")
	params := url.Query()
	params.Set("X-Plex-Token", "8xACJJEra1WzvnMAVkKw")
	url.RawQuery = params.Encode()
	response, _ := client.Get(url.String())
	io.Copy(os.Stdout, response.Body)
	defer response.Body.Close()
}
