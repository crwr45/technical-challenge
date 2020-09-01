package listmanager

import (
	"testing"
)

var productMap = map[string]string{
	"testProduct1": "A Beautiful Chandelier",
	"testProduct2": "A Big Car",
	"testProduct3": "A Blue Cat",
	"testProduct4": "A Balancing Coin",
}

func TestListProducts(t *testing.T) {
	testList := createFullTestList()
	_ = ListProductsInList(testList, productMap)
}

func TestCreatePurchasingReport(t *testing.T) {
	testList := createFullTestList()
	testList.PurchaseItem("testProduct1")
	_ = CreatePurchasingReport(testList, productMap)
}
