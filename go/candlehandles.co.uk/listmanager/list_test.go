package listmanager

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func createEmptyTestList() GiftList {
	allowedProducts := []string{"testProduct1", "testProduct2", "testProduct3", "testProduct4"}
	return GiftList{
		AllowedProducts: allowedProducts,
		Entries:         map[string]bool{},
	}
}
func createFullTestList() GiftList {
	allowedProducts := []string{"testProduct1", "testProduct2", "testProduct3", "testProduct4"}
	return GiftList{
		AllowedProducts: allowedProducts,
		Entries: map[string]bool{
			"testProduct1": false,
			"testProduct2": false,
			"testProduct3": false,
			"testProduct4": false,
		},
	}
}

func TestAddEntry(t *testing.T) {
	testList := createEmptyTestList()
	_ = testList.AddEntry("testProduct1")

	require.Len(t, testList.Entries, 1)
	require.Contains(t, testList.Entries, "testProduct1")
	require.False(t, testList.Entries["testProduct1"])
	require.Error(t, testList.AddEntry("testProduct1"))
	require.Error(t, testList.AddEntry("testProduct99"))
}

func TestRemoveEntry(t *testing.T) {
	testList := createFullTestList()
	testList.RemoveEntry("testProduct2")
	require.Len(t, testList.Entries, 3)
	require.NotContains(t, testList.Entries, "testProduct2")
	require.Error(t, testList.RemoveEntry("testProduct2"))
}

func TestPurchaseItem(t *testing.T) {
	testList := createFullTestList()
	require.False(t, testList.Entries["testProduct1"])
	_ = testList.PurchaseItem("testProduct1")
	require.True(t, testList.Entries["testProduct1"])
	require.Error(t, testList.PurchaseItem("testProduct1"))
	require.Error(t, testList.PurchaseItem("testProduct99"))
}

func TestProductIsAllowed(t *testing.T) {
	testList := createFullTestList()
	require.True(t, testList.productIsAllowed("testProduct2"))
	require.False(t, testList.productIsAllowed("testProduct99"))
}
