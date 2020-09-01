package listmanager

import (
	"fmt"
	"strings"
	"text/tabwriter"
)

func ListProductsInList(giftList GiftList, productMap map[string]string) string {
	var builder strings.Builder
	writer := tabwriter.NewWriter(&builder, 0, 0, 0, ' ', tabwriter.Debug)
	for productCode := range giftList.Entries {
		fmt.Fprintf(writer, "%s\t%s\t\n", productCode, productMap[productCode])
	}
	writer.Flush()
	return builder.String()
}

func CreatePurchasingReport(giftList GiftList, productMap map[string]string) string {
	var builder strings.Builder
	writer := tabwriter.NewWriter(&builder, 0, 0, 0, ' ', tabwriter.Debug)
	writer.Write([]byte("Purchased List Items\n"))
	for productCode := range giftList.Entries {
		if giftList.Entries[productCode] {
			fmt.Fprintf(writer, "%s\t%s\t\n", productCode, productMap[productCode])
		}
	}
	writer.Write([]byte("\nUnpurchased List Items\n"))
	for productCode := range giftList.Entries {
		if !giftList.Entries[productCode] {
			fmt.Fprintf(writer, "%s\t%s\t\n", productCode, productMap[productCode])
		}
	}
	writer.Flush()
	return builder.String()
}
