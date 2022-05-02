#%% 
def Searcher():
    import time
    Greetings = "Hello World, How are you all doing ?"
    
    # Below is Optional: I am giving it time to read something...
    time.sleep(5)

    while True:
        txt = yield
        if txt in Greetings:
            print('present...')
        else:
            print('Not present')

mySearch = Searcher()
next(mySearch)
mySearch.send('hey')

#%% You can continue to send it until closed

mySearch.send('World')
mySearch.send('you')

#%% Now let's close it 
mySearch.close()

#%% Now you can't send it anymore can continue to send it until closed

mySearch.send('World')
mySearch.send('you')
