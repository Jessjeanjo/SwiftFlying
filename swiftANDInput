//
//  PracticeInput.swift
//  
//
//  Jessica Joseph on 4/1/15.
//  
//

import Foundation

func input() -> String{
    var keyboard = NSFileHandle.fileHandleWithStandardInput()
    var inputData = keyboard.availableData
    return NSString(data: inputData, encoding: NSUTF8StringEncoding)! //Swift requires a ('!' OR '?') at the end
    
    // Why is NSString considered to be an optional value?
    // What does it mean when an optional type is not unwrapped?
    // Why would I need to add the ('!' OR '?') at the end of the return statement?
    
    //ALSO, Since this function takes no parameter, how could I actually use it? 
}


//  Python 2.7 has the raw_input("..") BIF(built in function) and Python 3 has the input("...") BIF
//  What is the swift equivalent? As of right now it seems like there isn't any equivalent
//  Is Apple planning on adding a swift equivalent of raw_input() or input()?
