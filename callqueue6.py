class CallCenter:
    def __init__(self):
        self.call_queue = []

    def addCall(self, customerID, callTime):
        call = {'customerID': customerID, 'callTime': callTime}
        self.call_queue.append(call)
        print(f"\n✅ Call Added → Customer ID: {customerID}, Call Time: {callTime} mins")

    def answerCall(self):
        if self.isQueueEmpty():
            print("\n⚠️ No calls to answer! Queue is empty.")
        else:
            answered_call = self.call_queue.pop(0)
            print(f"\n📞 Answering call → Customer ID: {answered_call['customerID']}, Duration: {answered_call['callTime']} mins")

    def viewQueue(self):
        if self.isQueueEmpty():
            print("\n📭 No pending calls!")
        else:
            print("\n📌 Pending Calls in Queue:")
            for i, call in enumerate(self.call_queue, start=1):
                print(f"{i}. Customer ID: {call['customerID']}, Call Time: {call['callTime']} mins")

    def isQueueEmpty(self):
        return len(self.call_queue) == 0


# ---------------- MENU DRIVEN PROGRAM ----------------

center = CallCenter()

while True:
    print("\n===== CALL CENTER MENU =====")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Pending Calls")
    print("4. Check if Queue is Empty")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':
        cid = input("Enter Customer ID: ")
        ctime = int(input("Enter Call Time (minutes): "))
        center.addCall(cid, ctime)

    elif choice == '2':
        center.answerCall()

    elif choice == '3':
        center.viewQueue()

    elif choice == '4':
        if center.isQueueEmpty():
            print("\n✅ Queue is empty!")
        else:
            print("\n❌ Queue is NOT empty!")

    elif choice == '5':
        print("\n👋 Exiting Call Center System. Goodbye!")
        break

    else:
        print("\n⚠️ Invalid input! Please enter a valid option.")
