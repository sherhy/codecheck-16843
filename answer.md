[あなたのコードがどのように動作するのか、簡潔に説明してください。]
sorry the code is dirty

main takes in the arguments and checks for erroneous inputs (sys.exit(1))

main calls f(n,seed), which starts the recursive calls

f seeks results from the api call --> which stores its data in the memo hash before returning,

f should check for data in memo hash before calling askServer()
