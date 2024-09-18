# -------------------------------------------------------------------------------------------------
# -- Imports
# -------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tusmo import tusmo
from time import sleep
# -------------------------------------------------------------------------------------------------


# =================================================================================================
# =================================================================================================


# -------------------------------------------------------------------------------------------------
def game(  ):
    global vBrowser
    
    oTusmo            = tusmo( )
    
    vGrids            = vBrowser.find_elements( By.XPATH, "//div[contains(@class,'motus-grid')]" )
    vNbGrid           = len( vGrids )
    vMotusGrid        = vGrids[-1]
    vGuessWord        = "".join(vMotusGrid.text.split( "\n" ))
    
    oTusmo.WordLenght = len( vGuessWord )
    oTusmo.WordList   = [ lWord for lWord in oTusmo.WordList if ( lWord[ 0 ] == vGuessWord[ 0 ] and len( lWord ) == oTusmo.WordLenght ) and "-" not in lWord]
    
    vTry              = 0
    vBuffer           = 0

    # -----------------------------------------------
    # -- Loop
    while vTry <= oTusmo.nb_essai:
        # -- Generate word
        vProposedWord = oTusmo.generate_word( )

        # -- Type Word
        for lLetter in vProposedWord:
            vLetter[ vLetterList.index( lLetter ) ].click( )
        vEnterKey.click( )
        sleep( 0.5 )
        
        # -- Generate word map
        vWordMap    = [ ]
        vGrids      = vBrowser.find_elements( By.XPATH, "//div[contains(@class,'motus-grid')]" )
        vMotusGrid  = vGrids[-1]
        vMap        = vMotusGrid.find_elements(By.TAG_NAME, 'div')
        
        for ldiv in vMap[ vBuffer + 1 : vBuffer + (oTusmo.WordLenght * 2) + 1 : 2 ]:
            vclass = ldiv.get_attribute("class").split(" ")[-1]
            vWordMap.append( vclass )
        
        if ( set( vWordMap ) == { "r" } ) or ( len( vGrids ) > vNbGrid ):
            return
        
        # Generate new word list
        oTusmo.update_wordlist( vWordMap, vProposedWord )
        vBuffer += oTusmo.WordLenght * 2
        vTry += 1
# -------------------------------------------------------------------------------------------------


# =================================================================================================
# =================================================================================================


# -------------------------------------------------------------------------------------------------
# -- Generate Word list
# -------------------------------------------------------------------------------------------------
vLetterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# -- Connexion to Tusmo
# -------------------------------------------------------------------------------------------------
vBrowser = webdriver.Chrome( )
vBrowser.get( "https://www.tusmo.xyz/" )
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# -- Change language to French
# -------------------------------------------------------------------------------------------------
vElement = vBrowser.find_element( By.XPATH, "//img[contains(@alt,'en')]" )
vElement.click( )

vElement = vBrowser.find_element( By.XPATH, "//img[contains(@alt,'FR')]" )
vElement.click( )
sleep( 1 )
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# -- Click to start game
# -------------------------------------------------------------------------------------------------
vElement = vBrowser.find_element( By.XPATH, "//span[contains(text(),'Solo')]" )
# vElement = vBrowser.find_element( By.XPATH, "//div[contains(text(),'Mot du jour')]" )
# vElement = vBrowser.find_element( By.XPATH, "//div[contains(text(),'Suite du jour')]" )
vElement.click( )
sleep( 0.5 )
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# -- Get Letters
# -------------------------------------------------------------------------------------------------
vLetter = [ ]
for lLetter in vLetterList:
    vLetter.append( vBrowser.find_element( By.XPATH, f"//span[contains(text(),'{ lLetter }')]" ) )
    
vEnterKey = vBrowser.find_element(By.CLASS_NAME, "fa-sign-in-alt")
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# -- Game
# -------------------------------------------------------------------------------------------------
vIN = ""
vErreurCount = 0
while vErreurCount <= 3:
    try:
        game( )
    except Exception as e:
        # vErreurCount += 1
        print( e )
    sleep( 2.15 )
    # vIN = input( )    
