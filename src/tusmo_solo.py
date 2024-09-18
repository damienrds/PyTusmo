from random import choice

# -------------------------------------------------------------------------------------------------
# -- Constants
# -------------------------------------------------------------------------------------------------
kPath = "./liste_francais_NoAccent.txt"
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
def getWordList( inPath ):
    
    with open( inPath, "r", encoding="utf-8" ) as file:
        vWordList = file.read( ).splitlines( )
    
    return vWordList
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
def getWordMap( inGessWord, inProposition ):
        
        vWordMap = [ ]
        
        for i in range( len( inGessWord ) ):
            if inGessWord[ i ] == inProposition[ i ]:
                vWordMap.append( 2 )
            elif inProposition[ i ] in inGessWord:
                vWordMap.append( 1 )
            else:
                vWordMap.append( 0 )
        
        return vWordMap
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    vGuessWord = "alphabet"
    
    vWordList = getWordList( kPath )
    vStop = True
    
    vWordLenght = len( vGuessWord )
    vExcludeLetter = [ ]
    vIncludeLetter = [ ]
    vNB_essai = 0
    
    # First sort by first letter and length
    vWordList = [ vWord for vWord in vWordList if ( vWord[ 0 ] == vGuessWord[ 0 ] and len( vWord ) == vWordLenght ) and "-" not in vWord]
    vProposedWord = choice( vWordList )
    vWordMap      = getWordMap( vGuessWord, vProposedWord )
    vNB_essai += 1
    
    # Guess loop
    while vStop or vNB_essai > 7:
        # Update the exclude and include letter list
        for lIndex in range( vWordLenght ):
            if vWordMap[ lIndex ] == 1:
                vIncludeLetter.append( vProposedWord[ lIndex ] )
            elif vWordMap[ lIndex ] == 0:
                vExcludeLetter.append( vProposedWord[ lIndex ] )
        
        # Sort word
        for lLetter in set( vExcludeLetter ):
            vWordList = [ vWord for vWord in vWordList if lLetter not in vWord ]
            
        for lLetter in set( vIncludeLetter ):
            vWordList = [ vWord for vWord in vWordList if lLetter in vWord ]
            
        for vIndex in range( vWordLenght ):
            if vWordMap[ vIndex ] == 1:
                vWordList = [ vWord for vWord in vWordList if vWord[ vIndex ] != vProposedWord[ vIndex ] ]
            elif vWordMap[ vIndex ] == 2:
                vWordList = [ vWord for vWord in vWordList if vWord[ vIndex ] == vProposedWord[ vIndex ] ]

        vProposedWord = choice( vWordList )
        vWordMap      = getWordMap( vGuessWord, vProposedWord )
        vNB_essai     += 1
        
        if set( vWordMap ) == { 2 }:
            vStop = False
            print( f"The word is: {vProposedWord} ({vNB_essai} essai)" )
# -------------------------------------------------------------------------------------------------
    