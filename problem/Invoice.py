class Invoice :
    def __init__(self,invoiceNumber, invoiceDate, company, companyAddress, billToName, billToAddress, invoiceItemHeadNode) :
        self.invoiceNumber = invoiceNumber
        self.invoiceDate = invoiceDate
        self.company = company
        self.companyAddress = companyAddress
        self.billToName = billToName
        self.billToAddress = billToAddress
        self.invoiceItemHeadNode = invoiceItemHeadNode

    # 請求書の支払総額を計算します。InvoiceItemHeadNodeから始まるすべてのリスト項目を反復処理し、数量も考慮して計算する必要があります。Tax inputがTrueに設定されている場合は、合計金額に10%を加算してください。
    def amountDue (self, taxes) : 
        currentNode = self.invoiceItemHeadNode
        total = 0 

        while currentNode is not None :
            total += currentNode.product.price * currentNode.quantity
            currentNode = currentNode.next

        return  total * 1.1 if taxes else total

    # 請求書の全項目と数量を出力します。「item :shampoo, price :10, quantity:7」のようにそれぞれのアイテムを出力してください。
    def printBuyingItems(self) :
        print("Printing the Item List...")
        currentNode = self.invoiceItemHeadNode
        while currentNode is not None :
            print("item :" + currentNode.product.title + ", price :" + str(currentNode.product.price) + ", quantity:" + str(currentNode.quantity))
            currentNode = currentNode.next


    # 請求書の全内容を出力します。以下のように出力してください。
    def printInvoice(self) :
        print(
            "Invoice\n" +
            "No. : " + self.invoiceNumber + "\n" +
            "INVOICE DATE : " + self.invoiceDate + "\n" +
            "SHIP TO : " + self.company + "\n" +
            "ADDRESS : " + self.companyAddress + "\n" +

            "BILL TO : " + self.billToName + "\n" +
            "ADDRESS : " + self.billToAddress + "\n" 
        )

        currentNode = self.invoiceItemHeadNode
        while currentNode is not None :
            print(currentNode.product.title + "($" +str(currentNode.product.price) +")" + "--- " + str(currentNode.quantity) + " pcs. " + "--- AMOUNT: " + str(currentNode.product.price * currentNode.quantity)) 
            currentNode = currentNode.next


        print(
            "SUBTOTAL : " + str(self.amountDue(False)) + "\n" +
            "TAX : " + str(self.amountDue(True) - self.amountDue(False)) + "\n" +
            "TOTAL : " + str(self.amountDue(True))
        )

class InvoiceItemNode :
    def __init__(self, product, quantity) :
        self.product = product
        self.quantity = quantity
        self.next = None

    # 購入する数量に基づいて、製品の合計価格を計算します。
    def getTotalPrice(self) :
        return self.quantity * self.product.price

class Product:
    def __init__(self, title, price) :
        self.title = title
        self.price = price

product1 = Product ("shampoo", 10)
product2 = Product ("conditioner", 5)
product3 = Product ("tooth brush", 3)

firstItem = InvoiceItemNode(product1, 7)
secondItem = InvoiceItemNode(product2, 9)
firstItem.next = secondItem
thirdItem = InvoiceItemNode(product3, 10)
secondItem.next = thirdItem

invoice = Invoice ("UC1234567890", "2020/05/06", "Recursion", "Los Angles", "Steven", "Dallas", firstItem)

invoice.printBuyingItems()
invoice.printInvoice()

print(invoice.amountDue(False))
print(invoice.amountDue(True))
