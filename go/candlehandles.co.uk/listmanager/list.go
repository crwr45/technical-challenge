package listmanager

import (
	"fmt"
)

// GiftList is a collection of Entries and is responsible
// for managing those entries
type GiftList struct {
	AllowedProducts []string
	Entries         GiftListEntryStatus
}

// GiftListEntryStatus is a map of product code to purchased status.
// Presence in the map means the item is wanted.
type GiftListEntryStatus map[string]bool

// AddEntry will add a new Entry to the GiftList, if the product
// is not already present and if it is allowed.
func (giftList *GiftList) AddEntry(productCode string) error {
	if !giftList.productIsAllowed(productCode) {
		return fmt.Errorf("product %s is not allowed in gift list", productCode)
	}
	if giftList.containsProduct(productCode) {
		return fmt.Errorf("product %s is already in gift list", productCode)
	}

	giftList.Entries[productCode] = false
	return nil
}

// RemoveEntry removes an Entry from the GiftList if it is present.
func (giftList *GiftList) RemoveEntry(productCode string) error {
	if !giftList.containsProduct(productCode) {
		return fmt.Errorf("product %s is not in the list", productCode)
	}

	delete(giftList.Entries, productCode)
	return nil
}

// PurchaseItem marks an Entry in the GiftList as purchased, if it is
// in the list.
func (giftList *GiftList) PurchaseItem(productCode string) error {
	if !giftList.containsProduct(productCode) {
		return fmt.Errorf("product %s is not in the list", productCode)
	}
	if giftList.itemIsPurchased(productCode) {
		return fmt.Errorf("product %s has already been purchased", productCode)
	}
	giftList.Entries[productCode] = true
	return nil
}

// getEntryForProduct finds the GiftListEntry for the product and returns a pointer to it,
// and an error if the product isn't in the Gift List.
func (giftList *GiftList) itemIsPurchased(productCode string) bool {
	return giftList.Entries[productCode]
}

func (giftList *GiftList) containsProduct(productCode string) bool {
	if _, ok := giftList.Entries[productCode]; ok {
		return true
	}
	return false
}

func (giftList *GiftList) productIsAllowed(productCode string) bool {
	for _, v := range giftList.AllowedProducts {
		if v == productCode {
			return true
		}
	}
	return false
}
