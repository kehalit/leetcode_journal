/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x){

// Edge case 1: negative numbers are not palindromes
if (x < 0) return false

// Edge case 1: numbers ending with 0 (but not 0 it self are not Palindromes)
if (x % 10 === 0 && x !== 0 ) return false


let reverse = 0
let n = x

console.log(`starting reversal for x = ${x}`)

// step 1: build the reversed number
while (n >= 1 ) {

    let remainder = n % 10
    n = Math.floor(n/10)
    reverse = reverse * 10 + remainder
}

// step 2 compare reverse to the original
    
    return reverse === x
}

console.log(isPalindrome(10))