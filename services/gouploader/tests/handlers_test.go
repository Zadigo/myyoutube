package tests

import (
	"fmt"
	"slices"
	"testing"
)

func TestHandlers(t *testing.T) {
	s := slices.Max([]int{1, 2, 3})
	fmt.Print(s)
}
